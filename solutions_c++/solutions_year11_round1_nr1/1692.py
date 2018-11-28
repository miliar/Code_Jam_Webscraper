// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
using namespace std;
int T,N,PD,PG;
void main()
{
	freopen("A-small-attempt5.in","r",stdin);
	//freopen("a.txt","r",stdin);
	freopen("c.txt","w",stdout);
	cin>>T;
	int CaseId,i,j;
	for(CaseId=1;CaseId<=T;CaseId++)
	{
		cin>>N>>PD>>PG;
		if(PD==100)
		{
			if(PG!=0)
				cout<<"Case #"<<CaseId<<": Possible"<<endl;
			else
				cout<<"Case #"<<CaseId<<": Broken"<<endl;
		}
		else if(PG==100)
			cout<<"Case #"<<CaseId<<": Broken"<<endl;
		else
		{
			if(PD==0)
				cout<<"Case #"<<CaseId<<": Possible"<<endl;
			else
			{
				if(PG==0)
					cout<<"Case #"<<CaseId<<": Broken"<<endl;
				else
				{
					int m=PD;
			int n=100;
			int r,gcd,temp;
			r=0;
			gcd=0;
			temp=0;
			i=0;
			j=0;
			while((r=m%n)!=0)
			{ m=n; n=r; }
			gcd=n;
			if(N<=100)
			{
				temp=100/gcd;
				for(i=1;i<=gcd;i++)
				{
					j=temp*i;
					if(j<=N)
					{
						cout<<"Case #"<<CaseId<<": Possible"<<endl;
						break;
					}
				}
				if(i==gcd+1)
					cout<<"Case #"<<CaseId<<": Broken"<<endl;
			}
				}
			}
		}
	}
}
