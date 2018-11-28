#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#define input freopen("input.txt", "r", stdin)
#define output freopen("output.txt", "w", stdout)
#define pb push_back
#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for(int i = (a), _b = (b); i <= _b; i++)
using namespace std;

const int inf = 0x7FFFFFFF;
const double eps = 1e-9L;
const double pi = acos(-1.0);
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<string,int> psi;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef long long ll;
typedef long double ld;

using namespace std;
 
    int main()
    {
    	int n;
    	cin>>n;
    	for (int z = 1; z <= n; z += 1)
    	{
       	string str[4];
    		for (int i = 0; i < 4; i += 1)
    		{
    			cin>>str[i];
    		}
    		bool x=false,o=false,space=false;
    		
    		for (int i = 0; i < 4; i += 1)
    		{
    			
    			if((str[i][0]=='X' || str[i][0]=='T') && (str[i][1]=='X' || str[i][1]=='T') && (str[i][2]=='X' || str[i][2]=='T') && (str[i][3]=='X' || str[i][3]=='T')) x=true;
    			if((str[i][0]=='O' || str[i][0]=='T') && (str[i][1]=='O' || str[i][1]=='T') && (str[i][2]=='O' || str[i][2]=='T') && (str[i][3]=='O' || str[i][3]=='T')) o=true;
    			if(str[i][0]=='.' || str[i][1]=='.' || str[i][2]=='.' || str[i][3]=='.') space=true;
    		}
    		
    		for (int i = 0; i < 4; i += 1)
    		{
    			if((str[0][i]=='X' || str[0][i]=='T') && (str[1][i]=='X' || str[1][i]=='T') && (str[2][i]=='X' || str[2][i]=='T') && (str[3][i]=='X' || str[3][i]=='T')) x=true;
    			if((str[0][i]=='O' || str[0][i]=='T') && (str[1][i]=='O' || str[1][i]=='T') && (str[2][i]=='O' || str[2][i]=='T') && (str[3][i]=='O' || str[3][i]=='T')) o=true;
    		}
    		
    			if((str[0][0]=='X' || str[0][0]=='T') && (str[1][1]=='X' || str[1][1]=='T') && (str[2][2]=='X' || str[2][2]=='T') && (str[3][3]=='X' || str[3][3]=='T')) x=true;
    			if((str[0][0]=='O' || str[0][0]=='T') && (str[1][1]=='O' || str[1][1]=='T') && (str[2][2]=='O' || str[2][2]=='T') && (str[3][3]=='O' || str[3][3]=='T')) o=true;
    			
    			if((str[0][3]=='X' || str[0][3]=='T') && (str[1][2]=='X' || str[1][2]=='T') && (str[2][1]=='X' || str[2][1]=='T') && (str[3][0]=='X' || str[3][0]=='T')) x=true;
    			if((str[0][3]=='O' || str[0][3]=='T') && (str[1][2]=='O' || str[1][2]=='T') && (str[2][1]=='O' || str[2][1]=='T') && (str[3][0]=='O' || str[3][0]=='T')) o=true;
    		
    		cout<<"Case #"<<z;
    		if(x) cout<<": X won\n";
    		else if(o) cout<<": O won\n";
    		else if(space) cout<<": Game has not completed\n";
    		else cout<<": Draw\n";
    	}
       return 0;
    }
