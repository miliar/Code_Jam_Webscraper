
/*
author:ravi shukla
*/

# include<iostream>
# include<cstdio>
# include<cstring>
# include<cstdlib>
# include<cmath>
# include<cassert>
# include<cctype>
# include<algorithm>

# include<vector>
# include<limits>
# include<list>
# include<stack>
# include<queue>
# include<set>
# include<map>
# include<bitset>
# include<sstream>
# include<deque>
# include<fstream>


#define REP(ii,a,b) for(int ii=a;ii<(int)(b);++ii)
#define REPD(ii,a,b) for(int ii=a;ii>(int)(b);ii--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define HASB(a,b) ((a&(1<<b))>0)
#define PI 3.14159265 

#define IMAX 2147483647
#define IMIN -2147483648
using namespace std;

typedef vector<int> VI;
typedef  int unsigned UI;
typedef long long LL;
typedef  long long unsigned LLU;

int main(){
    freopen("1cSin.txt","r+",stdin);
    freopen("1cSout.txt","w+",stdout);
    int i=0,tcases,j,nb,n,l,h,k;
     cin>>tcases;
     int num[105];
    while(i<tcases){
        i++;nb=0;
        cout<<"Case #"<<i<<":";
        cin>>n>>l>>h;
        REP(ii,0,n){
            cin>>num[ii];
        }
        for(j=l;j<=h;j++){
            for(k=0;k<n;k++){
                if(num[k]%j==0||j%num[k]==0)
                    continue;
                break;
            }
            if(k==n)
                break;
            }
        if(j==h+1)
            cout<<" NO";
        else
            cout<<" "<<j;
        cout<<endl;
    } 
    return 0;
}














