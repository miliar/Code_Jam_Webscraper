#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int main()
{
	int T;
	cin >> T;
	int index=0;
	while(index<T)
	{
		string s;
		cin >> s;
		int k=s.sz;

		bool ok=false;
		while(k>1)
		{
			char c=s[k-2];
			int p=k-1;
			bool found=false;
			char get='9'+1;
			int pos=-1;
			while(p<s.sz)
			{
				if(s[p]>c) { found=true; if(s[p]<get) { get=s[p]; pos=p; } }
				p++;
			}
			if(found)
			{
				s[k-2]=get; s[pos]=c;
				sort(s.begin()+k-1, s.end());
				ok=true;
				break;
			}
			else
				k--;
		}
		if(ok==false)
		{
			sort(s.begin(), s.end());
			char tmp;
			REP(j,s.sz) { if(s[j]!='0') {tmp=s[j]; s=s.substr(0,j)+s.substr(j+1);break;}}
			s=string(1,tmp)+"0"+s;
		}
		cout << "Case #" << ++index <<": "  << s << endl;
	}
	return 0;

}
