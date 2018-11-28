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

ifstream fin("A.in");
ofstream fout("A.out");

int main(){
//ios_base::sync_with_stdio(false);
    int cases;
    fin>>cases;
    string s;
    getline(fin,s);
//    string abecedari="abcdefghijklmnopqrstuvwxyz";
    string abecedari="yhesocvxduiglbkrztnwjpfmaq";
    for(int cas=1;cas<=cases;++cas){
        fout<<"Case #"<<cas<<": ";
        getline(fin,s);
        FOR(i,s.size()) {
            if(s[i]>='a' && s[i]<='z') fout<<abecedari[s[i]-'a'];
            else fout<<s[i];
        }
        fout<<endl;
    }
    system("pause");
}
