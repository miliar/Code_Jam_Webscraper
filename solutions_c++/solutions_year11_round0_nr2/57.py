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

string solve(int C, int D, const vvi& combine, const vvi& oppose, const string& str)
{
	string result;
	loop(i, sz(str))
	{
		if(sz(result) == 0)
			result.push_back(str[i]);
		else if(combine[result[sz(result)-1]][str[i]] > 0)
			result[sz(result)-1] = combine[result[sz(result)-1]][str[i]];
		else
		{
			int opp = 0;
			loop(j, sz(result))
				if(oppose[result[j]][str[i]] == 1)
				{
					opp = 1;
					break;
				}
			if(opp == 1)
				result.clear();
			else
				result.push_back(str[i]);
		}
	}

	string answer = "[";
	loop(i, sz(result))
	{
		if(i < sz(result)-1)
			answer = answer+result[i]+", ";
		else
			answer = answer+result[i];
	}
	answer += "]";
	return answer;
}

void preprocess(){}

void readinput(int& C, int& D, vvi& combine, vvi& oppose, string& str)
{
	cin>>C;
	loop(i, C)
	{
		cin>>str;
		combine[str[0]][str[1]] = str[2];
		combine[str[1]][str[0]] = str[2];
	}

	cin>>D;
	loop(i, D)
	{
		cin>>str;
		oppose[str[0]][str[1]] = 1;
		oppose[str[1]][str[0]] = 1;
	}

	int len;
	cin>>len>>str;
}

vs getoutput()
{
	int C, D;
	vvi combine(128, vi(128));
	vvi oppose(128, vi(128));
	string str;
	readinput(C, D, combine, oppose, str);
	string answer = solve(C, D, combine, oppose, str);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\B-small-attempt3.in", "r", stdin);freopen("test\\B-small-attempt3.out", "w", stdout);
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