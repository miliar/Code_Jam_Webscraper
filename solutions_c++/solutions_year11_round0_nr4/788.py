#include <cstdio>

int main() {

freopen("d.in","r",stdin);
freopen("d.out","w",stdout);

int t;
scanf("%d",&t);

double m[1001];
double p[1001];
m[0]=.0;
m[1]=.0;           
m[2]=2.0;

p[0]=1.0;

p[1]=0.0;
for (int i=2;i<1001;i++) {
	double pp=0.0;
	for (int j=0;j<i;j++)
		{
		double tmp=p[j];
		for (int k=1;k<=(i-j);k++) tmp/=(double)k;
		pp+=tmp;
		}
	p[i]=1.0-pp;
	}

for (int i=3;i<1001;i++) {
	double sum=.0;
	for (int j=2;j<i;j++) {
		double tmp=m[j]*p[j];
		for (int k=1;k<=(i-j);k++) tmp/=(double)k;
		sum+=tmp;
		} 
	sum+=1.0;
	m[i]=sum/(1-p[i]);
	}


for (int j=0;j<t;j++) {
        int n;
	scanf("%d",&n);
	int m1=n;
	int k;
	for (int i=0;i<n;i++) {
		scanf("%d",&k);
		if (k==(i+1)) m1--;
		}
	printf("Case #%d: %.6lf\n",j+1,m[m1]);
	}

return 0;

}
