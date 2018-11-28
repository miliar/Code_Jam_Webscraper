#include <iostream>
#include <queue>
#define fi first
#define se second
#include <utility>
#include <algorithm>
using namespace std;

int bit[11111];
long long res;
int apa;
int n;
pair <int,int> lho[11111];
void update(int x,int v){
	 for (int i=x;i<=10000;i+=(i&-i)) bit[i]+=v;
	 }
int sum(int x){
	int tmp=0;
	for (int i=x;i>0;i-=(i&-i)) tmp+=bit[i];
	return tmp;
	}

int main(){
	freopen("ins.in","r",stdin);
	freopen("A.out","w",stdout);
int T=0;
scanf("%d",&T);
while (T--){
	  memset(bit,0,sizeof(bit));
	  memset(lho,0,sizeof(lho));
	  
	  scanf("%d",&n);
	  for (int i=1;i<=n;i++) scanf("%d%d",&lho[i].fi,&lho[i].se);
		  int res=0;
		  sort(lho+1,lho+1+n);
		  reverse(lho+1,lho+1+n);
		  for (int i=1;i<=n;i++){
		  	  int tmp=sum(lho[i].se);
				update(lho[i].se,1);
				res+=tmp;
				}
		  apa++;
		  printf("Case #%d: %d\n",apa,res);
		  
		  }
//	system("pause");
	}
