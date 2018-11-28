#include <cstdio>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm> 

using namespace std;

#define forn(x,y) for(int x=0;x<y;x++)
#define mp make_pair 
#define pb pushback
#define inf 0x7f7f7f7f

typedef long long i64;

int n;
string s[4];

int check()
{
	int isend=1;
	forn(i,4)
	{
		int xw=1;
		int ow=1;
		forn(j,4)
		{
			//printf("before: %d ",xw);
			if (s[i][j]!='X'&&s[i][j]!='T')
				xw=0;
			//printf("s[i][j]=%c cond:%d  after:%d\n",s[i][j],(s[i][j]!='X'&&s[i][j]!='T'),xw);
			if (s[j][i]!='O'&&s[j][i]!='T')
				ow=0;
			
			if (s[i][j]=='.'||s[j][i]=='.')
				isend=0;

		}
		if (xw)	return 1;
		if (ow)	return 2;
	}
	
	//cerr << endl;

	forn(i,4)
	{
		int xw=1;
		int ow=1;
		forn(j,4)
		{
			if (s[i][j]!='O'&&s[i][j]!='T')
				ow=0;
			if (s[j][i]!='X'&&s[j][i]!='T')
				xw=0;
                  				
		}
		if (xw)	return 1;
		if (ow)	return 2;
	}


	int xw=1;
	int ow=1;
	forn(i,4)
	{
		
			if (s[i][i]!='O'&&s[i][i]!='T')
				ow=0;
			if (s[i][i]!='X'&&s[i][i]!='T')
				xw=0;
        
	}
	if (xw)	return 1;
	if (ow)	return 2;

	xw=1;
	ow=1;
	forn(i,4)
	{
		
			if (s[i][3-i]!='O'&&s[i][3-i]!='T')
				ow=0;
			if (s[i][3-i]!='X'&&s[i][3-i]!='T')
				xw=0;
        
	}
	if (xw)	return 1;
	if (ow)	return 2;

	if (isend)
		return 3;
	else 
		return 0;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("z.out","wt",stdout);
	cin >> n;
	getline(cin,s[0]);
	forn(i,n)
	{
		
		forn(j,4)
		{
			getline(cin,s[j]);
			//cerr << s[j] << endl;
		}
		switch(check())
		{
			case 0: printf("Case #%d: Game has not completed\n",i+1); break;
			case 1: printf("Case #%d: X won\n",i+1); break;
			case 2: printf("Case #%d: O won\n",i+1); break;
			case 3: printf("Case #%d: Draw\n",i+1); break;
		}
		//cerr << "\n";
		getline(cin,s[0]);
	}
	return 0;
}
