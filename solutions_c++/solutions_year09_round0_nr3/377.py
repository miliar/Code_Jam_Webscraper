#include <stdio.h>
#include <string.h>

int dy[501][20];
int T;

int main()
{
	FILE *fp, *fp1;
	int testcase, i,j,l,k,r;
	char inp[501];
	char str[] = "welcome to code jam";

	fp=fopen("C.in","r");
	fp1=fopen("C.out","w");
	
	fscanf(fp,"%d",&T);

	for(testcase=0; testcase<T; testcase++)
	{
		char temp;
		l=0;
		while(1){
			temp = fgetc(fp);
			if(temp >= 'a' && temp <= 'z') break;
		}
		while(1)
		{
			if(temp == '\n' || temp == EOF) break;
			inp[l++] = temp;
			temp = fgetc(fp);
		}
		inp[l] = 0;

		for(i=0;i<500;i++) for(j=0;j<20;j++) dy[i][j] = 0;

		for(i=0;i<l;i++)
		{
			for(j=0;j<strlen(str);j++)
			{
				if( j > i ) break;
				if( inp[i] != str[j] ) continue;
	
				r = 0;
				if(j==0) dy[i][j] = 1;
				else {
					for(k=0;k<i;k++)
					{
						r+=dy[k][j-1];
						r=r%10000;
					}
					dy[i][j] = r;
				}
			}
		}

		r = 0;
		for(i=0;i<l;i++)
		{
			r += dy[i][strlen(str)-1];
			r=r%10000;
		}
		fprintf(fp1,"Case #%d: %04d\n",testcase+1,r);
	}
}