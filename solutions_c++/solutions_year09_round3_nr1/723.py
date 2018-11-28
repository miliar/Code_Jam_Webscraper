#include<iostream>
#include<cmath>
#include<string>
#include<sstream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<numeric>
#include<iostream>
#include<fstream>

using namespace std;

#define MAX INT_MAX
#define EPS (1e-10)

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define K(a) ((a)*(a))

#define REP(i,v) for(typeof((v).begin()) i = (v).begin(); i!= (v).end(); ++i )
#define FOR(i,v) for(int i=0; i<v.size(); ++i)

typedef pair<int,int> pii; 





int main(){
    ifstream input;
    input.open("a.in");
    ofstream output;
    output.open("a.out");
  
    int T;     
    input>>T;
    
    for(int xxx=1; xxx<=T; xxx++){
            output<<"Case #"<<xxx<<": ";
            string s;
            input>>s;
            
            map<char,int> m; m.clear();
            for(int i=0; i<=9; i++)
                    m['0'+i]=-1;
            for(char c='a'; c<='z'; c++)
                     m[c]=-1;
                     
            m[s[0]]=1;
            int h=1;
            vector<int> v; v.clear();
            
            FOR(i,s){
                    if(m[s[i]]==-1)
                                    if(h==1){
                                            m[s[i]]=0;
                                            h=2;
                                            }         
                                    else 
                                         m[s[i]]=h++;
                    
                    v.pb(m[s[i]]);
                    }
            if(h==1)
                    h=2;
                    
            
            long long ret=0;
            FOR(i,v){
                     ret=ret*h+v[i];
//  output<<i<<' '<<v[i]<<' '<<ret<<endl;
                     }
    
                
            output<<ret<<endl;
            }
  //  system("pause");                                                             
    
    return 0;
}

