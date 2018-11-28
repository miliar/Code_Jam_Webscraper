//Code by Patcas Csaba
//Time complexity:
//Space complexity:
//Method:
//Implementation time: 

#include <vector>
#include <string> 
#include <set> 
#include <map> 
#include <queue> 
#include <bitset> 
#include <stack>
#include <list>

#include <numeric> 
#include <algorithm> 

#include <cstdio>
#include <fstream>
#include <iostream> 
#include <sstream> 
#include <iomanip>

#include <cctype>
#include <cmath> 
#include <ctime>
#include <cassert>

using namespace std;

#define LL long long
#define PII pair <int, int>
#define VB vector <bool>
#define VI vector <int>
#define VD vector <double>
#define VS vector <string>
#define VPII vector <pair <int, int> >
#define VVI vector < VI >
#define VVB vector < VB >

#define FORN(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define FORI(it, X) for(__typeof((X).begin()) it = (X).begin(); it !=(X).end(); ++it) 
#define REPEAT do{ 
#define UNTIL(x) }while(!(x)); 

#define SZ size()
#define BG begin() 
#define EN end() 
#define CL clear()
#define X first
#define Y second
#define RS resize
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()

ofstream fout("output.txt");

int l, speed1, speed2, n, m;
double maxTime;
vector < pair <PII, int> > a;
VD b, speed;
map <int, int> sectionSpeed;

double Time()
{
	double ans = 0;
	FOR(i, 0, m - 2)
	{
		ans += (b[i + 1] - b[i]) / double (speed[i]);
	}
	return ans;
}

void Split(int index, int newSpeed, double firstTime)
{
	if (firstTime == b[index + 1] - b[index]) speed[index] = newSpeed;
	else
	{
		b.insert(b.BG + index + 1, b[index] + firstTime);
		speed.insert(speed.BG + index, newSpeed);
		++m;
	}
}

void Solve()
{
	map <int, int> sectionStart;
	FOR(i, 0, m - 2) sectionStart[b[i]] = i;

	while (maxTime > 0)
	{
		bool found = false;
		FOR(i, 0, m - 2)
			if (speed[i] == speed1)
			{
				double len = min(maxTime * speed2, double (b[i + 1] - b[i]));
				Split(i, speed2, len);
				if (len == b[i + 1] - b[i]) maxTime -= (b[i + 1] - b[i]) / double(speed2);
				else maxTime = 0;
				found = true;
				break;
			}
		if (!found) break;
	}

	if (maxTime > 0)
	{
		vector <PII> speeds;
		for(map <int, int> :: iterator it = sectionSpeed.BG; it != sectionSpeed.EN; ++it)
			speeds.PB(MP((*it).Y, (*it).X));
		sort(ALL(speeds));
		FORN(j, speeds.SZ)
		{
			int i = sectionStart[speeds[j].Y];
			//FOR(i, 0, m - 2)
			if (b[i] == speeds[j].Y)
			{
				double len = min(maxTime * (speed2 + sectionSpeed[b[i]]), double (b[i + 1] - b[i]));
				Split(i, speed2 + sectionSpeed[b[i]], len);
				if (len == b[i + 1] - b[i]) maxTime -= (b[i + 1] - b[i]) / double(speed2 + sectionSpeed[b[i]]);
				else maxTime = 0;
			}
			if (maxTime <= 0) break;
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	int test;
	cin >> test;
	FOR(t, 1, test)
	{
		cin >> l >> speed1 >> speed2 >> maxTime >> n;
		sectionSpeed.CL;
		a.CL;
		FORN(i, n)
		{
			int be, en, sp;
			cin >> be >> en >> sp;
			a.PB(MP(MP(be, en), sp));
			sectionSpeed[be] = sp;
		}
		b.CL, b.PB(0), b.PB(l);
		FORN(i, a.SZ) 
		{
			b.PB(a[i].X.X), b.PB(a[i].X.Y);
		}
		sort(ALL(b));
		b.RS(unique(ALL(b)) - b.BG);
		m = b.SZ;
		speed.RS(m - 1);
		FOR(i, 0, m - 2) 
			if (sectionSpeed.count(b[i])) speed[i] = sectionSpeed[b[i]] + speed1;
			else speed[i] = speed1;
		Solve();

		cout << t << " / " << test << endl;
		fout << "Case #" << t << ": " << setprecision(7) << fixed << Time() << endl;
	}
	return 0;
}