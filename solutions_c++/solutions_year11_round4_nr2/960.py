#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;


int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("outB1.txt","w",stdout);
    int T,k,i,j,ii,jj,a[110][110],flag,R,C,D,cc;
    int x0,y0,x,y;
    char s[100][110];
    scanf("%d",&T);
    for(cc=1;cc<=T;cc++) {
        scanf("%d%d%d",&R,&C,&D);
        //printf("%d %d %d\n",R,C,D);
        for(i=0;i<R;i++) {
            scanf("%s",s[i]);
            //printf("%s\n",s);
            for(j=0;j<C;j++) a[i][j]=D+s[i][j]-'0';
        }
       // continue;
       // for(i=0;i<R;i++) {for(j=0;j<C;j++) printf("%c",s[i][j]); printf("\n"); }
        printf("Case #%d: ",cc);
        for(k=min(R,C);k>=3;k--) {
            for(i=0;i<R;i++) {
                for(j=0;j<C;j++) {
                    if(i+k>R||j+k>C) continue;
                    flag=0;
                    if(k%2==1) {
                        x0=2*i+k-1;
                        y0=2*j+k-1;
                        
                    }
                    else {
                        x0=2*i+k-1;
                        y0=2*j+k-1;
                    }
                   // cout<<k<<" "<<x0<<" "<<y0<<endl;
                    x=y=0;
                    int fuck=0;
                    for(ii=i;ii<i+k;ii++) {
                        for(jj=j;jj<j+k;jj++) {fuck++;
                            if((ii==i&&jj==j)||(ii==i&&jj==j+k-1)||(ii==i+k-1&&jj==j)||(ii==i+k-1&&jj==j+k-1)) continue;
                            x+=(2*ii-x0)*(s[ii][jj]-'0');
                            y+=(2*jj-y0)*(s[ii][jj]-'0');
                           // printf("%d %d %d %d %c8\n",ii,jj,x0,y0,s[ii][jj]);
                          //  cout<<2*ii-x0<<" "<<2*jj-y0<<" "<<s[ii][jj]<<" "<<ii<<" "<<jj<<endl;
                          //  cout<<(2*ii-x0)*(s[ii][jj]-'0')<<" "<<(2*jj-y0)*(s[ii][jj]-'0')<<" "<<i<<" "<<j<<endl;
                          //  cout<<x<<" "<<y<<endl;
                        }
                    }
                    //cout<<fuck<<x<<" "<<y<<endl;
                    if(x==0&&y==0) {
                        printf("%d\n",k);
                        flag=1;
                        break;
                    }
                }
                if(j<C) {
                    break;
                }
            }
            if(i<R) break;
        }
        if(k<3) printf("IMPOSSIBLE\n");
    }
    //system("pause");
    return 0;
}
