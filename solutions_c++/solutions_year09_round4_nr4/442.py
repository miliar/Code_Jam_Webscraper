#include <iostream>
#include <math.h>
using namespace std;
#define EPS 1e-7
double X[50],Y[50],R[50];
double dist(int i,int j)
{
	return sqrt((X[i]-X[j])*(X[i]-X[j])+(Y[i]-Y[j])*(Y[i]-Y[j]));
}
bool incircle(int i,int j)
{
	return (dist(i,j)+R[i]<=R[j]+EPS);
}
int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D-small.out","w",stdout);
	double ret=0;
	int tt,ttt,i,N;
	cin>>tt;
	for(ttt=1;ttt<=tt;ttt++)
	{
		cin>>N;
		for(i=0;i<N;i++) cin>>X[i]>>Y[i]>>R[i];
		if (N==1) ret=R[0]; else
		if (N==2) ret=max(R[0],R[1]); else
		if (N==3)
		{
			if (incircle(0,1)||incircle(0,2)) ret=max(R[1],R[2]); else
			if (incircle(1,0)||incircle(1,2)) ret=max(R[0],R[2]); else
			if (incircle(2,0)||incircle(2,1)) ret=max(R[0],R[1]); else
			ret=min(min(max(R[2],(R[0]+R[1]+dist(0,1))/2.0),
			            max(R[1],(R[2]+R[0]+dist(2,0))/2.0)),
					max(R[0],(R[1]+R[2]+dist(1,2))/2.0));
		}
		cout<<"Case #"<<ttt<<": ";
		printf("%.6lf\n",ret);
	}
//	system("pause");
	return 0;
}
