#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int tab[10010];
bool gate[10010];
bool change[10010];
bool val[10010];

int main(){
  int q;
  ios::sync_with_stdio(false);
  cin >> q;
  for(int Q=1;Q<=q;Q++){
    memset(tab,-1,sizeof(tab));
    int m, v;
    cin >> m >> v;
    int i=1;
    for(i=1;i<=m/2;i++){
      int g,c;
      cin >> g >> c;
      if(v==1)
	gate[i]=g;
      else gate[i]=1-g;
      change[i]=c;
    }
    int t = i-1;
    for(;i<=m;i++){
      int valt;
      cin >> valt;
      if(v==1){
	val[i]=valt;
	if(valt==1)tab[i]=0;
      }else{
	val[i]=1-valt;
	if(valt==0)tab[i]=0;
      }
    }
    for(i=t;i>0;i--){
      int left = i<<1,right = (i<<1)|1;
      tab[i]=1000000000;
      if(gate[i]==1){
	if(tab[left]>=0 && tab[right]>=0) tab[i]=tab[left]+tab[right];
      }else{
	if(tab[left]>=0 || tab[right]>=0){
	  if(tab[left]>=0)tab[i]=min(tab[i],tab[left]);
	  if(tab[right]>=0)tab[i]=min(tab[i],tab[right]);
	}
      }
      if(change[i]==1){
	gate[i]=1-gate[i];
	if(gate[i]==1){
	  if(tab[left]>=0 && tab[right]>=0) tab[i]=min(tab[i],tab[left]+tab[right]+1);
	}else{
	  if(tab[left]>=0 || tab[right]>=0){
	    if(tab[left]>=0)tab[i]=min(tab[i],1+tab[left]);
	    if(tab[right]>=0)tab[i]=min(tab[i],1+tab[right]);
	  }
	}
      }
      
      if(tab[i]==1000000000)tab[i]=-1;
    }
    cout<<"Case #"<<Q<<": ";
    if(tab[1]==-1)cout<<"IMPOSSIBLE"<<endl;
    else cout<<tab[1]<<endl;
  }
  return 0;
}
