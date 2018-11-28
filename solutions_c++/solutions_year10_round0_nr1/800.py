//BISMILLAHIRRAHMANIRRAHIM

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("AsO.txt","w",stdout);
	int T,I,n;
	bool f;
	__int64 k;
	cin>>T;
	for(I=1;I<=T;I++) {
		scanf("%d %I64d",&n,&k);
		//n--;
		f=1;
		//n--
		while(n--) {
			if((k&1)!=1) {
				f=0;
				break;
			}

			k>>=1;
			
		}
		//cout<<f<<'\n';
		printf("Case #%d: %s\n",I,f?("ON"):("OFF"));
	}
	return 0;
}