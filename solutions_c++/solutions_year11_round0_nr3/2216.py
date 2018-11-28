
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

using namespace std;

typedef vector<int> VI;
typedef  int unsigned UI;
typedef long long LL;
typedef  long long unsigned LLU;

int main(){
    int T,N,num,temp,xsum,i=0,sum;
    freopen("csla_in.IN","r+",stdin);
    freopen("cs_ou.txt","w+",stdout);
    cin>>T;
    while(T--){
        i++;
        cin>>N;
        xsum=0;sum=0;
        num=9999999;
        REP(ii,0,N){
            cin>>temp;
            sum+=temp;
            xsum^=temp;
            if(temp<num)
                num=temp;
            
        }
        if(xsum==0)
            cout<<"Case #"<<i<<": "<<sum-num;
        else
            cout<<"Case #"<<i<<": NO";
        cout<<endl;
            
    }
    return 0;
}














