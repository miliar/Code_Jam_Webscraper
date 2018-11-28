#include <iostream>
#include <cstring>
using namespace std;

int d,n,l;
bool p[20][26];
char a[6000][20];
int main() {
	cin>>l>>n>>d;
	for(int i=0;i<n;i++) { cin>>a[i]; }
	for(int i=0;i<d;i++) {
		int ans=0;
		memset(p,0,sizeof p);
		for(int j=0;j<l;j++) {
			char ch;
			cin>>ch;
			if (ch=='(') {
				cin>>ch;
				while (ch!=')') {
					p[j][ch-'a']=1;
					cin>>ch;
				}
			} else {
				p[j][ch-'a']=1;
			}
		}
		for(int k=0;k<n;k++) {
			ans++;
			for(int j=0;j<l;j++) if (!p[j][a[k][j]-'a']) {
				ans--;
				break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
