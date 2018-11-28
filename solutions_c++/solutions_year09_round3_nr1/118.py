#include <cstdio>
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

int main()
{
	int t;
	int f[500];
	int val[500];
	char s[1000];
	scanf("%d",&t);
	REP(__,t)
	{
		long long res = 0LL;
		scanf("%s",s);
		_m(f,0);_m(val,-1);
		REP(i,strlen(s)) f[s[i]]++;
		int base = 0;
		REP(i,500) base+=(f[i]>0);
		if (base==1) base++;
		long long po = 1LL;
		REP(i,strlen(s)-1) po = po * base;
		val[s[0]] = 1;
		int idx=0;
		REP(i,strlen(s))
		{
			if (val[s[i]]==-1) 
			{
				val[s[i]]=idx++;
				if (idx==1) idx++;
			}
			res += val[s[i]] * po;
			//printf("%d %d %I64d\n",s[i],val[s[i]],po);
			po /= base;
		}
		fprintf(stderr,"Case #%d: %I64d\n",__+1,res);
		printf("Case #%d: %I64d\n",__+1,res);
	}
	return 0;	
}
