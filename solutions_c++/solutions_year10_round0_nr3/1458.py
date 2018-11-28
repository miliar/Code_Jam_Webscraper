#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>

// #define DEBUG

using namespace std;

/*************************************************/
// BEGIN UTILITY CODE
typedef unsigned char byte;
typedef long long int64;

const double E6 = .000001;
const double E9 = .000000001;

void _print(string& lead, string& str) {cout<<lead<<'\"'<<str<<'\"'<<endl;} 
void _print(const char* lead, string& str) {cout<<lead<<'\"'<<str<<'\"'<<endl;} 
template<class T> string toString(T x){ostringstream oss; oss<<x; return oss.str();}

bool _isUpperCase(char c){return 'A' <= c && c <= 'Z';}
bool _isLowerCase(char c){return 'a' <= c && c <= 'z';}
bool _isAlpha(char c){return _isUpperCase(c) || _isLowerCase(c);}
bool _isNum(char c){return '0' <= c && c <= '9';}

char _toLower(char c){if(_isUpperCase(c)) return c + 'a' - 'A'; else return c;}
void _toLower(string& s){for(int i = 0; i < s.size(); i++) s[i] = _toLower(s[i]);}
char _toUpper(char c){if(_isLowerCase(c)) return c + 'A' - 'a'; else return c;}
void _toUpper(string& s){for(int i = 0; i < s.size(); i++) s[i] = _toUpper(s[i]);}
void _flush(){if(cin.peek()=='\n') cin.ignore(1,'\n');}

template<class T> void _print(const vector<T>& v){for(int i = 0; i < v.size(); i++)cout<<i<<" "<<v[i]<<endl;}


// END UTILITY CODE
/*************************************************/

int main() 
{
	int T;
	cin>>T;
	
	for(int i = 0; i < T; i++)
	{
		int R, k, N;
		cin>>R>>k>>N;
		vector<int> g(N);
		
		for(int j = 0; j < N; j++)
			cin>>g[j];
		
		// <total rode, next queue head>
		vector< pair<int, int> > one_step(N);
		
		// precalculate how many ride for each head of queue group j
		for(int start = 0; start < N; start++)
		{
			int total = 0;
			int space_left = k;
			int curr = start;
			while(space_left >= g[curr])
			{
				total += g[curr];
				space_left -= g[curr];
				curr++;
				curr %= N;
				if(curr == start) break;
			}
			
			one_step[start].first = total;
			one_step[start].second = curr;
		}
		
		
		long long total = 0;
			
		// brute force it
		if( R <= N)
		{
			int head = 0;
			for(int j = 0; j < R; j++)
			{
				total += (long long) one_step[head].first;
				head = one_step[head].second;
			}
		}
		
		// find a cycle
		set<int> ids;
		int curr_id = 0;
		ids.insert(curr_id);
		int cycle_start = 0;
		while(true)
		{
			curr_id = one_step[curr_id].second;
			if( ! ids.insert(curr_id).second )
			{
				cycle_start = curr_id;
				break;
			}	
		}
		
		// a cycle exists starting at cycle_start
		long long cycle_cost = 0;
		int cycle_length = 0;
		
		int id = cycle_start;
		do
		{
			cycle_length++;
			cycle_cost += one_step[id].first;
			id = one_step[id].second;
		}while(id != cycle_start);
		
		// how many steps to reach cycle_start from 0
		long long prefix_cost = 0;
		int prefix_length = 0;
		id = 0;
		while(id != cycle_start)
		{
			prefix_length++;
			prefix_cost += one_step[id].first;
			id = one_step[id].second;
		}
		
		
		// now it is just addition
		int trips_left = R - prefix_length;
		total = prefix_cost;
		
		int num_tours = trips_left / cycle_length;
		int remainder = trips_left % cycle_length;
		total += num_tours * cycle_cost;
		
		// brute force remainder
		id = cycle_start;
		for(int j = 0; j < remainder; j++)
		{
			total += (long long) one_step[id].first;
			id = one_step[id].second;
		}
		
		cout<<"Case #"<<i+1<<": "<<total<<endl;
	}
	
	
	return 0;
}
