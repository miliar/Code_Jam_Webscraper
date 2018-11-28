#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define read(a) scanf("%d",&a)
#define For(i,a,b) for(int i =(a);i<(b);++i)
#define INFINITY 0x3f000000
int vals[256];
int minCost[256][256];

int D,I,M,N;

int diffMem[513],*diffCost=diffMem+256;

int getMinCost(int i, int val){
   // cout<<i<<" "<<val<<endl;
   // puts("0");
    if(i>=N) return 0;
   // puts("1");
    int&ans = minCost[i][val];
   // puts("2");
    if(ans != INFINITY) return ans;
  //  puts("3");
    //by deleting
    ans = getMinCost(i+1,val)+D;
    //cout<<ans;
    //puts("A");
    //by going within m
    //or by inserting
    int curCost = abs(val-vals[i]);
    for(int x1=0;x1<=255;++x1){
       // cout<<"DFS "<<x1-val<<endl;
        int newVal = curCost+getMinCost(i+1,x1)+(diffCost[x1-val]);
        //cout<<newVal<<endl;
       // cout<<diffCost[x1-val]<<endl;
        //puts("c");
        if(newVal<ans)ans=newVal;
    }
    return ans;
}

int myChange(int i){
    if(i > 0)return i-1;
    if(i<0)return -i-1;
    return 0;
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int n;read(n);
    for(int times=1;times<=n;++times){
        scanf("%d%d%d%d",&D,&I,&M,&N);

        For(i,-256,257){
            diffCost[i] = ((M==0)?INFINITY:(I*(myChange(i)/M)));
        }
        diffCost[0]=0;

        For(i,0,N){
            read(vals[i]);
           // cout<<vals[i]<<endl;
        }
        For(i,0,256)For(j,0,256)minCost[i][j]=INFINITY;

        int minCost = INFINITY;
        For(last,0,256)
        {
            minCost = min(minCost,getMinCost(0,last));
          //  cout<<last<<' '<<minCost<<endl;
        }

        printf("Case #%d: %d\n",times,minCost);
    }
    return 0;
}
