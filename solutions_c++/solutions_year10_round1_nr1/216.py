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

string solve(int K, vector< vector<char> >& data)
{
	int N = sz(data);
	for(int i=0; i<N; i++)
	{
		int pos = N-1;
		for(int j=N-1; j>=0; j--)
			if(data[i][j]!= '.')
			{
				data[i][pos] = data[i][j];
				if(pos != j)
					data[i][j] = '.';
				pos--;
			}
	}
	bool red=false, blue=false;
	int x;
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
		{
			if(data[i][j] != '.')
			{
				char value = data[i][j];
				if(i<=N-K)
				{
					for(x=0; x<K; x++)
						if(data[i+x][j] != value)
							break;
					if(x == K)
					{
						if(data[i][j] == 'R')
							red = true;
						if(data[i][j] == 'B')
							blue = true;
					}
				}
				if(j<=N-K)
				{
					for(x=0; x<K; x++)
						if(data[i][j+x] != value)
							break;
					if(x == K)
					{
						if(data[i][j] == 'R')
							red = true;
						if(data[i][j] == 'B')
							blue = true;
					}
				}
				if(i<=N-K && j<=N-K)
				{
					for(x=0; x<K; x++)
						if(data[i+x][j+x] != value)
							break;
					if(x == K)
					{
						if(data[i][j] == 'R')
							red = true;
						if(data[i][j] == 'B')
							blue = true;
					}
				}
				if(i>=K-1 && j<=N-K)
				{
					for(x=0; x<K; x++)
						if(data[i-x][j+x] != value)
							break;
					if(x == K)
					{
						if(data[i][j] == 'R')
							red = true;
						if(data[i][j] == 'B')
							blue = true;
					}
				}
			}
		}
	string answer;
	if(red == true)
		answer = (blue==true) ? "Both" : "Red";
	else
		answer = (blue==true) ? "Blue" : "Neither";
	return answer;
}

void preprocess(){}

void readinput(int& K, vector< vector<char> >& data)
{
	int N;
	cin>>N>>K;
	data.resize(N, vector<char>(N));
	loop(i, N) loop(j, N)
		cin>>data[i][j];
}

vs getoutput()
{
	int K;
	vector< vector<char> > data;
	readinput(K, data);
	string answer = solve(K, data);
	return vs(1, answer);
}

void main()
{
	FILE *p, *q;
//	p=freopen("in.txt", "r", stdin); q=freopen("out.txt", "w", stdout);
//	p=freopen("test\\A-small-attempt0.in", "r", stdin);q=freopen("test\\A-small-attempt0.out", "w", stdout);
	p=freopen("test\\A-large.in", "r", stdin);q=freopen("test\\A-large.out", "w", stdout);
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