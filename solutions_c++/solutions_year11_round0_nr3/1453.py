#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int casos, n, menor, soma, v, op;
	bool resp;
	scanf("%d",&casos);
	for(int i=1; i<=casos; i++){
		scanf("%d",&n);
		menor = 0x7FFFFFFF;
		soma = 0;
		resp = true;
		op = 0;
		for(int j=0; j<n; j++){
			scanf("%d",&v);
			op = op ^ v;
			soma += v;
			menor = min(menor,v);
		}
		soma -= menor;
		
		if(op==0)
			printf("Case #%d: %d\n",i,soma);
		else
			printf("Case #%d: NO\n",i);
	}
}
