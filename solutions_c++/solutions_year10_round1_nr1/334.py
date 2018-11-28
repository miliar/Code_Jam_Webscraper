#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

char tmp[111][111],s[111][111];
int n,k;
int ans1,ans2;

void work(){
	memset(s,0,sizeof(s));
	memset(tmp,0,sizeof(tmp));
	ans1=ans2=0;
	cin >> n >> k;
	for (int i=0;i<n;i++) cin>>tmp[i];
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			s[j][n-i-1]=tmp[i][j];
	for (int i=n-1;i>=0;i--)
		for (int j=0;j<n;j++){
			int x=i,y=j;
			if (s[x][y]=='.') continue;
			while (x+1<n&&s[x+1][y]=='.'){
				s[x+1][y]=s[x][y];s[x][y]='.';x++;
			}
		}
		
	//for (int i=0;i<n;i++) cout << s[i] <<endl;
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++){
			int f1,f2;
			if (i+k<=n){
				f1=f2=1;
				for (int p=0;p<k;p++){
					if (s[i+p][j]!='R') f1=0;
					if (s[i+p][j]!='B') f2=0;
				}
				ans1|=f1;
				ans2|=f2;
			}
			if (j+k<=n){
				f1=f2=1;
				for (int p=0;p<k;p++){
					if (s[i][j+p]!='R') f1=0;
					if (s[i][j+p]!='B') f2=0;
				}
				ans1|=f1;
				ans2|=f2;
			}
			if (i+k<=n&&j+k<=n){
				f1=f2=1;
				for (int p=0;p<k;p++){
					if (s[i+p][j+p]!='R') f1=0;
					if (s[i+p][j+p]!='B') f2=0;
				}
				ans1|=f1;
				ans2|=f2;
			}
			if (i-k>=0&&j+k<=n){
				f1=f2=1;
				for (int p=0;p<k;p++){
					if (s[i-p][j+p]!='R') f1=0;
					if (s[i-p][j+p]!='B') f2=0;
				}
				ans1|=f1;
				ans2|=f2;
			}
		}
	if (ans1&&ans2) cout <<"Both" <<endl;
	else if (ans1) cout << "Red" <<endl;
	else if (ans2) cout << "Blue" <<endl;
	else cout <<"Neither" <<endl;
}


int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;cin >> t;
	int num=1;
	while (t--) {
		cout <<"Case #" << num++ << ": ";
		work();
	}
	return 0;
}
