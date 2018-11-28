#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<complex>
#include<sstream>
#include<map>
#include<set>
#define DEBUG(x) cout<<"line"<<__LINE__<<":"<<#x" == "<<x<<endl
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
#define INF 1000000
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<int,int> P;

int T;
///////////////////////////////////////////////////////////////
int main(){
    cin>>T;
    int A,B;
    for(int k = 0 ;k< T;k++){
        A=0;
        B=0;
        cin>>A>>B;
        int C = (int)log10(A);
        int ans = 0;
        for(int i =A;i<=B;i++){
            vector<int> te;
            for(int j =1;j<=C;j++){
                
                int a = (int)pow((double)10,j);
                int temp = i%(a);
                int temp1 = i/(a);
                int b = (int)pow((double)10,C-j+1);
                int temp2= temp*(b)+temp1;
                int flag = 1;
                te.push_back(temp2);
                for(int x = 0;x<(int)te.size()-1;x++){
                    if(te[x]==temp2) flag =0;
                      }
                // DEBUG(i);
                // DEBUG(temp);
                // DEBUG(temp1);
                // DEBUG(temp2);
                if(temp2>i&&temp2<=B&&flag){
//                    DEBUG("INC");
                    ans++;
                }
            }
        }
        cout<<"Case #"<<k+1<<": "<<ans<<endl;

    }    
    return 0;
  
}

