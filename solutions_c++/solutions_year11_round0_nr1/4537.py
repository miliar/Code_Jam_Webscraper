#include<stdio.h>
int T;
int n;
char turn[200];
int location[200];
int b,o;
int bl,ol;
int blue[200];
int orange[200];

int main(void)
{
	int i,j,t;
	int result;
	int Case;
	int inc_b, inc_o;
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");
	fscanf(in,"%d",&T);
//	scanf("%d",&T);

	Case = 1;
	while(T-- > 0){
		b = 0; o = 0;
		fscanf(in,"%d\n", &n);
//		scanf("%d\n", &n);
		for(i = 0; i < n; i++)
		{
			fscanf(in,"%c %d ",&turn[i], &location[i]);
//			scanf("%c %d ",&turn[i], &location[i]);
			if(turn[i] == 'O') orange[o++] = location[i];
			else blue[b++] = location[i];
		}

		bl = 1; ol = 1; t = 0; result = 0;
		inc_b = 1; inc_o = 1;
		i = 0; j = 0;
		while(1){
			if(t >= n) break;
			if(turn[t] == 'O' && ol == location[t]){
				i++;
				t++;
				if(orange[i] > ol) inc_o = 1;
				else if(orange[i] < ol) inc_o = -1;

				if(blue[j] != bl) bl += inc_b;
				result++;
				continue;
			}
			else if(turn[t] == 'B' && bl == location[t]){
				j++;
				t++;
				if(blue[j] > bl) inc_b = 1;
				else if(blue[j] < bl) inc_b = -1;

				if(orange[i] != ol) ol += inc_o;
				result++;
				continue;
			}

			if(blue[j] != bl) bl += inc_b;
			if(orange[i] != ol) ol += inc_o;
			result++;
		}
		
//		printf("Case #%d: %d\n",Case++, result);
		fprintf(out,"Case #%d: %d\n",Case++, result);
	}
	fclose(in);
	fclose(out);
	return 0;
}