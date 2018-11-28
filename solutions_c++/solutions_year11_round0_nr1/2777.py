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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

ifstream in;
ofstream out;
vector <int> oran;
vector <int> blue;
int ans;
void work();
int main()
{
	in.open("small.in");
	//in.open("large.in");
	out.open("small.out");
	//out.open("large.out");
	int tcnt, t;
	in>>t;
	for (int tcnt=0; tcnt<t; tcnt++) {
		out<<"Case #"<<tcnt+1<<": ";
		work();
		out<<ans<<endl;
	}
	return 0;
}
void work()
{
	oran.clear();
	blue.clear();
	ans = 0;
	int n, num;
	char ch;
	in>>n;
	int pos_oran = 1, pos_blue = 1, prev_time = 0, cur_time = 0;
	char prev_ch = '$';
	for (int i=0; i<n; i++) {
		in>>ch>>num;
		if (ch == 'O') {
			if (prev_ch == 'O') {
				cur_time = abs(num - pos_oran) + 1;
				ans += cur_time;
				prev_time += cur_time;
				pos_oran = num;
			} else {
				cur_time = abs(num - pos_oran) + 1;
				cur_time -= prev_time;
				if (cur_time <= 1) 
					cur_time = 1;
				prev_time = cur_time;
				pos_oran = num;
				prev_ch = 'O';
				ans += cur_time;
			}
		} else {
			cur_time = abs(num - pos_blue) + 1;
			if (prev_ch == 'O') {
				cur_time -= prev_time;
				if (cur_time <= 1)
					cur_time = 1;			
				prev_time = 0;
			}
			ans += cur_time;
			prev_time += cur_time;
			pos_blue = num;
			prev_ch = 'B';
		}
		cout<<ans<<endl;
	}
	
}
