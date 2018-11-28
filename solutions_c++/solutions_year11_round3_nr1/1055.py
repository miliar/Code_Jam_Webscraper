
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
    freopen("1cfin.IN","r+",stdin);
    freopen("1cfout.txt","w+",stdout);
    int i=0,tcases,j,nb,n,r,c,k;
    bool impos=false;
    cin>>tcases;
    char str[51][51];
    while(i<tcases){
        i++;
        nb=0;impos=false;
        cout<<"Case #"<<i<<":"<<endl;
        cin>>r>>c;
        cin.getline(str[0],51);
        REP(ii,0,r){
            cin.getline(str[ii],51);
            for(j=0;j<c;j++)
                if(str[ii][j]=='#')
                    nb++;
        }
        if(nb%4!=0)
            impos=true;
        for(j=0;!impos&&j<r-1;j++){
            for(k=0;!impos&&k<c-1;k++){
                if(str[j][k]=='#'){
                    if(str[j][k+1]=='#'&&str[j+1][k]=='#'&&str[j+1][k+1]=='#'){
                    str[j][k]='/';str[j][k+1]='\\';
                    str[j+1][k]='\\';str[j+1][k+1]='/';
                }else{
                    impos=true;
                }
            }
        }
    }
    if(impos)
    cout<<"Impossible"<<endl;
    else{
        for(j=0;j<r;j++){
                printf("%s\n",str[j]);
            }
        }
    }
        
    return 0;
}














