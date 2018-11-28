#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,Case,N,a[50];
    scanf("%d",&T);
    Case=1;
    while(T--){
        scanf("%d",&N);
        char str[100];
        for(int i=1;i<=N;i++){
            scanf("%s",str);
            int j;
            for(j=N-1;j>=0;j--){
                if(str[j]=='1')break;
            }
            a[i]=j+1;
        }
        int cnt=0;
        for(int i=1;i<=N;i++){
            for(int j=i;j<=N;j++){
               
                if(a[j]<=i){
                    cnt+=j-i;
                    swap(a[i],a[j]);
                    break;
                }
                swap(a[i],a[j]);
            }
//            for(int k=1;k<=N;k++)printf("%d ",a[k]);
//            printf("\n");
        }
        printf("Case #%d: %d\n",Case,cnt);
        Case++;


    }
    return 0;
}