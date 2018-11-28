#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
using namespace std;

int n,i;
double x[100],y[100],r[100];
double R,aux;

double dist(int a,int b)
{
	double X = x[a]-x[b];
	double Y = y[a]-y[b];
	return sqrt(X*X+Y*Y);
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,I;
	cin>>T;
	for(I=1;I<=T;++I)
	{
		cin>>n;
		for(i=1;i<=n;++i)
			cin>>x[i]>>y[i]>>r[i];
		if(n==1)
			R = 2*r[1];
		if(n==2)
			R = max(2*r[1],2*r[2]);
		if(n==3)
		{
			R = 10000.0;
			aux = max(r[1],max(2*r[2],max(2*r[3],r[2]+r[3]+dist(2,3))));
			if(aux<R) R = aux;
			aux = max(r[2],max(2*r[1],max(2*r[3],r[1]+r[3]+dist(1,3))));
			if(aux<R) R = aux;
			aux = max(r[3],max(2*r[2],max(2*r[1],r[2]+r[1]+dist(2,1))));
			if(aux<R) R = aux;
		}
		R /= 2.0;
		cout<<"Case #"<<I<<": "<<R<<endl;
	}
	return 0;
}
