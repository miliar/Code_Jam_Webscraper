#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <process.h>
#include <windows.h>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long


int numThreads;
const int _maxNumberOfThreads=8;
const int _maxNumberOfTests=201;
bool threadsUsed[_maxNumberOfThreads];
struct Answer
{
	int numberOfTest;
	int ans;
	inline void output()
	{
		printf("Case #%d: %.6lf\n",numberOfTest+1,1.0*ans);
	}
};

struct Solver
{
	int _numberOfThread;
	Answer *pAns;

	int n;
	int mas[1001];
	inline void readInput()
	{
		scanf("%d",&n);
		rept(i,n) scanf("%d",&mas[i]),--mas[i];
	}

	void run()
	{
		// put an answer into pAns
		int ans=0;
		rept(i,n) if (mas[i]!=i) ++ans;
		pAns->ans=ans;
	}
};



void run(void* _p)
{
	Solver* s=(Solver*)(_p);
	s->run();
	--numThreads;
	threadsUsed[s->_numberOfThread]=false;
	delete s;
	_endthread();
}
inline void execute(Solver* s)
{
	++numThreads;
	threadsUsed[s->_numberOfThread]=true;
	_beginthread(run,16777216,s); // <- increase stack size if necessary
}

Solver* solvers[_maxNumberOfThreads];
Answer answers[_maxNumberOfTests];

inline void solveParallel(int kolt,int maxThreads=2,int sleepTime=50)
{
	memset(threadsUsed,0,sizeof(threadsUsed));
	int p=0;
	while (p<kolt)
	{
		if (numThreads<maxThreads)
		{
			int num=0;
			for (;num<maxThreads && threadsUsed[num];++num);

			cerr<<p<<" "<<1.0*clock()/CLOCKS_PER_SEC<<endl;

			solvers[num]=new Solver();
			solvers[num]->_numberOfThread=numThreads;
			solvers[num]->readInput();
			answers[p].numberOfTest=p;
			solvers[num]->pAns=&answers[p++];
			execute(solvers[num]);
		}
		Sleep(sleepTime);
	}
	while (numThreads) Sleep(sleepTime);
	
	for (int i=0;i<kolt;++i) answers[i].output();

	cerr<<1.0*clock()/CLOCKS_PER_SEC<<endl;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int kolt=0;
	scanf("%d",&kolt);
	solveParallel(kolt);
}
