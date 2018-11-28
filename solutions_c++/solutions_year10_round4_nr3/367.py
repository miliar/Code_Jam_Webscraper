#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

bool a[300][300];

bool move() {
	bool ans=false;
	for(int i=300;i>0;i--) for(int j=300;j>0;j--) {
		if (a[i][j]) {
			ans=true;
			if (!a[i-1][j] && !a[i][j-1]) a[i][j]=false;
		}
		if (a[i-1][j] && a[i][j-1]) a[i][j]=true;
	}
	return ans;
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		int p;
		cin>>p;
		memset(a,0,sizeof a);
		for(int i=0;i<p;i++) {
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			for(int p=x1;p<=x2;p++) for(int q=y1;q<=y2;q++) a[p][q]=true;
		}
		int ans=0;
		while(move()) ans++;
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}
