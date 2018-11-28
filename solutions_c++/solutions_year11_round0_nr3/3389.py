#include <cstdio>
#include <iostream>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;
long long isi[1111];
int T,N;
int tc=1;

int main() {
	freopen("C.txt","w",stdout);
	freopen("Cin.txt","r",stdin);
	
scanf("%d",&T);
while (T--){
	memset(isi,0,sizeof(isi));
	long long x=0;
	long long wow=0;
	scanf("%d",&N);
	for (int i=0;i<N;i++){
		scanf("%lld",&isi[i]);
		x+=isi[i];
		wow^=isi[i];
		}
	sort(isi,isi+N);
	printf("Case #%d: ",tc++);
	if (wow) printf("NO\n");
	else printf("%lld\n",x-isi[0]);
	}
}
