#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

int T,N;
int x[1010],y[1010];
int main(){    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        for(i=0;i<N;i++)cin>>x[i]>>y[i];

        int cnt=0;
        for(i=0;i<N;i++)
        for(j=i+1;j<N;j++){
           // if( j==i )continue;
            if( (x[i]<x[j]&&y[i]>y[j]) || ( x[i]>x[j]&&y[i]<y[j]) )cnt++;
        }
        printf("Case #%d: %d\n",ca,cnt);
    }
}

