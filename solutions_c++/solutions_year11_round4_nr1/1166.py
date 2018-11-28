#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef struct{
	double b,e,w;
}runway;

bool compare(runway a, runway b)
{
	return a.w<b.w;
}

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("ouput.txt");
	fin >> T;
	for(int ca=0;ca<T;ca++)
	{
		double x,s,r,n;
		double t;
		fin >> x >> s >> r >> t >> n;
		vector <runway> run;
		double dis=0;
		for(int i=0;i<n;i++)
		{
			runway newr;
			fin >> newr.b >> newr.e >> newr.w;
			dis+=newr.e-newr.b;
			run.push_back(newr);
		}
		sort(run.begin(),run.end(),compare);
		double time=0;
		double disleft=x-dis;
		if (t!=0)
		{
			if (disleft*1.0/r<=t)
			{
				time+=disleft*1.0/r;
				t-=disleft*1.0/r;
				disleft=0;
			}
			else
			{
				disleft-=t*r;
				time+=t;
				time+=disleft*1.0/s;
				t=0;
			}
		}
		for(int i=0;i<run.size();i++)
		{
			double diff=run[i].e-run[i].b;
			dis+=diff;
			if (t!=0)
			{
				if (diff*1.0/(r+run[i].w)<=t)
				{
					t-=diff*1.0/(r+run[i].w);
					time+=diff*1.0/(r+run[i].w);
				}
				else
				{
					diff-=t*(r+run[i].w);
					time+=t;
					time+=diff*1.0/(s+run[i].w);
					t=0;
				}
			}
			else
			{
				time+=diff*1.0/(s+run[i].w);
			}
		}

		fout << "Case #" << ca+1 << ": ";
		fout << fixed << setprecision(9) << time << "\n";
	}
}