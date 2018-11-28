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

double gold = (sqrt(5.0)-1.0)/2;

int getlargeinterval(int x, int low, int high)
{
	int result;
	double n = x/gold;
	int m = (int)ceil(n);
	if(n > high)
		result = 0;
	else if(n < low)
		result = high-low+1;
	else
		result = high-m+1;
	return result;
}

int getsmallinterval(int x, int low, int high)
{
	int result;
	double n = x*gold;
	int m = (int)floor(n);
	if(n > high)
		result = high-low+1;
	else if(n < low)
		result = 0;
	else
		result = m-low+1;
	return result;
}

string solve(int A1, int A2, int B1, int B2)
{
	ll result = 0;
	for(int i=A1; i<=A2; i++)
	{
		if(i < B1)
			result += getlargeinterval(i, B1, B2);
		else if(i > B2)
			result += getsmallinterval(i, B1, B2);
		else
			result += getsmallinterval(i, B1, i)+getlargeinterval(i, i, B2);
	}
	char answer[21];
	sprintf(answer, "%lld", result);
	return answer;
}

void preprocess(){}

void readinput(int& A1, int& A2, int& B1, int& B2)
{
	cin>>A1>>A2>>B1>>B2;
}

vs getoutput()
{
	int A1, A2, B1, B2;
	readinput(A1, A2, B1, B2);
	string answer = solve(A1, A2, B1, B2);
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