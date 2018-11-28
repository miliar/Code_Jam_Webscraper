#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int T;
char dat[1000];
FILE *fp1;

void solve()
{
	int i,j,befi;
	int max, tmp, mp,min;
	max = -1;
	befi = -1;
	for(i=strlen(dat) - 1; i>= 0; i--)
	{
		if(max <= dat[i])
		{
			max = dat[i];
			mp = i;
		}
		else
		{
			min = 99999;

			for(j=i+1;j<strlen(dat);j++)
			{
				if(min > dat[j] && dat[j] > dat[i]) { min = dat[j]; mp = j; }
			}
			tmp = dat[i];
			dat[i] = min;
			dat[mp] = tmp;

			befi=i;
			break;
		}
	}
	if(befi != -1)
	{
		for(i=befi+1;i<strlen(dat);i++)
		{
			for(j=i+1;j<strlen(dat);j++)
			{
				if(dat[i] > dat[j])
				{
					tmp = dat[i];
					dat[i] = dat[j];
					dat[j] = tmp;
				}
			}
		}
		fprintf(fp1,"%s\n",dat);
	}
	else
	{
		befi = -1;
		for(i=befi+1;i<strlen(dat);i++)
		{
			if(i!=0)
			{
				for(j=i+1;j<strlen(dat);j++)
				{
					if(dat[i] > dat[j])
					{
						tmp = dat[i];
						dat[i] = dat[j];
						dat[j] = tmp;
					}
				}
			}
			else
			{
				for(j=i+1;j<strlen(dat);j++)
				{
					if(dat[i] > dat[j] && dat[j] != '0')
					{
						tmp = dat[i];
						dat[i] = dat[j];
						dat[j] = tmp;
					}
				}
			}
		}
		fprintf(fp1, "%d0%s\n", dat[0]-'0',dat+1);
	}
	
}
int main()
{
	int testcase;
	FILE *fp;
	fp=fopen("input.txt","r");
	fp1=fopen("output.txt","w");
	fscanf(fp,"%d",&T);
	for(testcase = 1; testcase <= T; testcase++)
	{
		fscanf(fp,"%s", dat);
		fprintf(fp1,"Case #%d: ",testcase);
		solve();
	}
	fclose(fp1);
	fclose(fp);


}