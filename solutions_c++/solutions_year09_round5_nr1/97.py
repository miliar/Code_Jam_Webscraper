#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

#define valid(r,c) ((r) >= 0 && (r) < R && (c) >= 0 && (c) < C)
int dir[4][2] = {{-1,0}, {0, 1}, {1, 0}, {0, -1}};	//four connected clockwise

#define state pair<int, vector<pair<int, int> > >

set<state> table;
int R, C;
string grid[100];

state goal, start;

bool vis[10];
bool connected(vector<pair<int, int> >& v){

	vector<int> c;
	memset(vis, 0, sizeof vis);
	c.push_back(0);
	vis[0] = true;
	for(int i = 0 ; i < c.size() ; i++){
		int idx1 = c[i];
		for(int j = 0 ; j < v.size() ; j++){
			if(vis[j])continue;
			int idx2 = j;
			if(abs(v[idx1].first-v[idx2].first) + abs(v[idx1].second-v[idx2].second) == 1){
				vis[j] = true;
				c.push_back(j);
			}
		}
	}

	return c.size() == v.size();
}

void print(vector<pair<int, int> >& v){
	for(int i = 0 ; i <v.size() ; i++)
		cout << v[i].first << "," << v[i].second << " ";
	cout << endl << endl;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		start.first = goal.first = 1;
		goal.second.clear();
		start.second.clear();
		table.clear();

		cin >> R >> C;
		for(int i = 0 ; i < R ; i++){
			cin >> grid[i];
			for(int j = 0 ; j < C ; j++){
				if(grid[i][j] == 'o')
					start.second.push_back(make_pair(i, j));
				else if (grid[i][j] == 'x')
					goal.second.push_back(make_pair(i, j));
				else if(grid[i][j] == 'w'){
					start.second.push_back(make_pair(i, j));
					goal.second.push_back(make_pair(i, j));
				}
			}
		}
		sort(start.second.begin(), start.second.end());
		sort(goal.second.begin(), goal.second.end());

		queue<state> q;
		if((table.insert(start)).second)
			q.push(start);

		int best = -1, level = 0;
		while(!q.empty()){
			int s = q.size();
			for(int ss = 0 ; ss < s ; ss++){
				state st = q.front(); q.pop();

				//print(st.second);

				if(st == goal){
					best = level;
					goto done;
				}

				//move
				for(int i = 0 ; i < (int)st.second.size() ; i++){
					for(int d = 0 ; d < 4 ; d++){
						int r[2], c[2];
						r[0] = st.second[i].first+dir[d][0];
						c[0] = st.second[i].second+dir[d][1];

						r[1] = st.second[i].first+dir[(d+2)%4][0];
						c[1] = st.second[i].second+dir[(d+2)%4][1];

						int b;
						for(b = 0 ; b < 2;  b++){
							if(!valid(r[b], c[b]) || grid[r[b]][c[b]] == '#')
								break;
							if(find(st.second.begin(), st.second.end(), make_pair(r[b], c[b])) != st.second.end())
								break;
						}
						if(b < 2)
							continue;

						state ns = st;
						ns.second[i] = make_pair(r[0], c[0]);
						ns.first = connected(ns.second);

						//print(ns.second);

						if(!st.first && !ns.first)
							continue;

						sort(ns.second.begin(), ns.second.end());
						if((table.insert(ns)).second)
							q.push(ns);
					}
				}
			}
			level++;
		}
done:
		cout << "Case #" << t+1 << ": " << best << endl;
	}

	return 0;
}
