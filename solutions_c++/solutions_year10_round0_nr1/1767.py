#include <iostream>
#include <queue>
using namespace std;
int main(){
	freopen("ins.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T;
	int a,b;
		int apa=1;
	scanf("%d",&T);
	while (T--){
		 scanf("%d%d",&a,&b); a--;
		 bool ok=1;
		 for (int i=0;i<=a;i++)
		 if ((1ll<<i) & b); else ok=0;
		  if (ok) printf("Case #%d: ON\n",apa);
		 else  printf("Case #%d: OFF\n",apa);
		  
		  apa++;
		  }
	
	}
