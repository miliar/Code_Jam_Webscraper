#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define E 1e-9
#define FOR(i,ini,fin) for(int i=(int)ini;i<(int)fin;i++)

#define M 1000000000
#define P 100.0000000

typedef long long L;
typedef double D;
typedef pair<int,int>par;

int diez[10];

set<int>v[2000002];
set<int>::iterator iter;
void genera(int n){
    set<int>x;
    int l=1+(int)log10(n), dig,  m=n;
    FOR(i,0,l-1){
        dig=m%10;
        m/=10;
        m= dig*diez[l-1]  + m;
        if(m>n && m<=2000000)v[n].insert(m);
    }
}
int main(){
    diez[0]=1;
    FOR(i,1,9)diez[i]=10*diez[i-1];
    FOR(i,10,2000001)genera(i);
    //cout<<"ya"<<endl;
    int t,a,b, x;
    scanf("%d",&t);
    FOR(i,0,t){
        scanf("%d%d",&a,&b);
        x=0;
        FOR(n,max(a,10),b){
            for(iter=v[n].begin();iter!=v[n].end();iter++){
                if(*iter > b)break;
                x++;
            }
        }
        printf("Case #%d: %d\n",i+1,x);
        //cout<<x<<endl;
    }

    return 0;
}


