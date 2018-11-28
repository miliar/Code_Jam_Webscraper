#include <stdio.h>
#include <math.h>

int v[50],x[50],c[50];


void qsort(int l,int r) {
int rr,rl;
int i=l,j=r;

rl=v[l+(r-l)/2];

while (i<=j) {
	while (v[i]>rl) i++;
	while (v[j]<rl) j--;
	if (i<=j) {
		rr=v[i];
		v[i]=v[j];
		v[j]=rr;
		i++;
		j--;
		}
	}
if (i<r) qsort(i,r);
if (j>l) qsort(l,j);



}



int main() {

freopen("B.in","r",stdin);
freopen("B.out","w",stdout);





int tst;
scanf("%d",&tst);

for (int nu=1;nu<=tst;nu++) {
printf("Case #%d: ",nu);

int n,k,b,t;
scanf("%d%d%d%d",&n,&k,&b,&t);




for (int i=0;i<n;i++) scanf("%d",&x[i]);
for (int i=0;i<n;i++) scanf("%d",&v[i]);


if (k==0) {printf("0\n");continue;}


for (int i=0;i<n;i++) {
	int j=i;
	while (x[j]==x[i]) {j++;if (j>=n) break;}
	qsort(i,j-1);

	}       


int c[50];

int pos;
for (int i=0;i<n;i++) {
	pos=x[i]+v[i]*t;
	if (pos>=b) c[i]=1;else c[i]=0;
	}

int flg=0;
int p;
for (p=n-1;p>=0;p--) {
	if (c[p]) k--;
	if (k==0) {flg=1;break;}
	}

if (flg) {

int ans=0;
for (int i=p;i<n;i++) {
	if (c[i]) {
		int j=i;
		while (x[i]==x[j]) {j++;if (j>=n) break;}
		if (!c[j-1]) ans++;
		
		for (int l=j;l<n;l++) if (!c[l]) ans++;
		}
	}

printf("%d\n",ans);}
else printf("IMPOSSIBLE\n");

}
return 0;
}

