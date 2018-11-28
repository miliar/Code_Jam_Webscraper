#include<cstring>
#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	freopen("b-large.in","rt",stdin);
	freopen("b-large.out","wt",stdout);
	int T, tt=0;
	scanf("%d\n",&T);
	char s[100], s2[100];
	while (tt<T) {
		gets(s);
		int len=strlen(s);
		memcpy(s2,s,sizeof(s2));
		bool big=true;
		for(int i=1;i<len;++i) {
			if (s2[i]>s2[i-1]) {
				big=false; break;
			}
		}
		printf("Case #%d: ",++tt);
		if (big) {
			int i=len-1;
			while (s2[i]=='0') --i;
			cout << s2[i] << 0;
			for(int j=len-1;j>=0;--j) {
				if (j!=i) cout << s2[j];
			}
			cout << endl;
			continue;
		}	
		while (1) {
			next_permutation(s,s+len);
			if (s[0]!='0') break;
		} 
		
		if (strcmp(s2,s)>=0) {
			cout <<	s[0] << 0;
			for(int i=1;i<len;++i)
				cout << s[i];
			cout << endl;
		} else printf("%s\n",s);
	}	
	return 0;
}