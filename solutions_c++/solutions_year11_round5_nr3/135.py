#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

string solve(int R, int C, const vvi& dir)
{
	int count = R*C;
	int result = 0;
	for(int i=0; i<(1<<count); i++)
	{
		int mask = 1;
		vi next(count, -1);
		for(int j=0; j<count; j++)
		{
			int r = j/C;
			int c = j-r*C;
			int rinc = r==R-1 ? 0 : r+1;
			int rdec = r==0 ? R-1 : r-1;
			int cinc = c==C-1 ? 0 : c+1;
			int cdec = c==0 ? C-1 : c-1;
			if((mask&i) == 0)
			{
				if(dir[r][c] == 1)
					next[j] = r*C+cdec;
				else if(dir[r][c] == 2)
					next[j] = rdec*C+c;
				else if(dir[r][c] == 3)
					next[j] = rdec*C+cdec;
				else if(dir[r][c] == 4)
					next[j] = rinc*C+cdec;
			}
			else
			{
				if(dir[r][c] == 1)
					next[j] = r*C+cinc;
				else if(dir[r][c] == 2)
					next[j] = rinc*C+c;
				else if(dir[r][c] == 3)
					next[j] = rinc*C+cinc;
				else if(dir[r][c] == 4)
					next[j] = rdec*C+cinc;
			}
			mask <<= 1;
		}
		set<int> S;
		loop(j, count)
			S.insert(next[j]);
		if(S.size() == count)
			result ++;
	}
	char answer[21];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(int& R, int& C, vvi& dir)
{
	cin>>R>>C;
	dir.resize(R, vi(C));
	char ch;
	loop(i, R) loop(j, C)
	{
		cin>>ch;
		if(ch == '-')
			dir[i][j] = 1;
		else if(ch == '|')
			dir[i][j] = 2;
		else if(ch == '\\')
			dir[i][j] = 3;
		else if(ch == '/')
			dir[i][j] = 4;
	}
}

vs getoutput()
{
	int R, C;
	vvi dir;
	readinput(R, C, dir);
	string answer = solve(R, C, dir);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
	freopen("test\\C-small-attempt0.in", "r", stdin);freopen("test\\C-small-attempt0.out", "w", stdout);
//	freopen("test\\C-large.in", "r", stdin);freopen("test\\C-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}