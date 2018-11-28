#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int N;
vector<pair<char, int>> buttons;

void readCase()
{
	scanf("%d", &N);
	buttons.clear();
	for(int i = 1; i <= N; i++) 
	{
		char color;
		int button;
		scanf(" %c %d", &color, &button);
		buttons.push_back(make_pair(color, button));
	}
}

void solve()
{
	int opos = 1, bpos = 1;
	int omove = 0, bmove = 0, cmove = 0;
	for(int i = 0; i < buttons.size(); i++)
	{
		char color = buttons[i].first;
		char button = buttons[i].second;
		if(color == 'O')	
		{
			omove = omove + abs(button - opos);
			opos = button;
			cmove = omove = max(omove, cmove) + 1;			
		} else {
			bmove = bmove + abs(button - bpos);
			bpos = button;
			cmove = bmove = max(bmove, cmove) + 1;
		}
	}
		
	printf("%d", cmove);
}

int main()
{
	//string fname = "./test/A-example.in";
	string fname = "./test/A-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int N;
	scanf("%d", &N);
	for(int tCase = 1; tCase <= N; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
	}
	return 0;
}

