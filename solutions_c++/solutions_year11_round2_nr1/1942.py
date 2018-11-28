#include <iostream>
#include <cstring>
#include <cmath>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>

#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
int n,i,a[151][151],t,j,k,g,h,col[150];
double res,wp[150],owp[150],oowp;
char x;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(k=0;k<t;++k){
        for(i=0;i<120;++i)
            for(j=0;j<120;++j)
                a[i][j]=-1;

        cin>>n;
        for(i=0;i<n;++i){
            h=g=0;
            for(j=0;j<n;++j){
                cin>>x;
                if (x!='.') a[i][j]=x-48;
                if (a[i][j]==1) h++;
                if (a[i][j]!=-1) g++;
            }
            if (!g) wp[i] = 0;
            else wp[i]=(double)h/g;
            col[i]=g;
        }
            cout<<"Case #"<<k+1<<":\n";
        for(i=0;i<n;++i){
            h=0; owp[i]=0;
            for(j=0;j<n;++j)
                if (a[i][j]!=-1) {
                    if (col[j]>1)  owp[i]+=(double)(wp[j]*col[j]-a[j][i])/(col[j]-1);
                    h++;}
            if (!h) owp[i]=0;
            else owp[i] = (double) owp[i]/h;
        }

        for(i=0;i<n;++i){
            res = (double)wp[i]*0.25;
            res = res+ (double)0.5*owp[i];
            h  =0; oowp=0;
            for(j=0;j<n;++j)
                if (a[i][j]!=-1){
                    h++;
                    if (a[i][j]!=-1) oowp+=owp[j];
                }
            if (!h) oowp=0;
            else oowp = (double)oowp/h;
            res = res+ (double)0.25*oowp;
            printf("%.10lf\n",res);
        }
	}
	return 0;
}
