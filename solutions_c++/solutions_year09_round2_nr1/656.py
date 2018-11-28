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

string feat[2000];
double val[2000];
bool isleaf[2000];
char fe[20][50];
int main()
{
	int t,n;
	char s[300],temp2[50];
	scanf("%d",&t);
	gets(s);
	REP(__,t)
	{
		_m(isleaf,1);
		REP(i,2000) feat[i]="";
		scanf("%d",&n);
		gets(s);
		string tree,temp;
		while (n--)
		{
			gets(s);
			temp = s;
			tree += temp;
		}
		int i=0;
		for(;i<tree.size();i++) if (tree[i]=='(') break;
		int idx = 1;
		for(i++;i<tree.size();i++)
		{
			if (tree[i]==' ') continue;
			if (tree[i]=='0' || tree[i]=='1' )
			{
				sscanf(tree.c_str()+i,"%lf",&val[idx]);
				//printf("Val %d = %lf\n",idx,val[idx]);
				while ((tree[i]>='0' && tree[i]<='9') || (tree[i]=='.')) i++;
				i--;
				continue;
			}
			if (tree[i]>='a' && tree[i]<='z')
			{
				sscanf(tree.c_str()+i,"%s",temp2);
				feat[idx] = temp2;
//				printf
				while (tree[i]>='a' && tree[i]<='z') i++;
				i--;
				continue;
			}
			if (tree[i]=='(' ) 
			{
				int j = i-1;
				while ( j > 0 && tree[j]==' ') j--;
				isleaf[idx] = false;
				if (tree[j]==')') idx=idx*2+1;
				else idx = 2 * idx;
			}
			if (tree[i]==')') idx>>=1;	
		} 
		
		//REP(i,17) printf("%d %s %lf\n",i,feat[i].c_str(),val[i]);
		int animal,nf;

		string fetemp;
		scanf("%d",&animal);
		fprintf(stderr,"Case #%d:\n",__+1);
		printf("Case #%d:\n",__+1);
		while (animal--)
		{
			double res = 1.0;
			scanf("%*s %d",&nf);
			int idx = 1;
			REP(i,nf) scanf("%s",fe[i]);
			while (1)
			{
				res *= val[idx];
				//printf("%d %lf lf\n",idx,val[idx],res);
				if (isleaf[idx])
				{
					break;	
				}
				bool ada=false;
				REP(i,nf) 
				{
					fetemp = fe[i];
					if (fetemp == feat[idx]) ada=true;
				}
				idx<<=1;
				if (!ada) idx++;
				
			}
			printf("%.7lf\n",res);
			fprintf(stderr,"%.7lf\n",res);
		}
	
	}
	return 0;	
}
