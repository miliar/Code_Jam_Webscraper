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

/*bool SameGroup(int a, int b, const vi& x1, const vi& y1, const vi& x2, const vi& y2)
{
	int x1a = x1[a], y1a = y1[a], x2a = x2[a], y2a = y2[a];
	int x1b = x1[b], y1b = y1[b], x2b = x2[b], y2b = y2[b];
	bool connect = false;
	if(max(x1a, x1b)<=min(x2a, x2b)+1 && max(y1a, y1b)<=min(y2a, y2b)+1)
		connect = true;
	if((x2a+1==x1b&&y2a+1==y2b) || (x2b+1==x1a&&y2b+1==y2a))
		connect = false;
	return connect;
}

int GetTime(const vi& index, const vi& x1, const vi& y1, const vi& x2, const vi& y2)
{
	vi::const_iterator it;
	int minsum = INT_MAX, maxx = 0, maxy = 0;
	tr(it, index)
	{
		if(x1[*it]+y1[*it] < minsum)
			minsum = x1[*it]+y1[*it];
		if(x2[*it] > maxx)
			maxx = x2[*it];
		if(y2[*it] > maxy)
			maxy = y2[*it];
	}
	return (maxx+maxy-minsum+1);
}*/

string solve(const vi& x1, const vi& y1, const vi& x2, const vi& y2)
{
	int R = sz(x1);
/*	vi group(R);
	int groupcount = 0;
	loop(i, R)
	{
		bool done = false;
		for(int j=0; j<i; j++)
		{
			if(SameGroup(i, j, x1, y1, x2, y2))
			{
				group[i] = group[j];
				done = true;
				break;
			}
		}
		if(!done)
			group[i] = groupcount++;
	}
	vvi groupindex(groupcount);
	loop(i, R)
		groupindex[group[i]].push_back(i);
	vi time(groupcount);
	loop(i, groupcount)
		time[i] = GetTime(groupindex[i], x1, y1, x2, y2);
	int result = *max_element(all(time));*/
	vvi data(101, vi(101, 0));
	vvi newdata(101, vi(101, 0));
	loop(i, R)
		for(int x=x1[i]; x<=x2[i]; x++)
			for(int y=y1[i]; y<=y2[i]; y++)
				data[x][y] = 1;
	int result = 0;
	bool empty = false;
	while(!empty)
	{
		result++;
		for(int i=1; i<=100; i++)
			for(int j=1; j<=100; j++)
			{
				if(!data[i-1][j] && !data[i][j-1])
					newdata[i][j] = 0;
				else if(data[i-1][j] && data[i][j-1])
					newdata[i][j] = 1;
				else
					newdata[i][j] = data[i][j];
			}
		data = newdata;
		empty = true;
		loop(i, 101) loop(j, 101)
			if(data[i][j])
			{
				empty = false;
				break;
			}
		if(empty)
			break;
	}
	char answer[11];
	sprintf(answer, "%d", result);
	return answer;
}

void preprocess(){}

void readinput(vi& x1, vi& y1, vi& x2, vi& y2)
{
	int R;
	cin>>R;
	x1.resize(R);
	y1.resize(R);
	x2.resize(R);
	y2.resize(R);
	loop(i, R)
		cin>>x1[i]>>y1[i]>>x2[i]>>y2[i];
}

vs getoutput()
{
	vi x1, y1, x2, y2;
	readinput(x1, y1, x2, y2);
	string answer = solve(x1, y1, x2, y2);
	return vs(1, answer);
}

void main()
{
	FILE *p, *q;
//	p=freopen("in.txt", "r", stdin); q=freopen("out.txt", "w", stdout);
	p=freopen("test\\C-small-attempt1.in", "r", stdin);q=freopen("test\\C-small-attempt1.out", "w", stdout);
//	p=freopen("test\\C-large.in", "r", stdin);q=freopen("test\\C-large.out", "w", stdout);
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