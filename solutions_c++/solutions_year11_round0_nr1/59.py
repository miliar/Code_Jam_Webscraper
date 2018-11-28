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

string solve(int N, const vii& seq)
{
	int prev[] = {1,1};
	int dist[] = {0,0};
	int commondist[] = {0,0};
	int result = 0;
	loop(i, N)
	{
		int cur = seq[i].first;
		dist[cur] = abs(seq[i].second - prev[cur]);
		int increase = max(dist[cur]-commondist[1-cur], 0) + 1;
		result += increase;
		commondist[cur] += increase;
		commondist[1-cur] = 0;
		prev[cur] = seq[i].second;
	}
	char answer[11];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(int& N, vii& seq)
{
	cin>>N;
	seq.resize(N);
	loop(i, N)
	{
		char ch;
		cin>>ch;
		if(ch=='O')
			seq[i].first = 0;
		else
			seq[i].first = 1;
		cin>>seq[i].second;
	}
}

vs getoutput()
{
	int N;
	vii seq;
	readinput(N, seq);
	string answer = solve(N, seq);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\A-small-attempt0.in", "r", stdin);freopen("test\\A-small-attempt0.out", "w", stdout);
	freopen("test\\A-large.in", "r", stdin);freopen("test\\A-large.out", "w", stdout);
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