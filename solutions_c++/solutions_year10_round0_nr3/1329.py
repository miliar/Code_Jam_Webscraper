#include<stdio.h>
#define BIGINT_LEN 21

int rotationcnt;
int maxsit;
int groupcnt;
int	groups[1000];
int gsum[1000]; // gsum[i] : i��° �׷��� ������ ��,�� Ż �� �ִ� �ο� ��
int glink[1000]; // glist[i] : i��° group�� ������ ��, ���� ���� �׷��� ��ġ
int gvisited[1000]; // gvisited[i] : cycle check�� ��, �湮�ߴ°�?
int gcyclestart; // cycle�� ���۵Ǵ� ����

char cyclesum[BIGINT_LEN]; // big integer..
int cyclesum_len;
char sum[BIGINT_LEN];
int sum_len;

FILE *fin;
FILE *fout;


//////////////////// BIGINT Implementation ///////////////////////////
void bigint_add(char *chrs, int a, int &len){
	int digit = 0;
	for(digit = 0; digit < BIGINT_LEN; digit++){
		if(chrs[digit] == 0 && a == 0){
			break;
		}

		chrs[digit] = chrs[digit] + (a % 10);
		if(chrs[digit] >= 10){
			chrs[digit + 1]++;
			chrs[digit] -= 10;
		}

		a /= 10;
	}
	if(digit > len)
		len = digit;
}
void bigint_add(char *dst, const char *src, int &dstlen){
	int digit = 0;
	for(digit = 0; digit < BIGINT_LEN; digit++){
		dst[digit] = dst[digit] + src[digit];
		if(dst[digit] >= 10){
			dst[digit + 1]++;
			dst[digit] -= 10;
		}
	}
	for(dstlen = BIGINT_LEN; dstlen >= 1; dstlen--)
		if(dst[dstlen - 1] != 0)
			break;
}
void bigint_print(char *chrs, int len){
	if(len == 0)
		fprintf(fout, "0");
	else{
		while(len--){
			fprintf(fout, "%d", (int)chrs[len]);
		}	
	}
}
//////////////////////// END BIGINT IMPLEMENTATION //////////////////////


int main(){
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	int casecnt, curcasecnt;
	fscanf(fin, "%d", &casecnt);
	curcasecnt = casecnt;
	int i, j;


	while(curcasecnt--){
		fscanf(fin, "%d %d %d", &rotationcnt, &maxsit, &groupcnt);
		for(i = 0; i < groupcnt; i++)
			fscanf(fin, "%d", &groups[i]);
		
		// cyclesum, sum �ʱ�ȭ.
		sum_len = cyclesum_len = 0;
		for(i = 0; i < BIGINT_LEN; i++)
			cyclesum[i] = sum[i] = 0;
		// gvisited �ʱ�ȭ.
		for(i = 0; i < groupcnt; i++)
			gvisited[i] = false;


		// ���� glink�� �����..
		for(i = 0; i < groupcnt; i++){
			// glink[i]�� ����...
			gsum[i] = 0;
			glink[i] = -1;
			for(j = i; j < groupcnt + i; j++){
				if(gsum[i] > maxsit - groups[j % groupcnt]){
					glink[i] = j % groupcnt;
					break;
				}
				gsum[i] += groups[j % groupcnt];
			}
			if(glink[i] == -1)
				// �ѹ��� ���� ������
				glink[i] = i;
		}

		// 0�������� �����ؼ�, cycle�� ã�´�. ã�� cycle�� ���ԵǴ� node�� gsum�� �� ���س���.
		int focus = 0;
		int totallength = 0;
		while(!gvisited[focus]){
			gvisited[focus] = true;
			focus = glink[focus];
			totallength++;
		}

		/* rotationcnt��ŭ!
		���� rotationcnt < totallength��� : �׳� �� ����.
		���� rotationcnt > totallength��� : 
				totalcnt - cyclelength��ŭ ���ϰ�, �ִ� ������ cyclelength�� �����ְ�, ������ ���� ���� ����������
		*/
		if(rotationcnt < totallength){
			focus = 0;
			while(rotationcnt--){
				bigint_add(sum, gsum[focus], sum_len);
				focus = glink[focus];
			}
		}else{
			// ���� focus�� : cycle�� ���۵Ǵ� node�� ��
			// �Ʒ� ������ �����ص� focus�� ������ cycle�� ���۵Ǵ� node�� ��.
			int cyclelength = 0;
			while(gvisited[focus]){
				bigint_add(cyclesum, gsum[focus], cyclesum_len);
				gvisited[focus] = false;
				focus = glink[focus];
				cyclelength++;
			}

			int addingfocus = 0;
			while(addingfocus != focus){
				bigint_add(sum, gsum[addingfocus], sum_len);
				
				addingfocus = glink[addingfocus];
				rotationcnt--;
			}

			for(i = 0; i < rotationcnt / cyclelength; i++){
				bigint_add(sum, cyclesum, sum_len);
			}

			rotationcnt -= (rotationcnt / cyclelength) * cyclelength;
			
			addingfocus = focus;
			while(rotationcnt--){
				bigint_add(sum, gsum[addingfocus], sum_len);
				addingfocus = glink[addingfocus];
			}
		}

		fprintf(fout, "Case #%d: ", casecnt - curcasecnt);
		bigint_print(sum, sum_len);
		fprintf(fout, "\n");
	}

	return 0;
}