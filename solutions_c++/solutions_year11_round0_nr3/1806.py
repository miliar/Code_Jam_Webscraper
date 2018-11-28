
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<float> vf;

#define For(i,a,b) for (int i(a),_b(b);i<b;i++)
#define Rep(i,a) for (int i(0),_a(a);i<a;i++)
#define Repd(i,a) for (int i(a),_a(a);i>0;i--)


int main(){
  freopen("C-large.in","rt",stdin);
  freopen("output.txt","wt",stdout);
  int cases;
  scanf("%d\n",&cases);
  Rep(i,cases){
    int candies;
    scanf("%d\n",&candies);
    vi can(candies);
    Rep(j,candies){
      scanf("%d",&can[j]);
    }
    int min=0;

   
    int xans=0;
    int ans=0;
    Rep(j,candies){
      xans=xans ^ can[j];
    }
    if(xans!=0){
      printf("Case #%d: NO\n",i+1);
    }
    else{
      Rep(j,candies){
      if(can[j]<can[min])min=j;
      ans=ans+can[j];
    }
      ans=ans-can[min];
      printf("Case #%d: %d\n",i+1,ans);
    }  
  }
}
