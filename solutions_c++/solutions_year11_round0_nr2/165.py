#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int c,d,n,len;
char cs[50][5],ds[50][5],s[105],ret[105];

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d",&c);
		for (int i=0; i<c; i++) scanf("%s",cs[i]);
		scanf("%d",&d);
		for (int i=0; i<d; i++) scanf("%s",ds[i]);
		scanf("%d",&n);
		scanf("%s",s);
		len=0;
		for (int i=0; i<n; i++) {
			int done=0;
			ret[len]=s[i]; len++;
			if (len==1) continue;
			for (int j=0; j<c; j++)
				if ((ret[len-2]==cs[j][0] && ret[len-1]==cs[j][1]) || (ret[len-2]==cs[j][1] && ret[len-1]==cs[j][0])) {
					ret[len-2]=cs[j][2]; len--;
				}
			for (int j=0; j<d; j++) {
				for (int k=0; k<len-1; k++)
					if ((ret[len-1]==ds[j][0] && ret[k]==ds[j][1]) || (ret[len-1]==ds[j][1] && ret[k]==ds[j][0])) {
						len=0;
						break;
					}
			}
			/*
			printf("%c: ",s[i]);
			for (int i=0; i<len; i++) {
				printf("%c",ret[i]);
			}
			printf("\n");
			*/
		}
		printf("Case #%d: [",T);
		for (int i=0; i<len; i++) {
			if (i>0) printf(", "); 
			printf("%c",ret[i]);
		}
		printf("]\n");
	}
}
