#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;

class Mission{
public:
	Mission(char c ,int d ){
		robot=c;
		desty=d;
	}
	char robot;
	int desty;
};

/*
 The first line of the input gives the number of test cases, T. T test cases follow.
 
 Each test case consists of a single line beginning with a positive integer N, 
 representing the number of buttons that need to be pressed. This is followed by N terms of 
 the form "Ri Pi" where Ri is a robot color (always 'O' or 'B'), and Pi is a button position. 
 */

int T;
int now[2];
bool pressed[2][101];

int main(){
	
	cin>>T;
	for (int testcase=1; testcase<=T; ++testcase) {
		queue<Mission> missions;
		vector< queue<Mission> > two_mission;
		two_mission.push_back( queue<Mission>() );
		two_mission.push_back( queue<Mission>() );
		
		now[0]=now[1]=1;
		memset(pressed,false,sizeof(pressed));
		
		int N;
		cin>>N;
		for (int i=0; i<N; ++i ) {
			char _t;
			int _d;
			cin>>_t>>_d;
			missions.push(Mission(_t,_d));
			if (_t=='O') {
				two_mission[0].push(Mission(_t,_d));
			}else {
				two_mission[1].push(Mission(_t,_d));
			}

		}
		
		ull times=0;
		
		while (!missions.empty()) {
			int _robot;
			Mission current = missions.front();
			_robot = (current.robot=='O'? 0:1);
			
			if (now[_robot]==current.desty) {
				pressed[_robot][current.desty]=true;
				missions.pop();
				two_mission[_robot].pop();
				
			}else {
				if (now[_robot]>current.desty) now[_robot]--;
				else						   now[_robot]++;
			}
			
			int _another = (_robot+1)%2;
			if ( now[_another]!=two_mission[_another].front().desty) {
				if (two_mission[_another].front().desty>now[_another]) {
					now[_another]++;
				}else {
					now[_another]--;
				}
			}
			
			times++;
		}
		cout << "Case #"<<testcase<<": "<<times<<endl;
	}
	return 0;
}
