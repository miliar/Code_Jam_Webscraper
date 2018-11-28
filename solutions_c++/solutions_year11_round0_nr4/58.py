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

string solve(int N, const vi& a)
{
	int result = 0;
	loop(i, N)
		if(a[i] != i+1)
			result++;
	char answer[21];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(int& N, vi& a)
{
	cin>>N;
	a.resize(N);
	loop(i, N)
		cin>>a[i];
}

vs getoutput()
{
	int N;
	vi a;
	readinput(N, a);
	string answer = solve(N, a);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\D-small-attempt0.in", "r", stdin);freopen("test\\D-small-attempt0.out", "w", stdout);
	freopen("test\\D-large.in", "r", stdin);freopen("test\\D-large.out", "w", stdout);
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