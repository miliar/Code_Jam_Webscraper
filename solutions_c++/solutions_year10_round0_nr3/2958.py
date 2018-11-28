#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())


#define CODEJAMJUDGE

  #ifdef CODEJAMJUDGE
     FILE * Input = fopen("Input.in","r");
     FILE * Output = fopen("Output.out","w");
  #endif

  #ifndef CODEJAMJUDGE
     #define Input stdin
     #define Output stdout
  #endif


int main(){
    int T,N,K,R,C;
    int i,t,j;
    fscanf(Input,"%d",&T);
    C^=C;
    while(C<T){
        fscanf(Input,"%d%d%d",&R,&K,&N);
        vi S;
        for(i=0;i<N;i++){
             fscanf(Input,"%d",&t);
             S.pb(t);
        }

        int index = 0;
        int ans = 0;
        int CS = 0;

        for(j=0;j<R;j++){
          vi S1(S.begin()+index,S.end());
        S = S1;
        index = 0;
        for(CS=0,i=index;i<N;i++){
            CS += S[i];
            if(CS<=K){
                S.pb(S[i]);
                index++;
            }
            else{
              ans += (CS-S[i]);
              break;
             }
          }
         ans += (CS<=K)?CS:0;
        }
        fprintf(Output,"Case #%d: %d\n",++C,ans);
    }
    fclose(Input);
    fclose(Output);
    return 0;
}
