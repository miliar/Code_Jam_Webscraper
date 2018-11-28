#include<stdlib.h>
#include<iostream>
#include<sstream>
#include<math.h>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<set>
#include<map>
#include<numeric>
#include<algorithm>
#include<stdio.h>

using namespace std;

#define for0(i,n) for((i)=0;(i)<(n);(i)++)
#define for1(i,n) for((i)=1;(i)<=(n);(i)++)
#define min2(a,b) (a)<(b)?(a):(b)
#define min3(a,b,c) ((a)<(b)?(a):(b))<(c)?((a)<(b)?(a):(b)):(c)
#define min4(a,b,c,d) min3(a,b,c)<d?min3(a,b,c):d
#define max2(a,b) (a)>(b)?(a):(b)
#define max3(a,b,c) ((a)>(b)?(a):(b))>(c)?((a)>(b)?(a):(b)):(c)
#define max4(a,b,c,d) max3(a,b,c)>d?max3(a,b,c):d

#define swap(a,b,t) t=a;a=b;b=t;

#define inf 1000000000
#define iss istringstream

#define vi vector<int>
#define vs vector<string>
#define vd vector<double>
#define ssc sscanf
#define sp sprintf
#define pb push_back
#define sortv(x) sort(x.begin(),x.end())

#define cname c
#define fname f
#define lvars  int l1=0,l2=0,l3=0,l4=0
#define tvars  int t1=0,t2=0,t3=0,t4=0

#define dec(c) (((c)>='0'&&(c)<=9))?((c)-'0'):(((c)>='a'&&(c)<='f')?(c)-'a'+10:(c)-'A'+10)

int n,x[1000],y[1000],z[1000],xv[1000],yv[1000],zv[1000];
int main()
{
	int t,t1=1,i,j;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for0(i,n)
		{
			cin>>x[i]>>y[i]>>z[i]>>xv[i]>>yv[i]>>zv[i];
		}

		double dis = 1000000000.0, tm;
		double sx=0.0,sy=0.0,sz=0.0,sxv=0.0,syv=0.0,szv=0.0,tdis,c1,c2,c3,c4,c5,c6;
		for(j=0;j<n;j++)
		{
			sxv+=xv[j];syv+=yv[j];szv+=zv[j];
			sx += x[j];sy += y[j]; sz += z[j];
		}

		c1 = 2.0*(sxv*sx+syv*sy+szv*sz);
		c2 = 2.0 * sxv*sxv;
		c3 = 2.0 * syv*syv;
		c4 = 2.0 * szv*szv;
		c5 = c2 + c3 + c4;
		tm = 0.0;
		if(c5 != 0.0)
			tm = -1.0 * (c1)/(c5);
		if(tm <= 0.0)tm = 0.0;

		double dx = (sx + tm*sxv)/(double)(n),dy = (sy + tm*syv)/(double)(n),dz = (sz + tm*szv)/(double)(n);

		dis = sqrt(dx*dx + dy*dy + dz*dz);
		
		printf("Case #%d: %lf %lf\n",t1,dis,tm);
		t1++;
	}
	return 0;
}