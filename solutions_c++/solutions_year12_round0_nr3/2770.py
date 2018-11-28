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

bool recycled(string a, string b)
{
	for(int i = 1; i<= a.size()-1; ++i)
	{
		string ta = a.substr(i,a.size()-i) + a.substr(0,i);
		if(ta == b) return true;
	}
	return false;
}
bool BM[2000001];

int main()
{
	/*string tt = "00484";
	int t = strToInt(tt);
	cout << t << endl;*/
	int A,B,T;
	cin >> T;
	int cnt = 0;
	for(int t = 1; t<= T; ++t)
	{
		cin >> A >> B;
		cnt = 0;
		memset(BM,0,sizeof(BM));
		//map<pair<int,int>, int> MP;
		for(int i = A; i< B; ++i)
		{
			vector<int> ans;
			string ia = intToStr(i);
			for(int k = 1; k<= ia.length()-1; ++k)
			{
				string ib = ia.substr(k,ia.size()-k) + ia.substr(0,k);
				if(ib[0] == '0') continue;
				int j = strToInt(ib);
				if(j> i && j<= B && (BM[j]==0))
				{
					ans.push_back(j);
					BM[j] = true;
					cnt++;
				}
			}
			for(int i = 0; i< ans.size(); ++i) BM[ans[i]] = 0;
		}
		
		cout << "Case #" << t << ": " << cnt << endl;
 
	}
	return 0;
}