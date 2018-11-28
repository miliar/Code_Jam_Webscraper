#include <cstdio>
#include <algorithm>
using namespace std;
class ball{
  public:
  int r;
  int num;
};
bool operator<(const ball &a, const ball &b){
  if(a.r<b.r) return true;
  else return false;
}
ball arr[1000];
int ans[1000][2];
int main(){
  int t;
  bool fail=false;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    int W,L,n;
    scanf("%d %d %d",&n, &W, &L);
    for(int i=0;i<n;i++){
      arr[i].num=i;
      scanf("%d",&arr[i].r);
    }
    sort(arr,arr+n);
    reverse(arr,arr+n);
    int idx=0;
    int y=0;
    int x=0;
    int maxY=arr[0].r;
    bool start=true;
    ans[arr[0].num][0]=0;
    ans[arr[0].num][1]=0;
    x=arr[0].r;
    idx=1;
    while(idx<n){
      //pchamy
      int who=arr[idx].num;
      if(x+arr[idx].r<=W){
        ans[who][0]=x+arr[idx].r;
        x+=2*arr[idx].r;
        if(start) ans[who][1]=y;
        else ans[who][1]=y+arr[idx].r;
        maxY=max(maxY, ans[who][1]+arr[idx].r);
        idx++;
      }else{
        //stawiamy
        start=false;
        ans[who][0]=0;
        ans[who][1]=maxY+arr[idx].r;
        //nowy rzad
        x=arr[idx].r;
        y=maxY;
        maxY+=2*arr[idx].r;

        idx++;
      }
    }
    printf("Case #%d:",tt);
    for(int i=0;i<n;i++) printf(" %d %d",ans[i][0], ans[i][1]);
    //printf(" %d max=%d",L,maxY);
    //for(int i=0;i<n;i++) if(ans[i][1]>L) fail=true;
    printf("\n");

  }
  //if(fail) printf("\n FUUUUUUUUUUUUUUUUUUUUU");
  //else printf("\n OK");
  return 0;
}







