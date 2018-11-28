#include <iostream>
#include <vector>
#include <fstream>

#define FR(i,a,b) for(int i=(a); i<(b); ++i)
#define FRO(i,n) FR(i,0,n)
#define FRE(i,a,b) for (int i=(a); i<=(b); ++i)
#define FROE(i,n) FRE(i,0,n)
#define FRS(i,a,v) FR(i,a,((v).size()))
#define FROS(i,v) FRO(i,((v).size()))

using namespace std;

int main(int argc, char** argv)
{
	fstream f(argv[1]);
	if (!f.is_open()) return 0;
	int T;
	f >> T;
//	cout <<"T="<<T<<endl;
	vector<double> re(T, 0);
	FRO(c, T)
	{
	//	cout <<"case: "<<c<<endl;
		int X, S, R, t, N;
		f >> X >> S >> R >> t >> N;
	//	cout <<X<<" "<<S<<" "<<R<<" "<<t<<" "<<N<<endl;
		vector<int> B(N), E(B), w(N);
		FRO(i, N)
		{
			f >> B[i] >> E[i] >> w[i];
	//		cout <<B[i]<<" "<<E[i]<<" "<<w[i]<<endl;
		}
		//find : time = f(X, S, R, t, N, B, E, w)
		//sort walkway by its speed w_i
		vector<int> dist(101, 0);
		FRO(i, N)
		{
			dist[w[i]] += (E[i]-B[i]);
		}
		dist[0] = X;
		FRS(i, 1, dist) dist[0] -= dist[i];
		vector<double> trun(dist.size(), 0);
		FROS(i, trun) 
		{
			trun[i] = (double) dist[i] / (R+i);
		}
		//distance gain
		double gain = t;
		FROS(i, trun)
		{
			if (trun[i]==0) continue;
			if (trun[i]<gain) 
			{
				gain -= trun[i];
				
			}
			else
			{
				trun[i] = gain;
				gain = 0;
			}
		}
		//time
		double tt = 0;
		FROS(i, dist)
		{
		//	tt += //(double)dist[i] / (double)(S+i);
			tt += trun[i] + (double)(dist[i]-trun[i]*(R+i))/
				(double)(S+i);
		}
		re[c] = tt;
	}

	ofstream g(argv[2]);
	if (!g.is_open()) return 0;
	g.precision(15);
	FROS(i, re)
	{
		g << "Case #"<<(i+1)<<": "<<re[i]<<endl;
	}
	g.close();
	return 0;
}