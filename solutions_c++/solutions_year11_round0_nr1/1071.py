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

const int SIZE = 110;
int type[SIZE], pos[SIZE], N;

struct state{
	int p[2], idx;
};
bool vis[SIZE][SIZE][SIZE];

bool valid(int x, int y){
	return x >= 1 && x <= 100 && y >= 1 && y <= 100;
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
		cerr << "Solving testcase " << t+1 << endl;

		cin >> N;
		for(int i = 0 ; i < N ; i++){
			char ch; cin >> ch >> pos[i];
			type[i] = ch == 'B';
		}

		memset(vis, 0, sizeof vis);

		queue<state> q;
		state start = {1, 1, 0};
		q.push(start);
		vis[start.p[0]][start.p[1]][start.idx] = true;

		int s = 0;
		while(!q.empty()){

			int x = q.size();
			for(int y = 0 ; y < x ; y++){
				state current = q.front(); q.pop();
				if(current.idx >= N)
					goto done;

//				if(current.p[0] ==4 && current.p[1] == 2 && current.idx == 4){
//					int m = 0 ;
//					m++;
//				}

				for(int i = -2 ; i <= 1 ; i++){
					if(i == -2 && (type[current.idx] != 0 || current.p[0] != pos[current.idx]))
						continue;

					for(int j = -2 ; j <= 1 ; j++){
						if(j == -2 && (type[current.idx] != 1 || current.p[1] != pos[current.idx]))
							continue;

						state ns = {i==-2?current.p[0]:current.p[0]+i, j==-2?current.p[1]:current.p[1]+j, current.idx};
						if(i == -2 || j == -2)
							ns.idx++;

						if(!valid(ns.p[0], ns.p[1]))
							continue;
						if(!vis[ns.p[0]][ns.p[1]][ns.idx]){
							vis[ns.p[0]][ns.p[1]][ns.idx] = true;
							q.push(ns);
						}
					}
				}
			}

			s++;
		}
done:
		cout << "Case #" << t+1 << ": " << s << endl;
	}

	return 0;
}
