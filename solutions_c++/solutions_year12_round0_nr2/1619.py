#include <stdio.h>
#include <algorithm>
using namespace std;

int ta[200];
int main() {
    int t,n,s,p;
    scanf("%d",&t);
    for (int i=1;i<=t;i++) {
    scanf("%d %d %d",&n,&s,&p);
    int x1=0,x2=0;
    for (int j=0;j<n;j++) scanf("%d",&ta[j]);
		for (int j=0;j<n;j++) {
        int x = ta[j];
				if ((x+2)/3>=p) x1++;
        else if (x != 0 && x%3 != 1 && (x+2)/3 >= p -1) x2++;
    }
    printf("Case #%d: %d\n",i,x1+min(x2,s));
    }
    return 0;
}
