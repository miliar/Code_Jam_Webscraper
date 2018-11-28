#include<iostream>
#include<cstdio>
#include<algorithm>
#define MAXL 1010
#define INF 1000000000
using namespace std;

char bin[MAXL][25];
char ans[25];

int main()
{
	int Min;
	int T,N;
	int i,j;
	int t = 0;
	int a;
	int maxlen,sum;
	int cnt1;
	bool find;
	FILE *fin = fopen("C-large.in","r");
	FILE *fout = fopen("C-large.txt","w");
	fscanf(fin,"%d",&T);
	while(T--)
	{
		find = true;
		fscanf(fin,"%d",&N);
		for(i=0;i<MAXL;i++)
			for(j=0;j<25;j++)
				bin[i][j] = '0';
		for(i=0;i<25;i++)
			ans[i] = '0';
		Min = INF;
		sum = 0;
		maxlen = -1;
		for(i=0;i<N;i++)
		{
			fscanf(fin,"%d",&a);
			Min = min(Min,a);
			sum += a;
			cnt1 = 0;
			while(a != 0)
			{
				if( (a&1) == 1)
				{
					bin[i][cnt1++] = '1';	
					
				}
				else
				{
					bin[i][cnt1++] = '0';
				}
				a = a >> 1;
			}
			maxlen = max(cnt1,maxlen);
		}
		for(i=0;i<N;i++)
			reverse(bin[i],bin[i]+maxlen);
	
		for(i=0;i<N;i++)
		{
			for(j=0;j<maxlen;j++)
			{
				if(ans[j] == '0' && bin[i][j] == '0')
					ans[j] = '0';
				else if(ans[j] == '0' && bin[i][j] == '1')
					ans[j] = '1';
				else if(ans[j] == '1' && bin[i][j] == '0')
					ans[j] = '1';
				else if(ans[j] == '1' && bin[i][j] == '1')
					ans[j] = '0';
			}
		}
		for(i=0;i<maxlen;i++)
		{
			if(ans[i] == '0')
				continue;
			else
			{
				find = false;
				break;
			}
		}	
		if(!find)
			fprintf(fout,"Case #%d: NO\n",++t);
		else
			fprintf(fout,"Case #%d: %d\n",++t,sum-Min);
		//printf("C = %d\n",C);
	}
	return 0;
}
