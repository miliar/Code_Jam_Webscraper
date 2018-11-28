#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <fstream>
using namespace std;
typedef long long ll;

int vis[30], del[10][10], com[10][10], val[300];
char nval[30];

void init(){
	memset(val, -1, sizeof(val));
	val['Q'] = 0;
	val['W'] = 1;
	val['E'] = 2;
	val['R'] = 3;
	val['A'] = 4;
	val['S'] = 5;
	val['D'] = 6;
	val['F'] = 7;
	int m = 8;
	for(char ch = 'A'; ch <= 'Z'; ++ch){
		if(val[ch] == -1){
			val[ch] = m++;
		}
		nval[val[ch]] = ch;
	}
}
vector<int> vec;

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int T, C, D, N, a, b, c;
	init();
	cin>>T;
	string str;
	for(int tt = 1; tt <= T; ++tt){
		memset(com, -1, sizeof(com));
		memset(del, 0, sizeof(del));
		cin>>C;
		for(int i = 0; i < C; ++i){
			cin>>str;
			a = val[str[0]], b = val[str[1]], c = val[str[2]];
			com[a][b] = com[b][a] = c;
		}
		cin>>D;
		for(int i = 0; i < D; ++i){
			cin>>str;
			a = val[str[0]], b = val[str[1]];
			del[a][b] = del[b][a] = 1;
		}
		cin>>N>>str;
		vec.clear();
		memset(vis, 0, sizeof(vis));
		for(int i = 0; i < N; ++i){
			if(vec.empty()){
				vec.push_back(val[str[i]]);
				vis[val[str[i]]]++;
			}else {
				if(com[val[str[i]]][vec.back()] != -1){
				//	cout<<"vec.back() "<<vec.back()<<endl;
					vis[vec.back()]--;
					vec.back() = com[val[str[i]]][vec.back()];
				//	cout<<"vec.back() "<<vec.back()<<endl;
				}else {
					int flag = 0;
					for(int j = 0; j < 8; ++j){
						if(vis[j] && del[j][val[str[i]]])flag = 1;
					}
					if(flag){
						vec.clear();
				//		cout<<"vec.clear(), i = "<<i<<endl;
						memset(vis, 0, sizeof(vis));
					}else{
						vec.push_back(val[str[i]]);
						vis[val[str[i]]]++;
					}
				}
			}
		}
		//cout<<"vec.size()="<<vec.size()<<endl;
		cout<<"Case #"<<tt<<": [";
		if(!vec.empty()){
			for(int i = 0; i < vec.size() - 1; ++i){
				cout<<nval[vec[i]]<<", ";
			}
			cout<<nval[vec.back()];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

