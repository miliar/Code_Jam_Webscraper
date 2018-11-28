#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std;

string special = "oieastbg";

int deg[50];
bool edge[50][50];
int cntEdge;

int trans(char c)
{
	return c - 'a';
}

int sID(char c)
{
	for(int i = 0; i < (int)special.length(); i++)
		if(special[i] == c)
			return 26 + i;
	return -1;
}

void addEdge(int a, int b)
{	
	if(edge[a][b])return ;
	edge[a][b] = true;
	deg[a] ++;
	deg[b] --;
	cntEdge ++;
}

void solve()
{
	int val;
	cin >> val;
	string s;
	cin >> s;
	memset(edge, 0, sizeof(edge));
	memset(deg, 0, sizeof(deg));
	cntEdge = 0;
	for(int i = 0; i < (int)s.length()-1; i++)
	{
		char A = s[i], B = s[i+1];
		addEdge(trans(A), trans(B));
		if(sID(A) >= 0)
			addEdge(sID(A), trans(B));
		if(sID(B) >= 0)
			addEdge(trans(A), sID(B));
		if((sID(A) >= 0) && (sID(B) >= 0))
			addEdge(sID(A), sID(B));
	}
	int invalid = 0;
	for(int i = 0; i < 50; i++)
		if(deg[i] >= 0)
			invalid += deg[i];
	invalid --;
	if(invalid < 0)
		invalid = 0;
	cout << cntEdge + invalid + 1 << endl;


}

int MAIN()
{
	int testCase;
	cin >> testCase;
	for(int caseID = 1; caseID <= testCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int RUN_RESULT = MAIN();
	return RUN_RESULT;
}
