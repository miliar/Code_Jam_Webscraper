/*
    ID:
    PROG:
    LANG:C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
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
#include <cstring>
using namespace std;

int comb[50][50],opp[50][50],a[500],ta;
int n,m,t;
string s;
char x;
int main(){
    //freopen("b-large.in","r",stdin);
    //freopen("b-large.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;++cs){
        memset(comb,0,sizeof(comb));
        memset(opp,0,sizeof(opp));
        cin>>m;
        for(int i=0;i<m;++i){
            cin>>s;
            comb[s[1]-'A'+1][s[0]-'A'+1]=comb[s[0]-'A'+1][s[1]-'A'+1]=s[2]-'A'+1;
        }
        cin>>m;
        for(int i=0;i<m;++i){
            cin>>s;
            opp[s[1]-'A'+1][s[0]-'A'+1]=opp[s[0]-'A'+1][s[1]-'A'+1]=1;
        }
        cin>>n;
        ta=0;
        for(int i=0;i<n;++i){
            cin>>x;
            a[ta++]=x-'A'+1;
            while(ta>1 && comb[a[ta-1]][a[ta-2]]){
                a[ta-2]=comb[a[ta-1]][a[ta-2]];
                --ta;
            }
            for(int i=0;i<ta-1;++i)
                if(opp[a[ta-1]][a[i]])ta=0;
        }
        cout<<"Case #"<<cs<<": [";
        if(ta!=0){
            x=a[0]+'A'-1;
            cout<<x;
            for(int i=1;i<ta;++i){
                 x=a[i]+'A'-1;
                 cout<<", "<<x;
            }
        }
        cout<<"]"<<endl;
    }
    //fclose(stdout);
    return 0;
}
