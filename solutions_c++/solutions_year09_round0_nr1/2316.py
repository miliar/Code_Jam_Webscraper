#include <iostream>
#include <cstdio>
using namespace std;
char word[6000][30];
char a[600];
bool cover[30][30];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int l,d,n;
	scanf("%d %d %d",&l,&d,&n);
	for (int i=0;i<d;++i) scanf(" %s",word[i]);
	for (int ti=1;ti<=n;++ti) {
		scanf(" %s",a);
		int len=strlen(a);
		memset(cover,0,sizeof(cover));
		int now=0;
		bool inbr=false;
		
		for (int i=0;i<len;++i) {
			if (a[i]==')') {
				inbr=false;
				now++;
				continue;
			}
			if (a[i]=='(') {
				inbr=true;
				continue;
			}
			cover[now][a[i]-'a'+1]=true;
			if (!inbr) now++;
		}
		/*
		for (int i=0;i<l;++i) {
			for (int j=1;j<=26;++j) if (cover[i][j]) {
				cout<<j<<' ';
			}
			cout<<endl;
		}
		*/
		int c=0;
		for (int i=0;i<d;++i) {
			bool ok=true;
			for (int j=0;j<l;++j) if (!cover[j][word[i][j]-'a'+1]) {
				ok=false;
				break;
			}
			if (ok) c++;
			
		}
		cout<<"Case #"<<ti<<": "<<c<<endl;
	}
	return 0;
}

		
			
		
	
	