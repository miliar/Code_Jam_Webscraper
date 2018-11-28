#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))
#define INF 1000000000

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

inline int tonumber(int number,int base)
{
	int res = 0;
	do
	{
		res += (number % base) * (number%base);
		number /= base;
	}while (number);
	return res;	
}

map<int,bool> happyNum;
set<int> vis;
bool happy(int number,int base)
{
	int temp = tonumber(number,base);
	if (temp == 1) return 1;
	if (vis.count(temp)) happyNum[temp] = 0;
	if (happyNum.count(temp)==0)
	{
		vis.insert(temp);
		int x = happy(temp,base);
		happyNum[temp] = x;
		vis.erase(temp);
	}
	return happyNum[temp];
}

int main()
{
	int t;
	char s[200];
	//printf("%d %d\n",happy(3,2),happy(3,3));
	scanf("%d",&t);
	gets(s);
//	printf("%d %d\n",happy(3,2),happy(3,3));
	REP(__,t)
	{
		gets(s);
		vector<int> base = splitInt(s);
		int res = 1;
		bool happyAll=false;
		while (!happyAll)
		{
			res++;
			happyAll=true;
			REP(i,base.size()) 
			{
				happyNum.clear();vis.clear();
//				printf("%d %d %d\n",res,base[i],happy(res,base[i]));
				//if (res % 1000000 == 0) printf("%d\n",res);
				if (!happy(res,base[i])) {happyAll = false; break;}
			}
		}
		printf("Case #%d: %d\n",__+1,res);	
	}
	return 0;	
}
