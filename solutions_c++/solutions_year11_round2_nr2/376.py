#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

double X[1000000];
double Y[1000000];
int n=0;
int D;
bool posible(double d)
{
	//cout<<d<<"sad"<<endl;
	Y[0]=X[0]-d;
	for(int i=1;i<n;i++)
	{
		//cout<<Y[i-1]<<endl;
		if(fabs(X[i]-Y[i-1])<D)
		{
			double f=D+Y[i-1]-X[i];
			if(f>d+0.00000000000000001)return 0;
			Y[i]=X[i]+f;
			continue;
		}
		if(X[i]<Y[i-1])return 0;
		double f=-D-Y[i-1]+X[i];
		if(f>d+0.0000000000000000000001)f=d;
		Y[i]=X[i]-f;
	}
	return 1;
}
int main (int argc, char * const argv[]) {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{	
		int C;
		cin>>C>>D;
		n=0;
		for(int i=0;i<C;i++)
		{
			int P,V;
			cin>>P>>V;
			for(int j=0;j<V;j++)X[n++]=P;
		}
		sort(X,X+n);
		double ini=0;
		double fin=1000000;
		
		double med;
		for(int busqueda=0;busqueda<100;busqueda++)
		{
			med=(ini+fin)*0.5;
			if(posible(med))fin=med;
			else
			ini=med;
		}
		cout<<"Case #"<<c<<": ";
		cout<<med<<endl;
				
	}
    return 0;
}

