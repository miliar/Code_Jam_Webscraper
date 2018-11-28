// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

int num[200][200];

void process(int tt)
{
	int H,W,R;
	int a[20][2];

	cin>>H>>W>>R;
	for(int i=0;i<R;i++) cin>>a[i][0]>>a[i][1];
	memset(num,0,sizeof(num));
	num[1][1]=1;
	for(int i=1;i<=H;i++) for(int j=1;j<=W;j++)
	{
		int rr,cc;
		rr=i-1,cc=j-2;
		if(rr>=1&&rr<=H&&cc>=1&&cc<=W)
		{
			bool flag=false;
			for(int k=0;k<R;k++) if(a[k][0]==rr&&a[k][1]==cc) {flag=true;break;}
			if(!flag) num[i][j]=(num[i][j]+num[rr][cc])%10007;
		}
		rr=i-2,cc=j-1;
		if(rr>=1&&rr<=H&&cc>=1&&cc<=W)
		{
			bool flag=false;
			for(int k=0;k<R;k++) if(a[k][0]==rr&&a[k][1]==cc) {flag=true;break;}
			if(!flag) num[i][j]=(num[i][j]+num[rr][cc])%10007;
		}
	}
	
	cout<<"Case #"<<tt<<": "<<num[H][W]<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}