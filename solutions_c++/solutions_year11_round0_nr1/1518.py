#include <iostream>
//#include <cstdio>
//#include <cmath>
using namespace std;

inline int min(int x, int y)
{
	return x<y?x:y;
}
inline int max(int x, int y)
{
	return x>y?x:y;
}
inline int abs(int x)
{
	return x<0?-x:x;
}

int compute()
{
	int n;
	cin >> n;
	int sec = 0;
	int o, b;
	o=b=1; //robo position
	char x;
	int y;
	int lastbtime = 0;
	int lastotime = 0;
	char lastx = ' ';
	for(int i=0;i<n;i++)
	{
		cin >> x >> y;
		int t;
		//cerr << x << y << endl;
		if(x=='O')
		{
			if(lastx=='B')lastotime=0;
			//lastotime += abs(o-y) + 1;
			//t = min(abs(o-y), max(0, abs(o-y) - lastbtime));
			t = max(0, abs(o-y) - lastbtime);
			lastbtime = 0;
			t++;
			//cout << "  " << t << " lb" << lastbtime << " lo" << lastotime << endl;
			//if(t<=0) t=0;
			lastotime += t;
			sec += t;// + 1;
			o=y;
		}
		else if(x=='B') //B
		{
			if(lastx=='O')lastbtime=0;
			//lastbtime += abs(b-y) + 1;
			//t = min(abs(b-y), max(0, abs(b-y) - lastotime));
			t = max(0, abs(b-y) - lastotime);
			lastotime = 0;
			t++;
			//cout << "  " << t << " lb" << lastbtime << " lo" << lastotime << endl;
			//if(t<=0) t=0;
			lastbtime += t;
			sec += t;// + 1;
			b=y;
		}
		lastx = x;
	}
	return sec;
}

int main()
{
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++)
		cout << "Case #" << i+1 << ": " << compute() << endl;
}
