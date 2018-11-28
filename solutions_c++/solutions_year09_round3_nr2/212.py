#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<fstream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int K=T;
	//ofstream fout("out.txt");
	while(T--)
	{
		int N;
		double kx=0,ky=0,kz=0,vx=0,vy=0,vz=0;
		int a,b,c,d,e,f;
		cin>>N;
		for(int i=0;i<N;i++)
		{
			cin>>a>>b>>c>>d>>e>>f;
			kx+=a;
			ky+=b;
			kz+=c;
			vx+=d;
			vy+=e;
			vz+=f;
		}
		double s=(vx*vx+vy*vy+vz*vz);
		double t;
		if(s==0)
			t=0;
		else 
			t=(-1)*(kx*vx+ky*vy+kz*vz)/s;
		if(t<0)
			t=0;
		double dist=(kx/N+t*vx/N)*(kx/N+t*vx/N)+(ky/N+t*vy/N)*(ky/N+t*vy/N)+(kz/N+t*vz/N)*(kz/N+t*vz/N);
		dist=sqrt(dist);
		printf("Case #%d: %0.8f %0.8f\n",K-T,dist,t);
	}
	return 0;
}   

