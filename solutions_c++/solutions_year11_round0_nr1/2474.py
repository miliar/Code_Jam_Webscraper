#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
typedef pair<bool, int> PBI;
void print ( int kase ,  int yes )
{
 	 cout <<"Case #"<<kase<<": ";
	 cout<<yes;
	 cout <<"\n";
 	 return ;
}
vector <PBI> commands;
int simulate() {
	int ret = 0;
	int o = 1 , b = 1;
	for (int i = 0 ;i < commands.size(); i++) {
		PBI curr = commands[i];
		if (curr.first == 0) {
			int diff = abs(curr.second - o) + 1;
			ret += diff ;
			o = curr.second;
			for (int j = i + 1 ; j < commands.size(); j++) if (commands [j].first == 1) {
				if ( abs(commands[j].second - b) > diff ) {
					if ( commands[j].second > b ) b += diff;
					else b -= diff;
				}
				else b  = commands[j].second;
				break;
			}
		}
		else {
			int diff = abs(curr.second - b) + 1;
			ret += diff ;
			b = curr.second;
			for (int j = i + 1 ; j < commands.size(); j++) if (commands [j].first == 0) {
				if ( abs(commands[j].second - o) > diff ) {
					if ( commands[j].second > o ) o += diff;
					else o -= diff;
				}
				else o  = commands[j].second;
				break;
			}
		}
	}
	return ret;
}
int main ()
{
 	freopen ("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- ) {
		int N; cin >> N;
		commands.clear();
		for (int i = 0; i < N; i++) {
			string color; int button;
			cin >> color >> button;
			if (color [0] == 'O') commands.push_back(make_pair(0,button));
			else commands.push_back(make_pair(1,button));
		}
		print(++kase, simulate());
		
	}
	return 0;
}
