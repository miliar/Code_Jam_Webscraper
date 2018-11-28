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

int getStraight(const vi& sub)
{
	vi subCopy(sub);
	int n = sub.size();
	int m = sub[n-1]-sub[0]+1;
	vi count(m);
	loop(i, n)
		count[sub[i]-sub[0]]++;
	
	int result = m;
	priority_queue<int, vi, greater<int> > Q;
	int prev = 0;
	loop(i, m)
	{
		if(count[i] > prev)
		{
			loop(j, count[i]-prev)
				Q.push(i);
		}
		else if(count[i] < prev)
		{
			loop(j, prev-count[i])
			{
				int node = Q.top();
				Q.pop();
				result = min(result, i-node);
			}
		}
		prev = count[i];
	}

	reverse(all(count));
	while(!Q.empty())
		Q.pop();
	prev = 0;
	loop(i, m)
	{
		if(count[i] > prev)
		{
			loop(j, count[i]-prev)
				Q.push(i);
		}
		else if(count[i] < prev)
		{
			loop(j, prev-count[i])
			{
				int node = Q.top();
				Q.pop();
				result = min(result, i-node);
			}
		}
		prev = count[i];
	}
	return result;
}

string solve(vi& c)
{
	int n = c.size();
	if(n == 0)
		return "0";
	sort(all(c));
	vi sub;
	int result = n;
	loop(i, n)
	{
		if(i>0 && c[i]-c[i-1]>1)
		{
			result = min(result, getStraight(sub));
			sub.clear();
		}
		sub.push_back(c[i]);
	}
	result = min(result, getStraight(sub));
	char answer[20];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(vi& c)
{
	int n;
	cin>>n;
	c.resize(n);
	loop(i, n)
		cin>>c[i];
}

vs getoutput()
{
	vi c;
	readinput(c);
	string answer = solve(c);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\B-small-attempt0.in", "r", stdin);freopen("test\\B-small-attempt0.out", "w", stdout);
	freopen("test\\B-large.in", "r", stdin);freopen("test\\B-large.out", "w", stdout);
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