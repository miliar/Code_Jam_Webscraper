#include <cstdio>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 1100

int n,q;
string engines[MAXN];
map<string,int> mp;
int resp[MAXN][MAXN];

int main(){
    
    int i,j,k,h;
    int t,lp;
    char buf[2*MAXN];
    
    gets(buf);
    sscanf(buf,"%d",&t);
    
    for(lp=1;lp<=t;lp++){
        mp.clear();
        gets(buf);
        sscanf(buf,"%d",&n);
        for(i=1;i<=n;i++){
            gets(buf);
            mp[string(buf)] = i;    
        }
        
        gets(buf);
        sscanf(buf,"%d",&q);
        
        for(i=0;i<=q;i++){
            for(j=0;j<=n;j++){
                resp[i][j] = q*q;    
            }   
        }
        
        for(j=1;j<=n;j++) resp[0][j] = 0;
        
        for(i=1;i<=q;i++){
            gets(buf);
            k = mp[string(buf)];
            for(j=1;j<=n;j++){
                if(j == k){
                    for(h=1;h<=n;h++){
                        if(h == k) continue;
                        resp[i][h] = min(resp[i][h],1+resp[i-1][j]);   
                    }
                }
                else{
                    resp[i][j] = min(resp[i][j],resp[i-1][j]);//não precisa trocar
                }    
            }
        }
        
        int ret = q*q;
        for(i=1;i<=n;i++){
            ret = min(ret,resp[q][i]);    
        }
        
        printf("Case #%d: %d\n",lp,ret);
           
    }
       
    return 0;
    
}
