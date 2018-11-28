#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>


using namespace std;


long long int func(vector<long long int>& b)
{
	int m = b.size(); 
	if (m==1) return 0;
	vector<long long int> f(m);
	f[0]=0;
	f[1]= b[1]-b[0];
	for (long long int i=2; i<m; ++i)
	{
		f[i] = max(f[i-1]+b[i]-b[i-1], b[i]-b[i-1]);
	}
	
	vector<long long int> g(m);
	g[0] = 0;
	g[1] = b[1]-b[0];
	for (long long int i=2; i<m; ++i)
	{
		g[i] = max(g[i-1], f[i]);
	}
	return g[m-1];

}
int main(long long int argc, char** argv)
{
	ifstream f(argv[1]);
	long long int T;
	f >> T;
	vector<double> rr(T);
	for (long long int t=0; t<T; ++t)
	{
		long long int C, D;
		f >> C >> D;
		vector<long long int> a;
		a.reserve(100); //small data set
		for (long long int c=0; c<C; ++c)
		{
			long long int pos, num;
			f >> pos >> num;
			for (long long int i=0; i<num; ++i) a.push_back(pos);
		}
		//time
		vector<long long int> b(a.size());
		for (long long int i=0; i<a.size(); ++i)
		{
			b[i] = i*D-a[i];
		}
		//cout <<"case "<<T<<": bsize="<<b.size()<<endl;
		//n^2 time searching
		long long int time2=0;
		if(0)
		{
			for (long long int j=0; j<b.size(); ++j)
			{
				for (long long int i=j+1; i<b.size(); ++i)
				{
					long long int k = b[i]-b[j];
					if (time2<k)  time2 = k;
				}
			}
		}
		else
		{
			time2 = max(time2, func(b));
		}
		double time = time2*0.5;
		rr[t] = time;

	}
	f.close();
	ofstream g(argv[2]);
	g.precision(15);
	for (long long int i=0; i<T; ++i)
	{
		g <<"Case #"<<(i+1)<<": "<<rr[i]<<endl;
	}
	g.close();


}