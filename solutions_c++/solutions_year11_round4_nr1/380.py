#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("a.in");
ofstream fout("a.out");

int T;
int X;
int S;
int R;
int t;
int N;

int B[1024];
int E[1024];
int W[1024];
int D[1024];
int main()
{
	
	fin>>T;
	for(int c=1;c<=T;c++)
	{
		fin>>X>>S>>R>>t>>N;

		int total = 0;
		for(int i=1;i<=N;i++)
		{
			fin>>B[i]>>E[i]>>W[i];
			D[i] = E[i]-B[i];
			total+=D[i];
		}
		W[0] = 0;
		D[0] = X-total;

		for(int i=1;i<=N;i++)
			for(int j=i+1;j<=N;j++)
			{
				if(W[i]>W[j])
				{
					int tmp=W[j];W[j] = W[i];W[i] = tmp;
					tmp=D[j];D[j] = D[i];D[i] = tmp;		

				}
			}

		double res = 0.0;
		double remainT = t;
		for(int i=0;i<=N;i++)
		{
			if(D[i]<=0) continue;
			double require = (double)D[i]/(W[i]+R);
			if(remainT >= require)
			{
				remainT -= require;
				res += require;
			}
			else
			{
				
				res += remainT;
				res +=((double)D[i] - remainT*(W[i]+R))/(W[i]+S);
				remainT=0;

			}
		}
		//cout<<"Case #"<<c<<": "<<res<<endl;
		//fout<<"Case #"<<c<<": "<<res<<endl;


	fout.setf(ios::fixed,ios::floatfield);
		cout<<"Case #"<<c<<": "<<setprecision(10)<<res<<endl;
		fout<<"Case #"<<c<<": "<<setprecision(10)<<res<<endl;
		
	}
	return 0;
}
