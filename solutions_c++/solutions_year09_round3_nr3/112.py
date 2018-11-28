#include<iostream>
#include<algorithm>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
const int INF = (1 << 29);

int table[102][102];//l//r
int solve(int l,int r,int *a,int n){
  if ( l>r)return 0;
  if ( r-l==1)return 0;
  if (r == l)return table[l][r]= 0;
  if ( table[l][r] != -1)return table[l][r];
  
  
  int ret = INF;
  for(int i=l+1;i<r;i++){
    int left ,right;
    a[i]--;
    left = solve(l,i,a,n);
    a[i]+=2;
    right = solve(i,r,a,n);
    a[i]--;
    //ret = min(ret,solve(l,i,a,n)+solve(i,r,a,n)+ a[i]-a[l]+a[r]-a[i]-1);
    //    cout << l << " " << i<< " " <<r << " " << left << " " << right << " " << 
    //  a[i]-a[l]+a[r]-a[i] << endl;
    ret = min(ret,right+left+a[i]-a[l]+a[r]-a[i]);
  }
  
  return table[l][r] = ret;
}

main(){
  int te,tc=1;
  cin>>te;
  while(te--){
   int p,q;
   cin>>p>>q;
   rep(i,q+2)rep(j,q+2)table[i][j]=-1;
   int a[q+2];
   rep(i,q)cin>>a[i+1];
   a[0]=1;
   a[q+1]=p;
   int ans = solve(0,q+1,a,q);
   cout << "Case #"<<tc++<<": " << ans << endl;

   /*
   REP(i,1,q+1){
     REP(j,1,q+1)cout << table[i][j] << " ";
     cout <<endl;
   }
   */

  }
}
