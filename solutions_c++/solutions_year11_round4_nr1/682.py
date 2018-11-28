// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <Windows.h>
using namespace std;

struct CORR
{
	double length;
	double w;
};

bool comp( CORR a , CORR b )
{
	return a.w < b.w;
}

int _tmain(int argc, _TCHAR* argv[])
{
	SetCurrentDirectoryA("D:\\codejam\\2\\A\\A\\Debug");
	int nT;
	FILE * fin = fopen("in.txt","r" );
	FILE * fout = fopen("out.txt","w" );

	fscanf( fin , "%d" , &nT );

	for( int nt = 1 ; nt <= nT ; nt++ )
	{
		double X,S,R,t;
		int N;
		fscanf(fin,"%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
		CORR * corr = new CORR[N];
		for( int i = 0 ; i < N ; i++ ) 
		{
			double B,E,wi;
			fscanf(fin,"%lf%lf%lf",&B,&E,&wi);
			corr[i].length = E-B;
			corr[i].w = wi;
		}
		sort( corr , corr+N , comp );
		double ans = 0;
		for( int i = 0 ; i < N ; i++ ) X -= corr[i].length;
		ans += min( t , X/R );
		t -= ans;
		X -= ans*R;
		ans += X/S;
		for( int i = 0 ; i < N ; i++ )
		{
			if( t > corr[i].length/(corr[i].w+R) ) 
			{
				t -= corr[i].length/(corr[i].w+R);
				ans +=  corr[i].length/(corr[i].w+R);
			}else{
				ans += t;
				corr[i].length -= (corr[i].w+R)*t;
				t = 0;
				ans += corr[i].length /(corr[i].w+S);
			}
		}
		
		fprintf(fout, "Case #%d: %lf\n",nt,ans );
	}


	return 0;
}

