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


typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef long long ll;

int maxim=-1;

void fun(int pos,int punt, int a, int b, VI &v){
    if(pos==v.size()){
        if(a && b && a==b) maxim=max(maxim,punt);
        return;
    }
    fun(pos+1,punt+v[pos],a^v[pos],b,v);
    fun(pos+1,punt,a,b^v[pos],v);
}

int main(){
//ios_base::sync_with_stdio(false);
    ifstream fin("C-small-attempt0.in");
    ofstream fout("Csmallout.txt");
    int casos;
    fin>>casos;
    FORU(cas,casos){
        maxim=-1;
        int n;
        fin>>n;
        VI v(n);
        FOR(i,n) fin>>v[i];
        fun(0,0,0,0,v);
        fout<<"Case #"<<cas<<": ";
        if(maxim==-1) fout<<"NO"<<endl;
        else fout<<maxim<<endl;
    }
    system("pause");
}
