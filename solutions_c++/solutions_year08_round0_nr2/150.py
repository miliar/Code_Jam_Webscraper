#include<iostream>
#include<algorithm>
#include<stdlib.h>
#include<string.h>


using namespace std;

struct Tent
{
	int time;
	int type, where;
	bool avi;
	
	const bool operator < (const Tent &s) const
	{
		if (time < s.time) return true;
		if (time > s.time) return false;
		return type>s.type;
	}
};

Tent e[1000];

int solve()
{
	int na, nb, n, m, a, b, i, t;
	char buf[100];
	
	cin >> t >> na >> nb;
	n = na+nb;
	
	m = 0;
	for (i=0; i<na; i++) {
		cin >> buf;
		a = atoi(buf)*60+atoi(buf+3);
		cin >> buf;
		b = atoi(buf)*60+atoi(buf+3)+t;
		e[m].time = a;
		e[m].type = 0;
		e[m].where = 0;
		e[m].avi = false;
		m++;
		e[m].time = b;
		e[m].type = 1;
		e[m].where = 1;
		e[m].avi = true;
		m++;
	}
	for (i=0; i<nb; i++) {
		cin >> buf;
		a = atoi(buf)*60+atoi(buf+3);
		cin >> buf;
		b = atoi(buf)*60+atoi(buf+3)+t;
		e[m].time = a;
		e[m].type = 0;
		e[m].where = 1;
		e[m].avi = false;
		m++;
		e[m].time = b;
		e[m].type = 1;
		e[m].where = 0;
		e[m].avi = true;
		m++;
	}
	
	if (m) sort(e, e+m);
	
	int ans[2];
	int now[2];
	ans[0]=ans[1]=now[0]=now[1]=0;
	for (i=0; i<m; i++) {
		if (e[i].type==0) {
			if (now[e[i].where]) now[e[i].where]--;
			else ans[e[i].where]++;
		}
		else {
			now[e[i].where]++;
		}
	}
	
	cout << ans[0] << " " << ans[1] << endl;
	
	return 0;
}

int main()
{
	int c, cc=0;
	cin >> c;
	while (c--) {
		cout << "Case #" << ++cc << ": ";
		solve();
	}
	return 0;
}
