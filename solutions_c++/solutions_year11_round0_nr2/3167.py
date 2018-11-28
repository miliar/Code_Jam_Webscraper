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

int main(){
//ios_base::sync_with_stdio(false);
    ifstream fin("B-large.in");
    ofstream fout("Blargeout.txt");
    int cases;
    fin>>cases;
    FORU(cas,cases){
        cout<<cas<<endl;
        int combinations;
        fin>>combinations;
        map<string,char> COM;
        string s;
        FOR(i,combinations){
            fin>>s;
            COM[s.substr(0,2)]=s[2];
            swap(s[0],s[1]);
            COM[s.substr(0,2)]=s[2];
        }
        fin>>combinations;
        map<char,string> M;
        FOR(i,combinations) {
            fin>>s;
            M[s[0]]+=s[1];
            M[s[1]]+=s[0];
        }
        int n;
        fin>>n>>s;
        string result;
        result+=s[0];
        for(int i=1;i<s.size();i++){
            //bool b=false;
            if(result.size()>=2){
                for(int i=0;i<M[result[result.size()-1]].size();i++){
                    if(result.find(M[result[result.size()-1]][i])!=-1) {
                        result="";
                       // b=true;
                        break;
                    }
                }
            }
            if( result.size()){
                string a=result[result.size()-1]+s.substr(i,1);
                if(COM.find(a)!=COM.end()) {
                    result[result.size()-1]=COM[a];
                }
                else result+=s[i];
            }
            else result+=s[i];
           // debug(result);
        }
        if(result.size()>=2){
            for(int i=0;i<M[result[result.size()-1]].size();i++){
                if(result.find(M[result[result.size()-1]][i])!=-1) {
                    result="";
                   // b=true;
                    break;
                }
            }
        }
        fout<<"Case #"<<cas<<": [";
        FOR(lletra, result.size()) {
            if(lletra) fout<<", ";
            fout<<result[lletra];
        }
        fout<<"]"<<endl;
    }
    system("pause");
}
