#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

double pi=2*acos(0.0);

int main()
{
	FILE* fin=fopen ("in.txt","r");
	FILE* fout=fopen("out.txt","w");

	int n=0;
	fscanf(fin,"%d", &n);
	for (int j=0;j<n;++j)
	{
		vector<int> k(6,0);
		vector<vector<int>>coord;
		int T=0;
		fscanf(fin,"%d",&T);
		for(int i=0;i<T;++i)
		{
			coord.push_back(k);
//			int x,y,z,vx,vy,vz;
			fscanf(fin,"%d%d%d%d%d%d", &coord[i][0], &coord[i][1], &coord[i][2], &coord[i][3], &coord[i][4], &coord[i][5]);
		}
		double a = 0.0,b=0.0,c=0.0;
		double x0=0.0,y0=0.0,z0=0.0;
		vector<double>c0(3,0.0);
		for(int q=0;q<3;++q)
		{
			for(int i=0;i<T;++i) c0[q]+=coord[i][q];
			c0[q]/=(double)T;
		}

		for (int q=0;q<3;++q)
		{
			double a1=0.0,b1=0.0,c1=0.0;
			for(int i=0;i<T;++i)
			{
				a1+=(double)coord[i][q+3];
				b1+=(double)coord[i][q+3];
			}
			a1/=(double)T;
			b1/=(double)T;
			a+=a1*a1;
			b+=b1*c0[q]*(double)2;
			c+=c0[q]*c0[q];
		}
		double t=0.0;
		if(fabs(a)<1e-5) 
		{
			if(fabs(c)<1e-5) t=0;
			else t=-b/c;
		}
		else
			t = -b/(double)2/a;

		double d = a*t*t+b*t+c;

		if(d<0.0){
		d=0.0;
		t = (-b-sqrt(b*b-4*a*c))/2/a;
		if(t<0.0) t = (-b+sqrt(b*b-4*a*c))/2/a;
		}

		if(t<0.0){t=0.0;d=c;}
		t=fabs(t);


		fprintf(fout, "Case #%d: %lf %lf\n", j+1, sqrt(d), t);
		cout << a <<" "<<b<<" "<<c<<"\n";
	}
	fclose(fin);fclose(fout);
	return 0;
}