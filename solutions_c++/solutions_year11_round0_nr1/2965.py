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


typedef vector<pair<int, int> > VP;
VP ora, blue;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n, m;
	char ch;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n;
		ora.clear();
		blue.clear();
		for(int i = 0; i < n; ++i){
			cin>>ch>>m;
			if(ch == 'O'){
				ora.push_back(make_pair(m, i));
			}else {
				blue.push_back(make_pair(m, i));
			}
		}
		int p1, p2, sum, pos1, pos2;
		p1 = p2 = 0;
		pos1 = pos2 = 1;
		sum = 0;
		while(p1 < ora.size() && p2 < blue.size()){
			int t1 = abs(ora[p1].first - pos1);
			int t2 = abs(blue[p2].first - pos2);
			if(ora[p1].second < blue[p2].second){
				sum += t1 + 1;
				if(t1 + 1 < t2){
					if(blue[p2].first < pos2){
						pos2 -= t1 + 1;
					}else {
						pos2 += t1 + 1;
					}	
				}else {
					pos2 = blue[p2].first;
				}
				pos1 = ora[p1++].first;
			}else {
				sum += t2 + 1;
				if(t2 + 1 < t1){
					if(ora[p1].first < pos1){
						pos1 -= t2 + 1;
					}else {
						pos1 += t2 + 1;
					}
				}else {
					pos1 = ora[p1].first;
				}
				pos2 = blue[p2++].first;
			}
		}
		while(p1 < ora.size()){
			sum += abs(pos1 - ora[p1].first) + 1;
			pos1 = ora[p1++].first;
		}
		while(p2 < blue.size()){
			sum += abs(pos2 - blue[p2].first) + 1;
			pos2 = blue[p2++].first;
		}
		cout<<"Case #"<<tt<<": "<<sum<<endl;
	}
	return 0;
}
					
					
			
		
