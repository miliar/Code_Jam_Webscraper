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
typedef vector<double> vd;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

inline double getCut(double p, double n, double w, double s)
{
	double x = 0;
	if(fabs(n-p) < 1e-9)
		x = s/p;
	else
		x = (sqrt(p*p+2*s*(n-p)/w)-p)/((n-p)/w);
	return x;
}

double nextCut(const vd& len, double eS, double prevCut)
{
	int base = max((int)floor(prevCut), 0);
	double start = prevCut;
	double prevLen = (prevCut-base)*(len[base+1]-len[base]) + len[base];
	double nextLen = len[base+1]; 
	double width = base+1-prevCut;
	double first = (nextLen+prevLen)*width/2;
	while(eS > first)
	{
		eS -= first;
		base ++;
		start = base;
		prevLen = len[base];
		nextLen = len[base+1];
		width = 1;
		first = (prevLen+nextLen)/2;
	}
	return start + getCut(prevLen, nextLen, width, eS);
}

vs solve(int W, const vii& lower, const vii& upper, int G)
{
	vd l(W+1), u(W+1), len(W+1);
	for(int i=0; i<(int)lower.size()-1; i++)
	{
		for(int j=lower[i].first; j<=lower[i+1].first; j++)
			l[j] = lower[i].second + (double)(j-lower[i].first)*(lower[i+1].second-lower[i].second)/(lower[i+1].first-lower[i].first);
	}
	for(int i=0; i<(int)upper.size()-1; i++)
	{
		for(int j=upper[i].first; j<=upper[i+1].first; j++)
			u[j] = upper[i].second + (double)(j-upper[i].first)*(upper[i+1].second-upper[i].second)/(upper[i+1].first-upper[i].first);
	}
	for(int i=0; i<=W; i++)
		len[i] = u[i]-l[i];

	double S = 0;
	loop(i, W)
		S += (len[i+1]+len[i])/2;
	double eS = S/G;

	vd cut(G);
	cut[0] = 0;
	vs answer(G);
	char result[20];
	for(int i=1; i<G; i++)
	{
		cut[i] = nextCut(len, eS, cut[i-1]);
		sprintf(result, "%.6f", cut[i]);
		answer[i] = result;
	}
	return answer;
}

void preprocess(){}

void readinput(int& W, vii& lower, vii& upper, int& G)
{
	int L, U;
	cin>>W>>L>>U>>G;
	lower.resize(L);
	upper.resize(U);
	loop(i, L)
		cin>>lower[i].first>>lower[i].second;
	loop(i, U)
		cin>>upper[i].first>>upper[i].second;
}

vs getoutput()
{
	vii lower, upper;
	int W, G;
	readinput(W, lower, upper, G);
	vs answer = solve(W, lower, upper, G);
	return answer;
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