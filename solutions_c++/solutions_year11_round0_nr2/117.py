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
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("ed.in");
ofstream fout("ed.out");

int N;
vector<string> vc,vd;

bool oppo[256][256];
int C,D,L;
char ch[111];
string s;
int len;


void process()
{
	if(len<=1) return;
	string s1="";
	s1 += ch[len-1];
	s1 += ch[len-2];
	string s2="";
	s2+= ch[len-2];
	s2 += ch[len-1];
	
	for(int i=0;i<C;i++)
	{
		string t = vc[i].substr(0,2);
		if(t==s1 || t==s2)
		{
			len--;
			ch[len-1] = vc[i][2];
			process();
			return;
		}
	}
	int ta = (int)ch[len-1];
	for(int i=0;i<len-1;i++)
	{
		int tb = (int)ch[i];
		if(oppo[ta][tb])
		{
			len = 0;
			return;
		}
	}

}

int main()
{
	fin>>N;
	for(int c=0;c<N;c++)
	{
		vc.clear();
		vd.clear();
		memset(oppo,false,sizeof(oppo));
		

		fin>>C;
		for(int i=0;i<C;i++)
		{
			fin>>s;
			vc.push_back(s);
		}
		fin>>D;
		for(int i=0;i<D;i++)
		{
			fin>>s;
			int ta = (int)s[0];
			int tb = (int)s[1];
			oppo[ta][tb] = oppo[tb][ta] = true;
			vd.push_back(s);

		}
		fin>>L;
		fin>>s;

		len = 0;
		for(int i=0;i<L;i++)
		{
			ch[len++] = s[i];
			process();
		}

		string res = "[";
		if(len>0) res += ch[0];
		for(int i=1;i<len;i++)
		{
			res += ", ";
			res += ch[i];
		}
		res += "]";

		

		cout<<"Case #"<<c+1<<": "<<res<<endl;
		fout<<"Case #"<<c+1<<": "<<res<<endl;

	
	}
	return 0;
}
