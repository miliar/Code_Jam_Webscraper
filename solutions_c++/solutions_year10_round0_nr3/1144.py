#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
vector <int> g;
vector <int> roundstart;
vector <int> roundincome;

int repeat(int j)
{
	int i;
	for (i = 0; i < roundstart.size(); i ++){
		if (roundstart[i] == j)
			return i;
	}
	return -1;
}	
int once(int repeat)
{
	int i;
	int sum = 0;
	for (i = 0; i < repeat; i ++){
		sum += roundincome[i];
	}
	return sum;
}

int several(int repeat)
{
	int i;
	int sum = 0;
	for (i = repeat; i < roundstart.size(); i ++){
		sum += roundincome[i];
	}
	return sum;
}

int rest(int repeat, int restround)
{
	int i;
	int sum = 0;
	for (i = repeat; i < repeat + restround; i ++){
		sum += roundincome[i];
	}
	return sum;
}

int main()
{
	ifstream fin ("C-small-attempt3.in");
//	ifstream fin ("test.txt");
	ofstream fout ("out.txt");
	int i, j, t;
	int r, n, k;
	int repeat_pos;
	int gi, cap, sum;
	int total;
	fin >> t;
	for ( i = 0; i < t; i++ ){
		fin >> r >> k >> n;
		total = 0;
		roundstart.clear();
		roundincome.clear();
		g.clear();
		sum = 0;
		for ( j = 0; j < n; j++){
			fin >> gi;
			total += gi;
			g.push_back(gi);
		}
		fout << "Case #" << i + 1 << ": ";
		if ( total <= k ){
			sum = total * r;
			cout << total << " " << k << endl;
		}
		else {
			cap = 0;
			j = 0;
			while ( (repeat_pos = repeat(j)) == -1 ){
				cap = 0;
				roundstart.push_back(j);
				while ( cap + g[j] <= k ){
					cout << g[j] << " ";
					cap += g[j];
					j++;
					j = j % n;
				}
				cout << ": "<< cap << endl;
				cout << endl;
				roundincome.push_back(cap);
			}
			cout << repeat_pos << endl;
			cout << (r - repeat_pos) / (roundstart.size() - repeat_pos) << endl;
			sum = once(repeat_pos) + (r - repeat_pos) / (roundstart.size() - repeat_pos) * several(repeat_pos) + rest(repeat_pos, (r - repeat_pos) % (roundstart.size() - repeat_pos));
		}
		cout << sum << endl;
		fout << sum << endl;
		
	}
	return 0;
}