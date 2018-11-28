//Arash Rouhani

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>

using namespace std;

typedef pair < int, int > II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC> VVC;
typedef long long  LL;
#define all(c) c.begin(), c.end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)

VII directions;
VVI map;
char basin;
int h, w;
VVC charmap;

II flows_to(II coord){
	II bestans = coord;
	int bestalt = map[coord.first][coord.second];
	tr(directions, d){
		II cc = II(max(min(d->first + coord.first,h-1),0), max(min(d->second + coord.second, w-1),0));
		if(map[cc.first][cc.second] < bestalt){
			bestans = cc;
			bestalt = map[cc.first][cc.second];
		}
	}
	return bestans;
}

void dfs(II coord){
	int y0=coord.first, x0 = coord.second;
	if(charmap[y0][x0]<basin){
		charmap[y0][x0]=basin;
		dfs(flows_to(coord));
		tr(directions, d){
			II cc = II(max(min(d->first + coord.first,h-1),0), max(min(d->second + coord.second, w-1),0));
			if(coord == flows_to(cc)){
				dfs(cc);
			}
		}
	}//otherwise already visited
}

int main(){
	directions.push_back(II(-1,0));
	directions.push_back(II(0,-1));
	directions.push_back(II(0,1));
	directions.push_back(II(1,0));

	int ntestcases;
	cin >> ntestcases;
	sfor(int, i, 1, ntestcases+1){
		cin >> h >> w;
		map.clear();
		map.resize(h, VI(w));
		tr(map, row)
			tr(*row, cell)
				cin >> *cell;
		charmap.clear();
		charmap.resize(h, VC(w, 0));
		basin='a';
		sfor(int, y, 0, h){
			sfor(int, x, 0, w){
				if(charmap[y][x]==0){
					dfs(II(y,x));
					basin++;
				}
			}
		}
		cout << "Case #" << i << ":\n";
		tr(charmap, row){
			tr(*row, column){
				cout << *column << " ";
			}
			cout << endl;
		}
	}
}
