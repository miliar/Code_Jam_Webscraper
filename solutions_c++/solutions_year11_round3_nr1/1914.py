#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<string> vecstr;
typedef vecstr::size_type mysize;


bool tryputred(vecstr&pic,mysize r,mysize c)
{
	if(r+1 == pic.size() || c+1 == pic[r].size()
		||pic[r+1][c] != '#'
		||pic[r][c+1] != '#'
		||pic[r+1][c+1] != '#' )
		return false;
	pic[r][c] = pic[r+1][c+1] = '/';
	pic[r+1][c] = pic[r][c+1] = '\\';
	return true;
}

bool transformpic( vecstr & pic )
{
	mysize r, c;
	for( r = 0; r < pic.size(); ++r )
		for( c = 0; c < pic[r].size(); ++c )
			if( pic[r][c] == '#' )
				if( !tryputred(pic,r,c) )
					return false;
	return true;
}

void solve()
{
	int rcnt, ccnt;
	cin >> rcnt >> ccnt;
	vecstr pic(rcnt);
	int r;
	for( r = 0; r < rcnt; ++r ) {
		cin >> pic[r];
	}
	if(transformpic(pic))
	{
		for( r = 0; r < rcnt; ++r )
			cout << pic[r] << endl;
	}
	else
		cout << "Impossible" << endl;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tcnt;
	cin >> tcnt;
	for( int t = 1; t <= tcnt; ++t )
	{
		cout << "Case #" << t << ":" << endl;
		solve();
	}
	return 0;
}