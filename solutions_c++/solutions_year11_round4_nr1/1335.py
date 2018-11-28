#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <string>
#include <algorithm>
#include <iterator>
#include <functional>
#include <stdlib.h>
#include <math.h>

using namespace std;

#define repp(I, Start, End)		for(I = Start; I < End; ++I)
#define rep(I, Start, End)		for(I = Start ; I >= End; --I)

template<class T>
void splitstr(const string &s, vector<T> &out)
{
	istringstream in(s);
	out.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

typedef unsigned int uint;
typedef unsigned long long ull;

#define N	1001

ull pascal[N][N];

void calcpascal()
{
	pascal[0][0] = 1;
	int i, j;
	repp(i, 1, N)
	{
		pascal[i][0] = 1;
		pascal[i][i] = 1;
		repp(j, 1, i)
		{
			pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
		}
	}
}




int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("output.txt");
	string sl = "";
	bool bFirstLineRead = false;
	int iTestCaseCount = 0;
	int iTestCaseNo = 0;
	while(getline(ifs, sl))
	{
		istringstream ss(sl);
		if(!bFirstLineRead)
		{
			ss >> iTestCaseCount;
			bFirstLineRead = true;
			continue;
		}
		++iTestCaseNo;
		if(iTestCaseNo > iTestCaseCount)
			break;

		int x,s,r,t,n;
		ss>>x;
		ss>>s;
		ss>>r;
		ss>>t;
		ss>>n;

		vector<int> len(n);
		vector<int> speed(n);

		int i;
		int ll = 0;
		repp(i, 0, n)
		{
			getline(ifs, sl);
			istringstream ss2(sl);
			int b, e;
			ss2>>b;
			ss2>>e;
			len[i]=e-b;
			ll+=len[i];
			ss2>>speed[i];
		}

		long double tot = 0.0;
		long double rem = t;

		long double tt = ((long double)(x-ll)/r);
		if(tt>t)
		{
			tot=t + ((long double)(x-ll)-t*r)/s;
			tt=-10.0;
		}
		else
		{
			tot=tt;
			tt=t-tt;
		}
		bool fin=false;
		while(tt>0.000000001)
		{
			int minind=-1;
			int minspeed=0;
			repp(i, 0, n)
			{
				if((len[i]>0) && ((minind<0) || (speed[i]<minspeed)))
				{
					minind=i;
					minspeed=speed[i];
				}
			}
			if(minind<0)
			{
				fin=true;
				break;
			}
			int l2=len[minind];
			len[minind]=-1;
			long double t2 = (long double)l2/(r+speed[minind]);
			if(t2>tt)
			{
				tot+=(tt+((long double)l2-tt*(r+speed[minind]))/(s+speed[minind]));
				break;
			}
			else
			{
				t2=((long double)l2/(r+speed[minind]));
				tt-=t2;
				tot+=t2;
			}
		}

		repp(i, 0, n)
		{
			if(len[i]>0)
				tot+=((long double)len[i]/(s+speed[i]));
		}


		char zz[200];
		sprintf(zz, "%.12f", tot);
		ofs << "Case #" << iTestCaseNo << ": " << zz << endl;
	}
}