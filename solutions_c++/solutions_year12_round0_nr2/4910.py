//Done by Grey Matter
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>
#include<list>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FOR(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;

ifstream fin("Bl.in");
ofstream fout("Bl.out");

int main(){
//ios_base::sync_with_stdio(false);
    int t;
    fin>>t;
    FORU(test,t){
        fout<<"Case #"<<test<<": ";
        int n,s,p;
        fin>>n>>s>>p;
        int baix=max(3*p-4,p);
        int alt=max(3*p-2,p);
        debug(alt);
        int num;
        int cont=0;
        int res=0;
        FOR(i,n){
            fin>>num;
            if(num>=alt) ++res;
            else if(num>=baix && cont<s) {++res; ++cont;}
        }
        fout<<res<<endl;
    }
    system("pause");
}
