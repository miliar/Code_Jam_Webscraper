#include<iostream>
using namespace std;

char s[1000];

int N;

int r[1000];

int run() {
	cin>>N;
	for(int i=1;i<=N;++i) {
		scanf("%s", s+1);
		int &a = r[i];
		a=0;
		for(int j=1;j<=N;++j)
			if(s[j]=='1') a=max(a,j);
	}
	int ans =0;
	for(int i=1;i<=N;++i) {
		if(r[i]>i) {
			for(int j=i+1;j<=N;++j)
				if(r[j]<=i) {
					ans += j-i;
					for(int k=j;k>i;--k) r[k]=r[k-1];
					break;
				}
		}
	}
	cout<<ans<<endl;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test; cin>>test;
	for(int no=1;no<=test;++no) {
		cout<<"Case #"<<no<<": "; run();
	}
}
