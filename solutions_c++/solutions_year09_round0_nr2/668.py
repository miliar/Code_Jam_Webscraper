#include<iostream>
#include<vector>
#include<stack>

using namespace std;

int main() {

	int t;
	cin>>t;
	
	for(int ti=0;ti<t;ti++) {
		int h,w;
		cin>>h>>w;
		vector<vector<int> > map(h,vector<int>(w));
		vector<vector<char> > ans(h,vector<char>(w,'\0'));
		for(int i=0;i<h;i++) {
			for(int j=0;j<w;j++) {
				cin>>map[i][j];
			}
		}
		char ch = 'a';
		for(int k=0;k<h;k++) {
			for(int l=0;l<w;l++) {
				stack<pair<int,int> > s;
				int i,j;
				i = k;
				j = l;
				while(ans[i][j]=='\0') {
                    s.push(pair<int,int>(i,j));
					pair<int,int> nextpos;
					int min = map[i][j];
					if(i>0&&map[i-1][j]<min) {
						min = map[i-1][j];
						nextpos.first = i-1;
						nextpos.second = j;
					}
					if(j>0&&map[i][j-1]<min) {
						min = map[i][j-1];
						nextpos.first = i;
						nextpos.second = j-1;
					}
					if(j<w-1&&map[i][j+1]<min) {
						min = map[i][j+1];
						nextpos.first = i;
						nextpos.second = j+1;
					}
					if(i<h-1&&map[i+1][j]<min) {
						min = map[i+1][j];
						nextpos.first = i+1;
						nextpos.second = j;
					}
					if(min==map[i][j]) {
						ans[i][j] = ch++;
						s.pop();
					}
					else {
						i = nextpos.first;
						j = nextpos.second;
					}
				}
				while(!s.empty()) {
					pair<int,int> pos = s.top();
					ans[pos.first][pos.second] = ans[i][j];
					s.pop();
				}
			}
		}
		cout<<"Case #"<<ti+1<<":\n";
		for(int i=0;i<h;i++) {
			for(int j=0;j<w;j++) {
				cout<<ans[i][j]<<" ";
			}
			cout<<'\n';
		}
	}
}
