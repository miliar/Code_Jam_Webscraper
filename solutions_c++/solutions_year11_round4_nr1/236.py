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

string solve(int X, int S, int R, int T, const vi& B, const vi& E, const vi& W)
{
	int N = W.size();
	vii walkway(N+1);
	int totallength = 0;
	loop(i, N)
	{
		walkway[i+1].first = W[i];
		walkway[i+1].second = E[i]-B[i];
		totallength += E[i]-B[i];
	}
	walkway[0] = ii(0, X-totallength);
	sort(all(walkway));

	double time = 0.0;
	double runtime = T;
	loop(i, N+1)
	{
		double len = walkway[i].second;
		double runspeed = walkway[i].first+R;
		if(len/runspeed <= runtime)
		{
			runtime -= len/runspeed;
			time += len/runspeed;
		}
		else
		{
			double walkspeed = walkway[i].first+S;
			time += runtime + (len-runtime*runspeed)/walkspeed;
			runtime = 0;
		}
	}
	char answer[21];
	sprintf(answer, "%.7f", time);
	return answer;
}

void preprocess(){}

void readinput(int& X, int& S, int& R, int& T, vi& B, vi& E, vi& W)
{
	int N;
	cin>>X>>S>>R>>T>>N;
	B.resize(N);
	E.resize(N);
	W.resize(N);
	loop(i, N)
		cin>>B[i]>>E[i]>>W[i];
}

vs getoutput()
{
	int X, S, R, T;
	vi B, E, W;
	readinput(X, S, R, T, B, E, W);
	string answer = solve(X, S, R, T, B, E, W);
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