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

const int* prime;

int sievePrim(int N)
{
	int size = (N+1)/2;
	unsigned char* table = new unsigned char[size];
	memset(table, 1, size);
	int larger = (int)(sqrt((double)N)/2);
	for(int i=1; i<=larger; i++)
	{
		if(table[i] == 0)
			continue;
		for(int j=2*i*(i+1); j<size; j+=2*i+1)
			table[j] = 0;
	}
	int count = 0;
	for(int i=0; i<=size; i++)
		if(table[i] == 1)
			count++;
	int* primelist = new int[count];
	count = 0;
	primelist[count++] = 2;
	for(int i=1; i<=size; i++)
		if(table[i] == 1)
			primelist[count++] = 2*i+1;
	delete []table;
	prime = (const int*)primelist;
	return count;
}

void ReleasePrime()
{
	delete []prime;
}

string solve(ll N, int primecount)
{
	int count = 1;
	loop(i, primecount)
	{
		ll temp = prime[i];
		temp *= prime[i];
		if(temp > N)
			break;
		while(temp <= N)
		{
			count ++;
			temp *= prime[i];
		}
	}
	if(N == 1)
		count = 0;
	char answer[11];
	sprintf(answer, "%d", count);
	return answer;
}

int preprocess()
{
	return sievePrim(1000000);
}

void readinput(ll& N)
{
	cin>>N;
}

vs getoutput(int primecount)
{
	ll N;
	readinput(N);
	string answer = solve(N, primecount);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\C-small-attempt0.in", "r", stdin);freopen("test\\C-small-attempt0.out", "w", stdout);
	freopen("test\\C-large.in", "r", stdin);freopen("test\\C-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	int primecount = preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput(primecount);
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}