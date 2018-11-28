#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>


using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repd(i,n,m) for(int i=n;i<(int)(m);i++)
#define repvi(v,i) for(vector<int>::iterator i = v.begin(); i < v.end();i++)
#define repvs(v,i) for(vector<string>::iterator i = v.begin(); i < v.end();i++)

int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int cases, numberOfButtons, button;
	char robot;	
	cin >> cases;

	repd(nn, 1, cases+1) {
		cout << "Case #" << nn << ": ";
		cin >> numberOfButtons;
		vector< pair<char,int> > plan;
		rep(i, numberOfButtons) {
			cin >> robot >> button;
			plan.push_back(make_pair(robot,button));
		}

		int Oposition = 1, Bposition = 1, Otime = 0, Btime = 0, timeNeed, timediff;
		rep(i, numberOfButtons) {
			robot = plan[i].first;
			button = plan[i].second;
			if (robot == 'O') {
				timeNeed = fabs(Oposition - button) + 1;
				if (Otime >= Btime) {
					Otime += timeNeed;
				} else {
						timediff = Btime - Otime;
						if (timediff >= timeNeed)
							Otime = Btime + 1;
						else
							Otime += timeNeed;
				}
				Oposition = button;
			} else {
				timeNeed = fabs(Bposition - button) + 1;
				if (Btime >= Otime){
					Btime += timeNeed;
				}else {
					timediff = Otime - Btime;
					if (timediff >= timeNeed){
						Btime = Otime + 1;
					}else
						Btime += timeNeed;
				}
				Bposition = button;
			}
		}
		if (Btime >= Otime)
			cout << Btime << endl;
		else
			cout << Otime << endl;

	}
	
	return 0;
}
