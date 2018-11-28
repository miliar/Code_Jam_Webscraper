#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back

using namespace std;

vector<char> bot;
vector<int> dir;

int myabs(int x)	{
	return x < 0 ? -x : x;
}

void solve(int z)	{

	int op = 1;
	int bp = 1;
	int t = 0;
	int othave = 0, bthave = 0;
	
	forp(0,bot.size(),i)	{
		
		char c = bot[i];
		int d = dir[i];
		
		if (c == 'O')	{
			int tneed = myabs(d - op) - othave;
			tneed = tneed > 0 ? tneed : 0;
			tneed++;
			t += tneed;
			
			othave = othave - myabs(d-op) - 1;
			othave = othave > 0 ? othave : 0;
			othave = 0;
			
			bthave += tneed;
			
			op = d;
		} else	{
			int tneed = myabs(d - bp) - bthave;
			tneed = tneed > 0 ? tneed : 0;
			tneed++;
			t += tneed;
			
			bthave = bthave - myabs(d-bp) - 1;
			bthave = bthave > 0 ? bthave : 0;
			bthave = 0;
			
			othave += tneed;
			
			bp = d;
		}
		
// 		cout << "op " << op << " bp " << bp << " t " << t << " ohave " << othave << " bhave " << bthave << endl;
	}
	
	cout << "Case #" << z << ": " << t << endl;
}

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
	
		bot.clear();
		dir.clear();
		int n;
		cin >> n;
		forp(0,n,i)	{
		
			char c;
			int d;
			cin >> ws >> c >> ws >> d;
			bot.pb(c);
			dir.pb(d);
		}
		
		solve(z+1);
	}
}