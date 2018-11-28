#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

int t,c,d,n;
bool mas[300][300];
string s,res;
char val[300][300];

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
//DEBUG = true;
#endif
cin>>t;
fw(test,1,t)
	{
	res = "";
	fr(i,300)
	fr(j,300)
		{
		val[i][j] = 'a';
		mas[i][j] = false;
		}
	cin>>c;
	fr(i,c)
		{
		cin>>s;
		val[s[0]][s[1]] = val[s[1]][s[0]] = s[2];
		}
	cin>>d;
	fr(i,d)
		{
		cin>>s;
		mas[s[0]][s[1]] = mas[s[1]][s[0]] = true;
		}
	cin>>n;
	cin>>s;
	dbg(s);
	fr(i,n)
		{
		dbg(res);
		if(res.length()>0&&val[res[res.length()-1]][s[i]]!='a')
			{
			char combined = val[res[res.length()-1]][s[i]];
			res = res.substr(0,res.length()-1);
			res.PB(combined);
			dout("Combined to: ");
			dbg(combined);
			}
		else 
			{
			bool cleared = false;
			fw(j,'A','Z')	
				if(mas[j][s[i]]&&res.find(j)!=-1)
					{
					if(DEBUG) cout<<"Cleared by: "<<s[i]<<" "<<((char) j)<<endl;
					res.clear();
					cleared = true;
					break;
					}
			if(!cleared) res.PB(s[i]);
			}
		}
	
	dbg(res);
	printf("Case #%d: [", test);
	fr(i,res.length())
		{
		printf("%c", res[i]);
		if(i<res.length()-1) printf(", ");
		}
	printf("]");
	if(test<=t) printf("\n");
	}
return 0;
}
