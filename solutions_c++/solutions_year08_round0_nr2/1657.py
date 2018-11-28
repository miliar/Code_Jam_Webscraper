#include <iostream>

using namespace std;

struct timee
{
	int a,b,c,d;
};

bool ca(timee a,timee b)
{
	return a.c*60+a.d<b.c*60+b.d;
}

bool cb(timee a,timee b)
{
	return a.a*60+a.b<b.a*60+b.b;
}

int main()
{
	int n;
	cin>>n;
	for (int ii=0;ii<n;ii++)
	{
		int t,a,b;
		cin>>t>>a>>b;
		int p[200],q[200],r[200],s[200];
		int w[200],x[200],y[200],z[200];
		char c;
		for (int i=0;i<a;i++)
			cin>>p[i]>>c>>q[i]>>r[i]>>c>>s[i];
		for (int i=0;i<b;i++)
			cin>>w[i]>>c>>x[i]>>y[i]>>c>>z[i];
		timee u[200],v[200];
		for (int i=0;i<a;i++)
		{
			u[i].a=p[i];
			u[i].b=q[i];
			u[i].c=r[i];
			u[i].d=s[i];
		}
		for (int i=0;i<b;i++)
		{
			v[i].a=w[i];
			v[i].b=x[i];
			v[i].c=y[i];
			v[i].d=z[i];
		}
		sort(u,u+a,ca);
		sort(v,v+b,cb);
		//for (int i=0;i<a;i++)
			//cout<<u[i].a<<u[i].b<<u[i].c<<u[i].d<<endl;
		//for (int i=0;i<b;i++)
			//cout<<v[i].a<<v[i].b<<v[i].c<<v[i].d<<endl;
		int az=a,bz=b,cz=0;
		for (int i=0;i<a;i++)
			for (int j=cz;j<b;j++)
			{
				//cout<<i<<j<<endl;
				cz++;
				int tt=u[i].c*60+u[i].d+t;
				if (tt<=v[j].a*60+v[j].b)
				{
					j=1000;
					bz--;
				}
			}
		sort(u,u+a,cb);
		sort(v,v+b,ca);
		cz=0;
		for (int i=0;i<b;i++)
			for (int j=cz;j<a;j++)
			{
				//cout<<i<<j<<endl;
				//cout<<v[i].a<<v[i].b<<v[i].c<<v[i].d<<endl;
				//cout<<u[j].a<<u[j].b<<u[j].c<<u[j].d<<endl;
				cz++;
				int tt=v[i].c*60+v[i].d+t;
				//cout<<tt<<"df"<<u[j].a*60+u[j].b<<endl;
				if (tt<=u[j].a*60+u[j].b)
				{
					//cout<<"ddf";
					j=1000;
					az--;
				}
			}
		cout<<"Case #"<<ii+1<<": "<<az<<" "<<bz<<endl;
	}
	return 0;
}