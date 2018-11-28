// 3C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
#include<math.h>
using namespace std;
int T;
int N;
int L,H;
int a[102];
void main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("b.txt","w",stdout);
	cin>>T;
	int caseId,i,j,k;
	for(caseId=1;caseId<=T;caseId++)
	{
		cin>>N>>L>>H;
		memset(a,0,sizeof(a));
		for(i=1;i<=N;i++)
		{
			cin>>a[i];
		}
		int min;
		for(i=L;i<=H;i++)
		{
			for(j=1;j<=N;j++)
			{
				if(i%a[j]!=0&&a[j]%i!=0)
					break;
			}
			if(j==N+1)
			{ 
				min=i;
				cout<<"Case #"<<caseId<<": "<<min<<endl;
				break;
			}
		}
		if(i==H+1)
			cout<<"Case #"<<caseId<<": NO"<<endl;
	}
}