#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main(){
	freopen("1.txt","r",stdin);
freopen("2.txt","w",stdout);
	int n,a,b,tp,k,c,T;
	scanf("%d",&n);
	for(T =1; T<=n; ++T){
		scanf("%d%d", &a, &b);
		int cnt = 0;
		for(int i=a; i<=b; i++){
			tp = i;
			k=log10(i*1.0);
			c=pow(10.0,k);
			int v[10],vz=0;
			while(k--){
				int r = tp/10;
				tp = (tp%10) * c + r;
				bool flag=false;
				for(int j=0; j<vz; j++)
					if(v[j] == tp ){
						flag = true;
						break;
					}
				if(flag) continue;
				v[vz++] = tp;
				if( tp <= b && tp >= a  && tp > i)
					++cnt;
			}
		}
		printf("Case #%d: %d\n",T,cnt);
	}
}
