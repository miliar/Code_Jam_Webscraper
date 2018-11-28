#include  <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
using namespace std;
int r,l,n;
bool c[10000]={false};
int d[10000]={0};
int a[10000],b[10000];
int le=0;
int xun=0;
int bNum=0;
long al;
int jie;
void init()
{
	le=0;
	xun=0;
	bNum=0;
	for(int i=0;i<n;i++)
		c[i]=false;
	int temp=0;
	int i=0;
	
	while(c[temp]==false)
	{
		d[temp]=bNum;
		c[temp]=true;
		le=0;
		while(true)
		{
			le+=a[i];
			i++;
			i%=n;
			if(le+a[i]>l||le+a[i]>al)
				break;
		}
		temp=i;
		b[bNum++]=le;
		
	}
	jie=d[temp];
}

int main()
{
	ofstream fout ("google.out");
    ifstream fin ("google.in");
	int m;
	fin>>m;
	for(int i=0;i<m;i++)
	{
		fin>>r>>l>>n;
		al=0;
		for(int j=0;j<n;j++)
		{
			fin>>a[j];
			al+=a[j];
		}
		init();
		int alb=0;
		for(int k=jie;k<bNum;k++)
			alb+=b[k];
		int zon=(r-jie)/(bNum-jie);
		int yu=(r-jie)%(bNum-jie);
		int re=0;
		for(int k=jie;k<jie+yu;k++)
			re+=b[k];
		for(int k=0;k<(jie>r? r:jie);k++)
			re+=b[k];
		re+=zon*alb;
		fout<<"Case #"<<i+1<<": "<<re<<endl;
	}
	return 1;
}