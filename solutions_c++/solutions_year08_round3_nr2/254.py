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

using namespace std;

#define MAX INT_MAX
#define EPS (1e-10)

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define K(a) ((a)*(a))

#define REP(i,v) for(typeof((v).begin()) i = (v).begin(); i!= (v).end(); ++i )
#define FOR(i,v) for(int i=0; i<v.size(); ++i)

typedef pair<int,int> pii;


long long tab[100];
int k;


int oblicz(long long wynik,long long act,int where){
 if(where>k)
              if(wynik%2==0||wynik%3==0||wynik%5==0||wynik%7==0) return 1;
              else return 0;   
    
 int ret=0;
 
 if(where<k) 
 ret+=oblicz(wynik,act*10+tab[where],where+1);
 ret+=oblicz(wynik-act,tab[where],where+1);
 ret+=oblicz(wynik+act,tab[where],where+1);
 
 return ret;
}


int main(){        
    freopen ("b.out","w",stdout);
    freopen ("b.in","r",stdin);
    
    int n;
    scanf("%d\n",&n);
    for(int i=1; i<=n; i++){
            char c[100];
            scanf("%s\n",c);
            string s(c);
            k=s.size();
            
            for(int j=0; j<k; j++)
                    tab[j]=(s[j]-'0');
                    
            int ret=0;
            ret=oblicz(0,0,0);


            cout<<"Case #"<<i<<": "<<ret/6<<endl;
            }

    
    return 0;
}
