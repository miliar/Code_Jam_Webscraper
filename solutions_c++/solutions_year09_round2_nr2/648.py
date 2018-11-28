#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main(){
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);
	int ntest;
	char s[30];
	scanf("%d", &ntest);
	gets(s);
	int j, l;
	int a[30];
	for (int itest=0; itest<ntest; ++itest){		
		gets(s);
		l=strlen(s);
		for (int i=0; i<l; ++i)
			a[i]=s[i]-'0';
		if (!next_permutation(a,a+strlen(s))){
			j=0;
			while (a[j]==0) ++j;
			swap(a[0],a[j]);
			for (j=l; j>0; --j)
				a[j+1]=a[j];
			a[1]=0;
			++l;
		};
		printf("Case #%d: ", itest+1);
		for (int i=0; i<l; ++i)
			printf("%d", a[i]);
		printf("\n");
	}
	return 0;
}