#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>
using namespace std;

struct rpi
{
	double wp;
	double op;
	double oop;
	int a,b;
	rpi() : wp(0.0), op(0.0), oop(0.0){}
};

int main()
{
	string line;
	int T;
	getline(cin,line); T = atoi(line.c_str());
	for(int tcase=1; tcase <= T; ++tcase)
	{
		int num_t;
		getline(cin,line); num_t = atoi(line.c_str());
		int record[102][102]= { {0,}, };
		for(int i=0; i < num_t; ++i)
		{
			getline(cin,line);
			for(size_t j=0; j < line.size(); ++j)
			{
				if( line[j]=='0' )
					record[i][j]=-1;
				else if( line[j]=='1' )
					record[i][j]=1;
			}
		}
		vector<rpi> r(num_t, rpi());
		for(int i=0; i < num_t; ++i)
		{
			int a=0,b=0;
			for(int j=0; j < num_t; ++j)
			{
				if(i==j) continue;
				if(record[i][j]) ++b;
				if(record[i][j]==1) ++a;
			}
			r[i].a=a;
			r[i].b=b;
			r[i].wp = (double)a/b;
		}
		for(int i=0; i < num_t; ++i)
		{
			double _a=0.0;
			for(int j=0; j < num_t; ++j)
			{
				if(i==j)continue;
				if(record[i][j]==1)
				{
					double tmp = (double)r[j].a/(double)(r[j].b-1);
					_a += tmp;
				}
				else if( record[i][j]==-1 )
				{
					double tmp = (double)(r[j].a-1)/(double)(r[j].b-1);
					_a += tmp;
				}
			}
			r[i].op = _a/r[i].b;
		}
		for(int i=0; i < num_t; ++i)
		{
			double _a=0.0;
			for(int j=0; j < num_t; ++j)
			{
				if(i==j) continue;
				if(record[i][j])
					_a += r[j].op;
			}
			r[i].oop = _a/r[i].b;
		}

		cout << "Case #" << tcase << ":" <<endl;
		for(int i=0; i < num_t; ++i)
		{
			double a = 0.25*r[i].wp+0.5*r[i].op+0.25*r[i].oop;
			cout<< setprecision(6) << a << endl;
		}

	}
	return 0;
}
