#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cstring>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORI(i,a,n) for(int i=(a);i<(n);i++)
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;
set<vector<string> > visited;
bool valid(const vector<string>& x)
{

    for(int i=0;i<sz(x);i++)
    {
	for(int j=i+1;j<sz(x);j++) if(x[i][j]=='1') 
	{
	    return false;
	}
    }
 
    return true;
}


int main()
{
    int t;
    cin>>t;
    int casenum=0;
    while(t--)
    {	casenum++;
	visited.clear();
	int n;
	cin>>n;
	string line;
	vector<string> mat;
	for(int i=0;i<n;i++) cin>>line,	mat.push_back(line);
	int rv=0;
	
	for(int i=0;i<n;i++)
	{
	    bool ok=true;
	    for(int j=i+1;j<n;j++) if(mat[i][j]=='1') ok=false;
	    if(ok) continue;
	    for(int l=i+1;l<n;l++)
	    {
		ok=true;
		for(int j=i+1;j<n;j++) if(mat[l][j]=='1') ok=false;
		if(ok)
		{
		    for(int k=l;k>i;k--)
		    {
			rv++;
			swap(mat[k],mat[k-1]);
		    }
		    break;
		}
	    }
	}

	cout<<"Case #"<<casenum<<": "<<rv<<endl;

    }

    return 0;
}
