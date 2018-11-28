#include<stdio.h>
#include <algorithm>

using namespace std;

int T;
int p,q;
int dat[101];
int l, r;
int ans;
int check[100];
int ii[5];
int li[101];

int temp[1001];
void back(int a)
{
	int i,j;
	int l, r, tmp;	
	if(a>=q)
	{
		l = 1;
		r = p;
		for(i=0;i<=p;i++) temp[i] = 1;
		tmp = 0;
		for(i=0;i<q;i++)
		{
			temp[li[i]] = 0;
			for(j=li[i]+1;j<=p;j++)
			{
				if(temp[j] == 1) tmp++;
				else break;
			}
			for(j=li[i]-1;j>=1;j--)
			{
				if(temp[j] == 1) tmp ++;
				else break;
			}
		}
		if(ans>tmp) ans = tmp;
	}
	for(i=0;i<q;i++)
	{
		if(check[i] == 0)
		{
			li[a] = dat[i];
			check[i] = 1;
			back(a+1);	
			check[i] = 0;
			li[a] = 0;
		}
	}
}
int main()
{

	int testcase,i,j,max, mp;
	int rightest;
	int li, ri;
	FILE *fp, *fp1;
	fp=fopen("input.txt","r");
	fp1=fopen("output.txt","w");
	fscanf(fp,"%d",&T);
	for(testcase = 1; testcase<=T; testcase++)
	{
		fscanf(fp,"%d %d",&p,&q);
		for(i=0;i<q;i++) fscanf(fp,"%d",&dat[i]);
		sort(dat, dat + q);

		ans = 999999999;
		back(0);

		fprintf(fp1,"Case #%d: %d\n",testcase, ans);
		
	}
}