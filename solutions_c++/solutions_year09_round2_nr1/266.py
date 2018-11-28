#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
struct cell {
	char nm[22];
	double k;
	long ls,rs;
} a[1000];
char ch[2222][22];
long ntests,root,kol,n;

void read(long x) {
	char c;
		for (c=getchar();c!='(';c=getchar());

        scanf("%lf",&a[x].k);
        scanf("%s",&a[x].nm);
       	long len = strlen(a[x].nm);
       	if (a[x].nm[0]!=')') {
		a[x].ls = ++kol;
		read(a[x].ls);
		a[x].rs = ++kol;
		read(a[x].rs);
		for (c=getchar();c!=')';c=getchar());
       	}
}

inline long cmp(long x, long y) {
	long l1 = strlen(a[x].nm);
	long l2 = strlen(ch[y]);

	if (l1!=l2) return 0;

	for (long i=0;i<l1;i++)
		if (a[x].nm[i]!=ch[y][i]) return 0;

	return 1;
}

double ans(long x, double T) {
	 T *= a[x].k;

	 if (a[x].nm[0]==')') return T;

	 long f = 0;
	 for (long i=0;i<n;i++) 
	 	if (cmp(x,i)) {
	 		f = 1;
	 		return ans(a[x].ls,T);
	 		break;
	 	}

	if (!f) return ans(a[x].rs,T);
}

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("input2.txt","w",stdout);
	
	char we;
	for (;scanf("%c",&we)!=EOF;) {
		if (we==')' || we=='(') printf(" ");
		printf("%c",we);
		if (we==')' || we=='(') printf(" ");
	}

	freopen("input2.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d\n",&ntests);
	for (long _=1;_<=ntests;_++) {
	        memset(a,0,sizeof(a));
	        memset(ch,0,sizeof(ch));
	        root = 0; kol = 0;
	        long l,A;
	        char wwww[100];
	        scanf("%d\n",&l);
	        read(root);
		scanf("%d\n",&A);

		printf("Case #%d:\n",_);
                for (long __=0;__<A;__++) {
                	char www[1111];
                	scanf("%s",&www);
                	scanf("%d",&n);
                	for (long W=0;W<n;W++) scanf("%s",&ch[W]);
                	scanf("\n");
                	printf("%lf\n",ans(root,1));	
                }  


		
	}

	return 0;
}
