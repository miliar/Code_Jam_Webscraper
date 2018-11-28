#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

int n,t,na,nb;
int sa[1500],sb[1500];

int parse(string time) {
	int hours,mins;
	sscanf(time.c_str(),"%d:%d",&hours,&mins);
	return hours*60+mins;
}

int ans(int trips[]) {
	int added = 0;
	int stock = 0;
	for(int i=0;i<1440;i++) {
		if (trips[i]<0) {
			if (stock>0) {
				int diff = stock - (-1*trips[i]);
				if (diff<0) {
					stock = 0;
					added += -1*diff;
				} else {
					stock += trips[i];
				}
			} else {
				added += -1*trips[i];
			}
		} else {
			stock += trips[i];
		}
	}
	return added;
}

int main() {
	cin >> n;
	for(int i=1;i<=n;i++) {
		cin >> t;
		cin >> na >> nb;
		for(int k=0;k<1440;k++) {
			sa[k] = 0; sb[k] = 0;
		}
		for(int k=0;k<na;k++) {
			string start,end;
			cin >> start >> end;
			int time = parse(start);
			sa[time]--;
			time = parse(end) + t;
			sb[time]++;
		}
		for(int k=0;k<nb;k++) {
			string start,end;
			cin >> start >> end;
			int time = parse(start);
			sb[time]--;
			time = parse(end) + t;
			sa[time]++;
		}
		cout << "Case #" << i << ": " << ans(sa) << " " << ans(sb) << endl;
	}
	return 0;
}
