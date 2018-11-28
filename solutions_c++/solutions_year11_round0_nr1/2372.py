#include<iostream>
#include<cstdio>
using namespace std;

inline int dis(int a,int b){return a-b>0?a-b:b-a;}
inline int sub(int a,int b){return a-b>0?a-b:0;}

int main(){
    int T,n,p,cas=1;
    int o_canwalk, b_canwalk, o_pos, b_pos, ans;
    char r;
    
    scanf("%d",&T);
    while(T--){
        
        scanf("%d",&n);
        o_canwalk = b_canwalk = ans = 0;
        o_pos = b_pos = 1;
        while(n--){

            scanf("%c",&r);     // read ' '
            scanf("%c%d",&r,&p);
            
            if(r=='O'){
                ans += sub(dis(o_pos,p), o_canwalk) + 1;
                b_canwalk += sub(dis(o_pos,p), o_canwalk) + 1;
                o_canwalk = 0;
                o_pos = p;
            }else{
                ans += sub(dis(b_pos,p), b_canwalk) + 1;
                o_canwalk += sub(dis(b_pos,p), b_canwalk) + 1;
                b_canwalk = 0;
                b_pos = p;
            }
            
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
