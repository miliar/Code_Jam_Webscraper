#include<stdio.h>
#define BIGINT_LEN 21

int rotationcnt;
int maxsit;
int groupcnt;
int	groups[1000];
int gsum[1000]; // gsum[i] : i번째 그룹이 선두일 때,총 탈 수 있는 인원 수
int glink[1000]; // glist[i] : i번째 group이 선두일 때, 다음 선두 그룹의 위치
int gvisited[1000]; // gvisited[i] : cycle check할 때, 방문했는가?
int gcyclestart; // cycle이 시작되는 지점

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
		
		// cyclesum, sum 초기화.
		sum_len = cyclesum_len = 0;
		for(i = 0; i < BIGINT_LEN; i++)
			cyclesum[i] = sum[i] = 0;
		// gvisited 초기화.
		for(i = 0; i < groupcnt; i++)
			gvisited[i] = false;


		// 이제 glink를 만든다..
		for(i = 0; i < groupcnt; i++){
			// glink[i]를 구함...
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
				// 한바퀴 돈당 ㅋㅋㅋ
				glink[i] = i;
		}

		// 0에서부터 시작해서, cycle을 찾는다. 찾은 cycle에 포함되는 node의 gsum을 다 합해놓음.
		int focus = 0;
		int totallength = 0;
		while(!gvisited[focus]){
			gvisited[focus] = true;
			focus = glink[focus];
			totallength++;
		}

		/* rotationcnt만큼!
		만약 rotationcnt < totallength라면 : 그냥 다 더함.
		만약 rotationcnt > totallength라면 : 
				totalcnt - cyclelength만큼 더하고, 최대 가능한 cyclelength를 더해주고, 마지막 남은 찌꺼기는 직접더해줌
		*/
		if(rotationcnt < totallength){
			focus = 0;
			while(rotationcnt--){
				bigint_add(sum, gsum[focus], sum_len);
				focus = glink[focus];
			}
		}else{
			// 현재 focus값 : cycle이 시작되는 node의 값
			// 아래 루프를 실행해도 focus는 여전히 cycle이 시작되는 node의 값.
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