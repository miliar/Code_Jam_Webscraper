#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

const int dx[4]={0,1,1,0};
const int dy[4]={0,1,0,1};
const char c[4]={'/','/','\\','\\'};

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin >> T;
	for(int q=0;q<T;q++){
		cout << "Case #" << q+1 << ":\n";
		int n,m;
		cin >> n >> m;
		vector<string> a;
		a.resize(n+1);
		for(int i=0;i<n;i++){
			cin >> a[i];
			a[i].push_back('.');
		}
		for(int i=0;i<m+1;i++){
			a[n].push_back('.');
		}
		int f=1;
		for(int i=0;i<n && f;i++){
			for(int j=0;j<m && f;j++){
				if(a[i][j]=='#'){
					int g=0;
					for(int d=0;d<4;d++){
						g+=a[i+dx[d]][j+dy[d]]=='#';
					}
					if(g!=4){
						f=0;
						break;
					}
					for(int d=0;d<4;d++){
						a[i+dx[d]][j+dy[d]]=c[d];
					}
				}
			}
		}
		if(!f){
			cout << "Impossible\n";
			continue;
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}

