#include<cstdio>
#include<cmath>
#include<cstring>
#include<time.h>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
using namespace std;


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cs = 0, T, R, C, D; char s[508][508];
    scanf("%d",&T);
    while( T-- ){
        scanf("%d%d%d",&C,&R,&D);
        //cout<<"OK "<<R<<" "<< C<<" "<<D<<endl;
        for(int i=0; i<C; i++) scanf("%s",s[i]);
        int result = -1;
        for(int k=min(C,R); k>=3; k--){
            for(int i=0; i+k<=C; i++){
                for(int j=0; j+k<=R; j++){
                    double x = 0, y = 0;
                    for(int u=0; u<k; u++){
                        for(int v=0; v<k; v++){
                            if( (u==0||u==k-1) && (v==0||v==k-1) ) continue;
                            x += ( u-(k-1)/2.0 )*(s[i+u][j+v]-'0');
                            y += ( v-(k-1)/2.0 )*(s[i+u][j+v]-'0');
                        }
                    }
                    //if( i==1 && j==1 ) cout<<x<<" "<<y<<endl;
                    if( fabs(x)<1e-6 && fabs(y)<1e-6 ){ result = k; break; }
                }
                if( result!=-1 ) break;
            }
            if( result!=-1 ) break;
        }
        printf("Case #%d: ",++cs);
        if( result==-1 ) printf("IMPOSSIBLE\n");
        else printf("%d\n",result);
    }
    return 0;
}
