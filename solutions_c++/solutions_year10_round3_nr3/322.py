#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <map>

#pragma comment(linker, "/STACK:16000000")

using namespace std;

void solve_gcj1c(){
	int n,m;
	cin>>n>>m;
	int a[1000][3000];
	char ch;
	m/=4;
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			cin>>ch;
			if (ch<='9'){
				ch-='0';
			}
			else{
				ch=ch-'A'+10;
			}
			a[i][j*4+3]=ch%2;
			ch/=2;
			a[i][j*4+2]=ch%2;
			ch/=2;
			a[i][j*4+1]=ch%2;
			ch/=2;
			a[i][j*4]=ch%2;
		}
	}
	m*=4;
	int ans[1000];
	memset(ans,0,sizeof(ans));
	for (int z=min(n,m);z>=0;z--){
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				bool pp=true;
				if ((i+z>n)||(j+z>m)||(a[i][j]<0)) continue;
				for (int i1=0;i1<z;i1++){
					if (!pp) break;
					for (int j1=0;j1<z;j1++){
						if (i1%2==j1%2){
							if ((a[i+i1][j+j1]<0)||(a[i][j]!=a[i+i1][j+j1])){
								pp=false;
								break;
							}
						}
						else{
							if ((a[i+i1][j+j1]<0)||(a[i][j]==a[i+i1][j+j1])){
								pp=false;
								break;
							}
						}
					}
				}
				if (pp){
					ans[z]++;
					for (int i1=0;i1<z;i1++){
						for (int j1=0;j1<z;j1++){
							a[i+i1][j+j1]=-1;
						}
					}
				}
			}
		}
	}
	int ans1=0;
	for (int i=1000;i>=0;i--){
		if (ans[i]>0)
		ans1++;
	}
	cout<<ans1;
	for (int i=1000;i>=0;i--){
		if (ans[i]>0)
			cout<<endl<<i<<' '<<ans[i];
	}
	return;
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);	
	int z;
	cin>>z;
	for (int t=0;t<z;t++){
		cout<<"Case #"<<t+1<<": ";
		solve_gcj1c();
		cout<<endl;
	}
	return 0;
}