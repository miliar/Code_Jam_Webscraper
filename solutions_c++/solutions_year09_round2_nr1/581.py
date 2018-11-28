#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>

struct num{
	double w;
	char s[100];
};

char s[1024][1024];
num a[1024];
char q;

void tak(int i){
	scanf(" ( %lf %s", &a[i].w, &a[i].s);
	if (a[i].s[0]==')'){
		a[i].s[0]=0;
	}else{
		tak(2*i);
		tak(2*i+1);
	}
	scanf(" ) ");
}

double p;
int l;

void solve(int i){
	bool g=false;
	p=p*a[i].w;
	for (int j=0; j<l; ++j){
		if (strcmp(s[j],a[i].s)==0) g=true;
	}
	if (a[i].s[0]!=0){
		if (g) solve(2*i);
		else solve(2*i+1);	
	}
}

int m;

int main(){
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);
	int ntest, n;
	scanf("%d", &ntest);
	for (int itest=0; itest<ntest; ++itest){
		printf("Case #%d:\n", itest+1);
		scanf("%d", &n);
		gets(s[0]);
		tak(1);
		scanf("%d", &m);
		for (int i=0; i<m; ++i){
			scanf("%*s %d", &l);
			for (int j=0; j<l; ++j){
				scanf("%s", &s[j]);			
			}			
			p=1;
			solve(1);
			printf("%.6lf\n", p);
		}
	}
	return 0;
}