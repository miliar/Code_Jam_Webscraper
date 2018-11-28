#include <stdio.h>

int n,l,chk[5],tchk[5];
double pro[5],temp;

int goback(int x,int y)
{
	int i,cnt,cp;
	double pr;
	if(x==n)
	{
		pr=1;
		for(i=0;i<n;i++)
		{
			if(chk[i]==1) // true
				pr*=pro[i];
			else //false
				pr*=(1.0-pro[i]);
		}
		for(i=0;i<n;i++)
			tchk[i]=chk[i];
		for(i=0;i<y;i++)
			tchk[n-1-i]=1;
		cnt=y;
		cp=0;
		for(i=0;i<n;i++)
		{
			if(tchk[i]==0)
			{
				cp=1;
				break;
			}
		}
		cnt+=l-(n-y)+1;
		if(cp==1)
			cnt+=l+1;
			
		temp+=pr*cnt;
		return 0;
	}
	chk[x]=1;
	goback(x+1,y);
	chk[x]=0;
	goback(x+1,y);
	return 0;
}

int main()
{
	int t,tcase;
	int i;
	double re;

	FILE *in,*out;
	in=fopen("A-small-attempt1.in","r");
	out=fopen("output.txt","w");

	fscanf(in,"%d",&tcase);

	for(t=0;t<tcase;t++)
	{
		for(i=0;i<5;i++)
			chk[i]=0;

		fscanf(in,"%d",&n);
		fscanf(in,"%d",&l);
		for(i=0;i<n;i++)
			fscanf(in,"%lf",&pro[i]);
		re=99999;
		if(t==13)
			printf("");
		for(i=0;i<=n;i++)
		{
			temp=0;
			goback(0,i);
			if(re>temp)
				re=temp;
		}
		if(re>l+2)
			re=l+2;
		fprintf(out,"Case #%d: %lf\n",t+1,re);
	}
	return 0;
}