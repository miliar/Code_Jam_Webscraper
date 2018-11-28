#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstring>
#include <cmath>
#include <utility>
#include <map>
#define inf 1000111222
#define  mp make_pair
#define chen insert
#define xoa erase
#define ii pair <int, int>
#define ss second
#define ff first

using namespace std;

char s[5][5];
int s1x[5], s2x[5], s1o[5], s2o[5];

int xuli()
{
	int kt = 0;
	int c1x=0;
	int c2x=0;
	int c1o=0;
	int c2o=0;
	int sl=0;
	for (int i=0; i<5; i++) {
		s1x[i]=0;
		s2x[i]=0;
		s1o[i]=0;
		s2o[i]=0;
	}
	for ( int i=0; i<4; i++)
		for ( int j=0; j<4; j++)
		{
			if ( s[i][j] == '.' ) sl++;
			if ( s[i][j] == 'X' || s[i][j] == 'T' ) {				
				s1x[i]++;
				s2x[j]++;
			}
			else if ( s[i][j] == 'O' || s[i][j] == 'T' ) {				
				s1o[i]++;
				s2o[j]++;
			}
		}
	
	for (int i=0; i<=4; i++)	
	{
		if ( s[i][i] == 'X' || s[i][i]=='T') c1x++;
		if ( s[i][i] =='O' || s[i][i] =='T') c1o++;
		if ( s[i][3-i] == 'X' || s[i][3-i] =='T') c2x++;
		if ( s[i][3-i] == 'O' || s[i][3-i] =='T') c2o++;
	}	
	
	if ( c1x == 4 || c2x == 4 ) return 1;
	if ( c1o == 4 || c2o == 4 ) return -1;	
	for (int i=0; i<5; i++) {
		if ( s1x[i]==4 || s2x[i]==4 ) return 1;
		if ( s1o[i]==4 || s2o[i]==4 ) return -1;		
	}
	if ( sl ) return -2;
	return 0;
}

int main ()
{
	int t;
	//freopen("test.inp","r",stdin);
	//freopen("test.out","w",stdout);
	scanf("%d ",&t);
	for (int o=1; o<=t; o++) {
		printf("Case #%d: ",o);
		for ( int i=0; i<4; i++) {
			gets(s[i]);			
		}
		int k = xuli();
		if ( k == 1 ) cout << "X won";
		else if ( k == 0 ) cout << "Draw";
		else if ( k == -1 ) cout << "O won";
		else if ( k == -2 ) cout << "Game has not completed";
		cout << endl;
		gets(s[0]);
	}
	
	return 0;
}
