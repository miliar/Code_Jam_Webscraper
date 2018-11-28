#include <iostream>
#include <fstream>
#include<string.h>

using namespace std;
ofstream fout ("jam3.out");
ifstream fin ("C-small-attempt0.in");
short almat[127][510];
char mm[20]="welcome to code jam";
int st[510];
int main()
{
	int T,i,strl,k,ss,j,sum,p,ct,gt;
	char str[510],ch,ch1,c;
	fin>>T;
	fin.get(c);
	for(i=0;i<T;++i)
	{
		fin.getline(str,310);
		strl=strlen(str);
		for(k=0;k<127;++k)
			almat[k][0]=1;
		memset(st,0,sizeof(st));
		for(k=strl-1;k>=0;--k)
		{
			ch=str[k];
			almat[ch][almat[ch][0]]=k;
			almat[ch][0]++;
			if(ch=='m')
				st[k]=1;
		}
		for(j=17;j>=0;--j)
		{
			ch=mm[j+1];
			ch1=mm[j];
			sum=0;
			for(k=1,p=1;p<almat[ch1][0];++p)
			{
				while((almat[ch][k]>almat[ch1][p])&&(k<almat[ch][0]))
				{
					sum+=st[almat[ch][k]];
					sum%=10000;
					++k;
				}
				st[almat[ch1][p]]=sum;
			}
		}
		ss=0;
		for(j=1;j<almat['w'][0];++j)
		{
			ss+=st[almat['w'][j]];
			ss%=10000;
		}
		ct=ss/1000;
		fout<<"Case #"<<i+1<<": "<<ct;
		gt=(ss-ct*1000)/100;		
		fout<<gt;
		gt=(ss-ct*1000-gt*100)/10;
		fout<<gt<<ss%10<<endl;
	}

	return 0;
}