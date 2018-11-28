// a2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<memory>
#include<algorithm>
using namespace std;
double p[10];
double result[10];
double per[10];
double min(double a,double b)
{
	if(a<=b)
	{ return a; }
	else
	{ return b;}
}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("b.txt","w",stdout);
	int T,i,j,A,B;
	cin>>T;
	for(int caseId=1;caseId<=T;caseId++)
	{
		cin>>A>>B;
		memset(per,0,10);
		memset(p,0,10);
		memset(result,0,10);
		
		for(i=1;i<=A;i++)
		{
			cin>>p[i];
		}
		if(A==1)
		{
			per[1]=p[1];
			per[2]=1-p[1];

			result[1]=(B-A+1)*per[1]+(2*B-A+2)*per[2];
			result[2]=B+2;
			result[3]=B+2;

			sort(result+1,result+4);
			
			cout<<"Case #"<<caseId<<": ";	
			printf("%.6f",result[1]);
			cout<<endl;
			
		}
		else if(A==2)
		{
			per[1]=p[1]*p[2];
			per[2]=p[1]*(1-p[2]);
			per[3]=(1-p[1])*p[2];
			per[4]=(1-p[1])*(1-p[2]);

			result[1]=(B-1)*per[1]+2*B*per[2]+2*B*per[3]+2*B*per[4];
			result[2]=(B+1)*(per[1]+per[2])+(2*B+2)*(per[3]+per[4]);
			result[3]=B+3;
			result[4]=B+2;
			sort(result+1,result+5);
			cout<<"Case #"<<caseId<<": ";
			printf("%.6f",result[1]);
			cout<<endl;
		}
		else 
		{
			per[1]=p[1]*p[2]*p[3];
			per[2]=p[1]*p[2]*(1-p[3]);
		    per[3]=p[1]*(1-p[2])*p[3];
			per[4]=(1-p[1])*p[2]*p[3];
			per[5]=p[1]*(1-p[2])*(1-p[3]);
			per[6]=(1-p[1])*p[2]*(1-p[3]);
			per[7]=(1-p[1])*(1-p[2])*p[3];
			per[8]=(1-p[1])*(1-p[2])*(1-p[3]);

			result[1]=(B-2)*per[1]+(2*B-1)*(1-per[1]);
			result[2]=B*(per[1]+per[2])+(2*B+1)*(1-per[2]-per[1]);
			result[3]=(B+2)*(per[1]+per[2]+per[3]+per[5])+(2*B+3)*(1-(per[1]+per[2]+per[3]+per[5]));
			result[4]=B+4;
			result[5]=B+2;

			sort(result+1,result+6);
			cout<<"Case #"<<caseId<<": ";
			printf("%.6f",result[1]);
			cout<<endl;
		}
	}		

	return 0;
}

