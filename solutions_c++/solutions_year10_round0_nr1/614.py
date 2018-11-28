#include <cstdio>
#include <string>
using namespace std;




int main() {
int z,zz,n,m,k;
	freopen("d:\\in.in","r",stdin);
	freopen("d:\\o","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",z);
		m=(1<<n);
		puts(((k%m)==m-1)?"ON":"OFF");
	}
	return 0;
}
