#include<iostream>
using namespace std;
#define INT __int64
int binNum(int x)
{
	int ret=0;
	while(x) { x/=2; ret++;}
	return ret;
}
int main(void)
{
	FILE*in=fopen("D:\\in.txt","r");
	FILE*out=fopen("D:\\out.txt","w");
	int test;
	fscanf(in,"%d",&test);
	for(int i=1;i<=test;i++)
	{
		INT l,p,c;
		fscanf(in,"%I64d%I64d%I64d",&l,&p,&c);
		int num=0;
		INT mul=l;
		while(mul<p)
		{
			num++;
			mul=mul*c;
		}
		num--;
		//cout<<num<<endl;
		fprintf(out,"Case #%d: %d\n",i,binNum(num));
	}
	return 0;
}