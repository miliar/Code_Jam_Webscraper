#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <fstream>
#include <iomanip>
using namespace std;
typedef long long ll;

//set<pair<int,int> >sp[2];
int mp[120][120];

void fill(int x1, int y1, int x2, int y2){
	for(int i = x1; i <= x2; ++i)
		for(int j = y1; j <= y2; ++j)
			mp[i][j] = 1;
}
int run(){
//	cout<<"run"<<endl;
	for(int i = 100; i >= 1; --i)
		for(int j = 100; j >= 1; --j)
			if(mp[i-1][j] && mp[i][j-1])mp[i][j] = 1;
	for(int i = 100; i >= 1; --i)
		for(int j = 100; j >= 1; --j)
			if(!mp[i-1][j] && !mp[i][j-1])mp[i][j] = 0;
	
	for(int i = 1; i <= 100; ++i)
		for(int j = 1; j <= 100; ++j)
			if(mp[i][j])return 1;
	return 0;
}
	
int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	int T, x1, y1, x2, y2, R, f;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>R;
		memset(mp, 0, sizeof(mp));
		for(int i = 0; i < R; ++i){
			cin>>x1>>y1>>x2>>y2;
			fill(x1, y1, x2, y2);
		}
		int ans = 0;
//		cout<<"hehe"<<endl;
		while(run()){
			++ans;
		}
		cout<<"Case #"<<tt<<": ";
		cout<<ans+1<<endl;
	}
	return 0;
}

