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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>

using namespace std;

const double PI = acos(-1.0);
#define FOR(a,b) for(int i = a; i< b; ++i)
#define SORT(a,b) sort(a.begin(),a.end(),b)
#define MEMS(a,b) memset(a,b,sizeof(a))
template<class T>
inline T gcd(T a , T b) { if(a == 0 || b == 0 || a == b) return max(a,b); return a>b?gcd(a%b,b) : gcd(a,b%a);}
string intToStr(int n) { char p[15];sprintf(p,"%d",n);return string(p);}
int strToInt(string s) { istringstream sin(s); int r; sin >> r; return r;} 

int CA[4] = { 1, 2, 4, 8};

vector<vector<string> > pro;

void ready()
{
	vector<string> p;
	p.push_back("0"); p.push_back("1");
	pro.push_back(p);
	p.clear();
	p.push_back("00"); p.push_back("01"), p.push_back("10"), p.push_back("11");
	pro.push_back(p);
	p.clear();
	p.push_back("000"); p.push_back("001"), p.push_back("010"), p.push_back("011");
	p.push_back("100"); p.push_back("101"), p.push_back("110"), p.push_back("111");
	pro.push_back(p);
}

int main()
{
	int T, A, B;
	ready();
	cin >> T;
	for(int t = 1; t<= T; ++t)
	{
		cin >> A >> B;
		double *pa = new double[A];
		for(int i = 0;i< A; ++i) cin >> pa[i];
		vector<string> Pby = pro[A-1];
		vector<pair<double,int> > probly;
		for(int i = 0; i< Pby.size(); ++i)
		{
			double pp = 1;
			double bkc = 0;
			for(int j = 0; j< Pby[i].length(); ++j)
			{
				if(Pby[i][j] == '1')
				{
					pp *= pa[j];
				}
				else pp*= (1.0-pa[j]);
			}
			for(int j = Pby[i].length()-1; j>= 0; j--)
			{
				if(Pby[i][j] == '1') bkc ++;
				else break;
			}
			probly.push_back(make_pair(pp,bkc));
		}
		double ret_ex = 10000*1000;
		int n = Pby.size();
		// keep typing
		double ex = 0;
		for(int i = 0; i< n; ++i)
		{
			if(probly[i].second == A)
				ex += probly[i].first*(B-A+1);
			else ex += probly[i].first*(2*B+2-A);
		}
		ret_ex = min(ex,ret_ex);
		// press k bs
		for(int i = 1; i<= A; ++i)
		{// 
			ex = 0;
			for(int j = 0; j< probly.size(); ++j)
			{
				int correct = 0;
				for(int k = 0; k< A-i; ++k)
				{
					if(Pby[j][k] == '1') correct ++;
					else break;
				}
				if(correct == A-i) {
					ex += probly[j].first*(B+1-(A-i)+i);
				}
				else 
				{
					ex += probly[j].first*(B+1-(A-i)+i+B+1);
				}
			}
			ret_ex = min(ex,ret_ex);
		}
		// enter now
		ret_ex = min(B+2.0,ret_ex);

		printf("Case #%d: %.6lf\n",t,ret_ex);
		//cout << "Case #1: " << ret_ex << endl;
	}
	return 0;
}