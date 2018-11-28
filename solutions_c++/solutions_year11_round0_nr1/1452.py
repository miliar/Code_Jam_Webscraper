#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int NUMBER_OF_ROBOTS = 2;
typedef long long int LL;
int main() {
    ios_base::sync_with_stdio(false);
    int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
	    int ans = 0;
	    int first_robot_name = 'O';
	    int actual_time = 0;
	    vector<int> robot_time(NUMBER_OF_ROBOTS, 0);
	    vector<int> robot_position(NUMBER_OF_ROBOTS, 1);
	    int n;
	    cin >> n;
	    for(int i = 0; i < n; ++i) {
	        char robot_name;
	        int pos;
	        cin >> robot_name >> pos;
	        if(robot_name != first_robot_name) {
	            first_robot_name = robot_name;
	            swap(robot_time[0], robot_time[1]);
	            swap(robot_position[0], robot_position[1]);
	        }
	        actual_time = max(actual_time, robot_time[0] + abs(robot_position[0] - pos)) + 1;
	        robot_time[0] = actual_time;
	        robot_position[0] = pos;
	    }
	    ans = actual_time;
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
/*
2
2
 1
2 3
 4
*/
