
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
    int i=0,tcases,n,olast,blast,pos,time,temp,tempo,tempb,to,tb;
   freopen("bt_inl.IN","r+",stdin);
   freopen("bt_out.txt","w+",stdout);
    char id;
        cin>>tcases;
    while(i<tcases){
        i++;
        cin>>n;
        time=0;
        tempo=tempb=0;
        olast=1;blast=1;
        while(n--){
        cin>>id>>pos;
        if(id=='O'){
            temp=abs(pos-olast);
            if(temp>=tempb){
                to=(temp-tempb)+1;
                tempo+=to;
                tempb=0;
                }else {
            tempb=0;
           to= 1;tempo=1;
           }
        olast=pos;
        time+=to;
    }else{//blue
        temp=abs(pos-blast);
        if(temp>=tempo){
            tb=(temp-tempo)+1;
            tempb+=tb;
            tempo=0;
            }else{
            tempo=0;
            tb=1;tempb=1;
            
        }
        blast=pos;
        time+=tb;
    }
    }
    
    cout<<"Case #"<<i<<": "<<time;
    cout<<endl;
}
    return 0;
}














