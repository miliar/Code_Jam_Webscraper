#include<stdio.h>
#include<string.h>

int T;
int testcase;
char dat[1001];
int map[1001];
long long ans;
long long tmp;
int main()
{
	int i,base,r;
	FILE *fp, *fp1;
	fp = fopen("input.txt","r");
	fp1 = fopen("output.txt","w");
	fscanf(fp,"%d",&T);
	for(testcase=1;testcase<=T;testcase++)
	{
		for(i=0;i<1000;i++){
			map[i] = -2;
		}
		fscanf(fp,"%s",dat);
		base = 0;
		for(i=0;i<strlen(dat);i++)
		{
			if(map[dat[i]] == -2) 
			{
				base ++;
				map[dat[i]] = -1;
			}
		}
		if(base == 1) base = 2;

		map[dat[0]] = 1;
		r = 0;
		for(i=1;i<strlen(dat);i++)
		{
			if( map[dat[i]] == -1 )
			{
				if(r != 1) map[dat[i]] = r++;
				else {
					map[dat[i]] = 2;
					r= 3;
				}
			}
		}

		ans = 0;
		tmp = (long long) 1;
		for(i=strlen(dat)-1;i>=0;i--)
		{
			ans += (long long)tmp * (long long)map[dat[i]];
			tmp *= (long long)base;
		}
		
		fprintf(fp1,"Case #%d: %lld\n",testcase, ans);

	}
}