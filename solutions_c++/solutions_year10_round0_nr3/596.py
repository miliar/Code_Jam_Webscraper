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
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

string solve(int R, int k, const vi& group)
{
	int N = sz(group);
	vi run(N, -1);
	vll ticket(N+1, 0);
	run[N-1] = 0;
	ticket[0] = 0;
	int start = 0;
	int startperiod = 0, runperiod = 0;
	ll ticketperiod = 0;
	for(int r=1; r<=N; r++)
	{
		ll occupy = group[start];
		int cur=start, next = (start+1);
		if(next == N)
			next = 0;
		while(occupy+group[next]<=k && next!=start)
		{
			cur = next;
			occupy += group[next++];
			if(next == N)
				next = 0;
		}
		start = next;
		ticket[r] = ticket[r-1]+occupy;
		if(run[cur] == -1)
			run[cur] = r;
		else
		{
			startperiod = run[cur];
			runperiod = r-run[cur];
			ticketperiod = ticket[r] - ticket[run[cur]];
			break;
		}
	}
	int periodnumber = (R-startperiod)/runperiod;
	int modstart = R - periodnumber*runperiod;
	ll totalticket = ticketperiod*periodnumber + ticket[modstart];
	char answer[21];
	sprintf(answer, "%lld", totalticket);
	return answer;
}

void preprocess(){}

void readinput(int& R, int& k, vi& group)
{
	int N;
	cin>>R>>k>>N;
	group.resize(N);
	vi::iterator it;
	tr(it, group)
		cin>>(*it);
}

vs getoutput()
{
	int R, k;
	vi group;
	readinput(R, k, group);
	string answer = solve(R, k, group);
	return vs(1, answer);
}

void main()
{
	FILE *p, *q;
//	p=freopen("in.txt", "r", stdin); q=freopen("out.txt", "w", stdout);
//	p=freopen("test\\C-small-attempt0.in", "r", stdin);q=freopen("test\\C-small-attempt0.out", "w", stdout);
	p=freopen("test\\C-large.in", "r", stdin);q=freopen("test\\C-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for (int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
		fflush(stdout);
	}
	fclose(p);
	fclose(q);
}