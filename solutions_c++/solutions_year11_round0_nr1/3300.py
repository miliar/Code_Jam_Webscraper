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
    ifstream fin("A-large.in");
    ofstream fout("Aoutlarge.txt");
    int casos;
    fin>>casos;
    FORU(cas,casos){
        int po=1,pb=1,to=0,tb=0;
        int ordres,num;
        string robot;
        fin>>ordres;
        FOR(i,ordres){
            fin>>robot>>num;
            if(robot=="O"){
                if(to>tb){ //L'últim ha estat el Orange
                    to=to+abs(num-po)+1;
                }
                else{ //Ultim ha estat el Blau
                    to=max(to+abs(num-po),tb)+1;
                }
                po=num;
            }
            else{
                if(to<tb){ //Ultim blau
                    tb=tb+abs(num-pb)+1;
                }
                else{ //Ultim taronja
                    tb=max(tb+abs(num-pb),to)+1;
                }
                pb=num;
            }
        }
        fout<<"Case #"<<cas<<": "<<max(to,tb)<<endl;
    }
    system("pause");
}
