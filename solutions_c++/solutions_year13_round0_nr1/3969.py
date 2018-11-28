#include<iostream>      
#include<cstdio>      
#include<map>      
#include<cstring>      
#include<cmath>      
#include<vector>      
#include<algorithm>      
#include<set>      
#include<stack>    
#include<string>      
#include<ctime>    
#include<queue>      
#define inf 0x3f3f3f3f   
#define maxn 210005      
#define eps 1e-8    
#define zero(a) fabs(a)<eps      
#define Min(a,b) ((a)<(b)?(a):(b))      
#define Max(a,b) ((a)>(b)?(a):(b))      
#define pb(a) push_back(a)      
#define mp(a,b) make_pair(a,b)      
#define mem(a,b) memset(a,b,sizeof(a))      
#define LL long long      
#define MOD 1000000007    
#define sqr(a) ((a)*(a))      
#define Key_value ch[ch[root][1]][0]      
#define test puts("OK");      
#define pi acos(-1.0)    
#define lowbit(x) ((-(x))&(x))    
#define HASH1 1331    
#define HASH2 10001 
#define lson step<<1
#define rson step<<1|1   
#define C   240      
#define vi vector<int>    
#define TIME 10      
//#pragma comment(linker, "/STACK:1024000000,1024000000")      
using namespace std;
char str[5][5];
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--){
        int emp=0;
        for(int i=0;i<4;i++){
            scanf("%s",str[i]);
            for(int j=0;j<4;j++)
                if(str[i][j]=='.')
                    emp++;
        }
        bool o=false,x=false;
        for(int i=0;i<4;i++){
            int O=0,X=0,T=0;
            for(int j=0;j<4;j++){
                if(str[i][j]=='T') T++;
                else if(str[i][j]=='X') X++;
                else if(str[i][j]=='O') O++;
            }
            if(O==4||(O==3&&T==1)) o=true;
            if(X==4||(X==3&&T==1)) x=true;
        }
        for(int i=0;i<4;i++){
            int O=0,X=0,T=0;
            for(int j=0;j<4;j++){
                if(str[j][i]=='T') T++;
                else if(str[j][i]=='X') X++;
                else if(str[j][i]=='O') O++;
            }
            if(O==4||(O==3&&T==1)) o=true;
            if(X==4||(X==3&&T==1)) x=true;
        }
        int O=0,X=0,T=0;
        for(int i=0;i<4;i++){
            if(str[i][i]=='T') T++;
            else if(str[i][i]=='X') X++;
            else if(str[i][i]=='O') O++;
            if(O==4||(O==3&&T==1)) o=true;
            if(X==4||(X==3&&T==1)) x=true;
        }
        O=0,X=0,T=0;
        for(int i=0;i<4;i++){
            if(str[i][3-i]=='T') T++;
            else if(str[i][3-i]=='X') X++;
            else if(str[i][3-i]=='O') O++;
            if(O==4||(O==3&&T==1)) o=true;
            if(X==4||(X==3&&T==1)) x=true;
        }
        printf("Case #%d: ",++cas);
        if(o)  puts("O won");
        else if(x) puts("X won");
        else if(emp) puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}