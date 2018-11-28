#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
const int MAX=1005; 
class Wire{
      public:
             int A,B;             
};
inline bool cmp(Wire a,Wire b){
       return ((a.A)>(b.A));
}
int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);    
    int T,N,i,j,k,cnt;
    vector<Wire> list(MAX);
    scanf ("%d",&T);
    for (k=1;k<=T;k++){
        scanf ("%d",&N);
        for (i=0;i<N;i++)
            scanf ("%d %d",&(list[i].A),&(list[i].B));
        sort(list.begin(),list.end(),cmp);
        /*for (i=0;i<N;i++)
            printf("%d %d\n",list[i].A,list[i].B);*/
        cnt=0;
        for (i=0;i<N;i++)
            for (j=i+1;j<N;j++)
                if (list[j].B>list[i].B)
                   cnt++;
        printf("Case #%d: %d\n",k,cnt);
    }
    return 0;
}
