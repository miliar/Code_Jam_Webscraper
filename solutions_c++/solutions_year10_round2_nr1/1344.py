#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class directory {
public:
	int def;
	int p;
	char x[100][100];
};

directory a[200];
int n,m;
int ans;
bool cmp(directory x,directory y) {
	return x.def<y.def;
}
int main() {
	int T,Ti;
	FILE *fi=fopen("input.txt","rt");
	FILE *fo=fopen("output.txt","wt");
	fscanf(fi,"%d",&T);
	for(Ti=0;Ti<T;Ti++) {
		fscanf(fi,"%d%d",&m,&n);
		int i;
		for(i=0;i<m;i++) {
			char tp[101];
			fscanf(fi,"%s",tp);
			int cep=0;
			char cp[101];
			strset(cp,0);
			int eqa=strlen(tp);
			for(int l=1;l<eqa;l++) {
				if(tp[l]=='/') {
					for(int j=0;j<cep;j++) {
						a[i].x[a[i].p][j]=cp[j];
					}
					a[i].p++;
					cep=0;
					for(j=0;j<100;j++) cp[j]=0;
				} else cp[cep++]=tp[l];
			}
			for(int j=0;j<cep;j++) {
				a[i].x[a[i].p][j]=cp[j];
			}
			a[i].p++;
			a[i].def=0;
		}
		for(i=m;i<m+n;i++) {
			char tp[101];
			fscanf(fi,"%s",tp);
			int cep=0;
			char cp[101];
			strset(cp,0);
			int eqa=strlen(tp);
			for(int l=1;l<eqa;l++) {
				if(tp[l]=='/') {
					for(int j=0;j<cep;j++) {
						a[i].x[a[i].p][j]=cp[j];
					}
					a[i].p++;
					cep=0;
					for(j=0;j<100;j++) cp[j]=0;
				} else cp[cep++]=tp[l];
			}
			for(int j=0;j<cep;j++) {
				a[i].x[a[i].p][j]=cp[j];
			}
			a[i].p++;
			a[i].def=1;
		}
		sort(a,a+n+m,cmp);
		int sp=0;
		for(i=0;i<n+m;i++) {
			if(a[i].def==1) {
				sp=i;
				break;
			}
		}
		int cand;
		for(i=sp;i<n+m;i++) {
 			cand=999999;
 			if(i==0) {
				cand=a[i].p;
			}
			else {
				for(int j=0;j<i;j++) {
					int k;
					for(k=0;k<a[j].p;k++) {
						if(strcmp(a[j].x[k],a[i].x[k])) break;
					}
					cand=cand>(a[i].p-k)?(a[i].p-k):cand;
				}
			}
			ans+=cand;
		}
		fprintf(fo,"Case #%d: %d\n",Ti+1,ans);
		ans=0;
		for(i=0;i<100;i++) {
			for(int j=0;j<100;j++) {
				for(int k=0;k<100;k++) {
					a[i].x[j][k]=0;
				}
			}
			a[i].p=0;
			a[i].def=0;
		}
	}
	return 0;
}