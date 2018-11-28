#ifndef __MYLIB_H
#define __MYLIB_H

#include<iostream>
#include<algorithm>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<utility>  // pair, make_pair
#include<cstdio>
#include<cmath>
#include<cstring>
#include<climits>
using namespace std;

#define all(vec)    vec.begin(),vec.end()
#define rall(vec)    vec.rbegin(),vec.rend()
#define sz(r)      r.size()
#define rem1(v, i)    (v.erase(v.begin()+i))
#define rem2(v, i, j)  (v.erase(v.begin()+i, v.begin()+j+1))
#define digits(i)    (int)((log(i)/log(10))+1)
#define dround(num)    (int)floor(num+0.5)  // Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define strtoint(str)    (extract_int(str)[0])

#define REP(i,n)     for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr)     for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define first_bit_index(num) __builtin_ctz(num) // count trailing zeros
#define last_bit_index(num)  __builtin_clz(num) // count leading zeros
#define UNDEFINED_BIT       32
#define test_bit(num, bit)   ((num & 1 << bit) != 0)
#define num_bits(num)       __builtin_popcount(num)

#define inf   INT_MAX
#define mn_inf  INT_MIN

typedef stringstream sstream;
typedef struct point{
  int x, y;
  point(){};
  point(int a, int b){x=a;y=b;}
}point;

int X[] = {0, 1, -1, 0, -1, 1, -1, 1};
int Y[] = {1, 0, 0, -1, -1, 1, 1, -1};


/**
 * Convert int to string
*/
string inttostr(int num)
{
  string res;
  sstream s;

  s << num; s >> res;
  return res;
}

/**
 * Extract int from string
*/
vector<int> extract_int(string str)
{
  sstream s;
  s << str;

  vector<int> res;
  int num = -1;

  while((s >> num))
    res.push_back(num);

  return res;
}

#endif 

/* End of my lib */

bool check(vector<string> grid, char c) {

	//cout << "check .." << endl;

	for(int i = 0; i < 4; i++) {
		int cntR = 0, cntC = 0;

		for(int j = 0; j < 4; j++) {
			if(grid[i][j] == c || grid[i][j] == 'T') cntR++;
			if(grid[j][i] == c || grid[j][i] == 'T') cntC++;
		}	

		if(cntR == 4 || cntC == 4) return true;
	}

	int cntL = 0, cntR = 0;
	for(int i = 0; i < 4; i++) {
		if(grid[i][i] == c || grid[i][i] == 'T') cntL++;
		if(grid[i][4-i-1] == c || grid[i][4-i-1] == 'T') cntR++;
	}

	if(cntR == 4 || cntL == 4) return true;

	return false;
}

bool check_empty_cell(vector<string> grid) {
	//cout << "check empty" << endl;

	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	if(grid[i][j] == '.') return true;

	return false;
}

int main() {
	int t;
	cin >> t;

	vector<string> grid(4);

	for(int i = 1; i <= t; i++) {
		for(int j = 0; j < 4; j++) cin >> grid[j];

		if(check(grid, 'X')) cout << "Case #" << i << ": X won";
		else if(check(grid, 'O')) cout << "Case #" << i << ": O won";
		else if(check_empty_cell(grid)) cout << "Case #" << i << ": Game has not completed";
		else cout << "Case #" << i << ": Draw";

		cout << endl;
	}
}

