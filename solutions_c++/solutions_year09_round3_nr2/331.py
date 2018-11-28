// b.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <iomanip>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;


int main()
{
	fstream in("B-large.in",ios::in),out("B-large.out",ios::out);
	int T;
	int i,j,k,M,N;
	long long a1,b1,b2,a2,a3,b3;
	long long a,b,c;
	long double tmin,dmin;
	in>>T;
	for(i=0;i<T;i++)
	{
		in>>N;
		int **p=new int *[N];
		for(k=0;k<N;k++)
			p[k]= new int[6];
		for(j=0;j<N;j++)
			for(k=0;k<6;k++)
				in>>p[j][k];
		a1=0,b1=0,b2=0,a2=0,a3=0,b3=0;
		for(j=0;j<N;j++)
		{
			a1+=p[j][0];
			a2+=p[j][1];
			a3+=p[j][2];
			b1+=p[j][3];
			b2+=p[j][4];
			b3+=p[j][5];
		}
//		cout<<a1<<" "<<a2<<" "<<a3<<endl;
		a=b1*b1+b2*b2+b3*b3;
		c=a1*a1+a2*a2+a3*a3;
		b=2*(a1*b1+a2*b2+a3*b3);
		if(b<0)
		{
	//		cout<<-b<<" "<<2*a<<endl;
	//		tmin=((double)(1/3));
			tmin=static_cast<double>(-b)/static_cast<double>(2*a);
	//		cout<<tmin<<endl;
	//		tmin=static_cast<double>(-b/(2*a));
			dmin=sqrt(static_cast<double>(a*tmin*tmin+b*tmin+c))/N;
			out<<fixed<<setprecision(8);
			out<<"Case #"<<i+1<<": "<<dmin<<" "<<tmin<<endl;
		}
		else
		{
			tmin=0;
			dmin=sqrt(static_cast<double>(c))/N;
			out<<fixed<<setprecision(8);
			out<<"Case #"<<i+1<<": "<<dmin<<" "<<tmin<<endl;
		}
		delete [] p;

	}

	in.close();
	out.close();
	return 0;
}


