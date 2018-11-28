#include <cstdio>
using namespace std;

int a1,a2,b1,b2,ans;

bool canwin(int a,int b) {
	if (a<b) return canwin(b,a);
	if (b==0) return true;
	if (a/b>1) return true; else return !canwin(b,a-b);
}

int main() {
	int cases;
	scanf("%d",&cases);
	for (int dog=1;dog<=cases;dog++) {
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		ans=0;
		for (int a=a1;a<=a2;a++)
			for (int b=b1;b<=b2;b++) {
				if (canwin(a,b)) ans++;
			}
		printf("Case #%d: %d\n",dog,ans);
	}
}
