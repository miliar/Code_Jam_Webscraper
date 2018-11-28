#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

#define BLUE 0
#define ORANGE 1

typedef pair<int, int> movement_t;

void move(
	vector<movement_t> &movements_blue, 
	vector<movement_t> &movements_orange, 
	int &pos_blue, 
	int &pos_orange,
	int &m_blue,
	int &m_orange,
	int &time
){
		
	int time_delta = abs(movements_blue[m_blue].second - pos_blue) + 1;
	time += time_delta;
	pos_blue = movements_blue[m_blue].second;
	
	if (m_orange < movements_orange.size()){
		int amount = min(time_delta, abs(movements_orange[m_orange].second - pos_orange));
		//WATCH(amount);
		int direction = movements_orange[m_orange].second > pos_orange ? +1 : -1; 
		pos_orange +=	direction*amount;
	}

	m_blue++;

}

int solve(vector<movement_t> &movements_blue, vector<movement_t> &movements_orange){
	
	WRITE("SOLVE");

	int time = 0;
	int m_orange = 0;
	int m_blue = 0;
	int pos_orange = 1;
	int pos_blue = 1;
	
	while(true){
		if ( m_blue < movements_blue.size() and (m_orange >= movements_orange.size() or
			movements_blue[m_blue].first < movements_orange[m_orange].first)){ //blue is next
			
			WRITE("BLUE PRESSES");
			move(movements_blue, movements_orange, pos_blue, pos_orange, m_blue, m_orange, time);

		} else if (m_orange < movements_orange.size() and (m_blue >= movements_blue.size() or 
			movements_blue[m_blue].first > movements_orange[m_orange].first)){ // orange is next

			WRITE("ORANGE PRESSES");
			move(movements_orange, movements_blue, pos_orange, pos_blue, m_orange, m_blue, time);
				
		} else {
			break;
		}

		WATCH(pos_blue);
		WATCH(m_blue);
		WATCH(pos_orange);
		WATCH(m_orange);
		WATCH(time);
		WRITE("");
	}

	return time;
}


int main(){
	//Descomente para acelerar cin
	ios::sync_with_stdio(false);

	int n;
	cin >> n;
	int tcount = 0;
	FORN(i, 0, n){
		vector<movement_t > movements_orange;
		vector<movement_t > movements_blue;
		int m;
		cin >> m;
		FORN(j, 0, m){
			string color; 
			int button;
			cin >> color >> button;
			movement_t movement = make_pair(j, button);
			if (color == "B"){
				movements_blue.push_back(movement);
			} else {
				movements_orange.push_back(movement);
			}
		}

		int ans = solve(movements_blue, movements_orange);
		cout << "Case #" << ++tcount << ": " << ans << endl;
	}

	
}
