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
	int t,n;
	char s[100];
	char s2[100];
	scanf("%d",&t);
	REP(__,t)
	{
		scanf("%s",s2);
		string vv = s2,nn=s2;
		//sort(vv.begin(),vv.end());
		bool found = false;
		string res;
		if (next_permutation(vv.begin(),vv.end()))
		{
			if (vv > nn)
			{
				found = 1;
				res = vv;	
			}
		}
		
		if (!found)
		{
			sort(vv.begin(),vv.end());
			REP(i,vv.size()) if (vv[i]!='0') 
			{
				swap(vv[i],vv[0]);
				break;	
			}
			vv.insert(1,"0");
			res = vv;
		}
		
		fprintf(stderr,"Case #%d: %s\n",__+1,res.c_str());
		printf("Case #%d: %s\n",__+1,res.c_str());
	}
	return 0;	
}
