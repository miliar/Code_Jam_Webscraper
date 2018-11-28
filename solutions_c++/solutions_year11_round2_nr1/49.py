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
#pragma comment(linker, "/STACK:67108864")
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


int numThreads=0;
const int _maxNumberOfThreads=8;
const int _maxNumberOfTests=201;
bool threadsUsed[_maxNumberOfThreads];
HANDLE nowRunning[_maxNumberOfThreads];
struct Answer
{
	int numberOfTest;
	vector<double> ans;
	inline void output()
	{
		printf("Case #%d:\n",numberOfTest+1);
		rept(i,L(ans))
		{
			printf("%.9lf\n",ans[i]);
		}
	}
};

struct Solver
{
	int _numberOfThread;
	Answer *pAns;
	int n;
	char mas[101][101];
	double wp[101],owp[101],oowp[101];
	inline void readInput()
	{
		scanf("%d",&n);
		rept(i,n) scanf("%s",mas[i]);
		C(wp); C(owp); C(oowp);
	}

	void run()
	{
		// put an answer into pAns
		rept(i,n)
		{
			int c=0,g=0;
			rept(j,n)
			{
				if (mas[i][j]!='.') ++c;
				if (mas[i][j]=='1') ++g;
			}
			wp[i]=(double)g/c;
		}

		rept(bad,n)
		{
			double sum=0.0;
			int cnt=0;
			rept(i,n)
			{
				if (mas[bad][i]=='.') continue;
				++cnt;
				int c=0,g=0;
				rept(j,n)
				{
					if (j==bad) continue;
					if (mas[i][j]!='.') ++c;
					if (mas[i][j]=='1') ++g;
				}
				sum+=(double)g/c;
			}
			sum/=cnt;
			owp[bad]=sum;
		}

		rept(i,n)
		{
			double sum=0.0;
			int c=0;
			rept(j,n)
			{
				if (mas[i][j]=='.') continue;
				sum+=owp[j];
				++c;
			}
			sum/=c;
			oowp[i]=sum;
		}

		vector<double> ans;
		rept(i,n) ans.pb(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
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
	threadsUsed[s->_numberOfThread]=true;
	++numThreads;
	nowRunning[s->_numberOfThread]=(HANDLE)_beginthread(run,0,s);
}

Solver solvers[_maxNumberOfThreads];
Answer answers[_maxNumberOfTests];

inline void solveParallel(int kolt,int maxThreads=2)
{
	memset(threadsUsed,0,sizeof(threadsUsed));
	int p=0;

	while (p<kolt)
	{
		if (numThreads<maxThreads)
		{
			int num=0;
			for (;num<maxThreads && threadsUsed[num];++num);

			cerr<<"Test #"<<p+1<<" was taken by thread #"<<num<<" at "<<1.0*clock()/CLOCKS_PER_SEC<<endl;

			solvers[num]._numberOfThread=num;
			solvers[num].readInput();
			answers[p].numberOfTest=p;
			solvers[num].pAns=&answers[p++];
			execute(&solvers[num]);
		}

		if (numThreads==maxThreads) WaitForMultipleObjects(numThreads,nowRunning,false,INFINITE);
	}
	while (numThreads)
	{
		for (int i=0;i<maxThreads;++i) if (threadsUsed[i]) WaitForSingleObject(nowRunning[i],INFINITE);
	}
	
	for (int i=0;i<kolt;++i) answers[i].output();

	cerr<<1.0*clock()/CLOCKS_PER_SEC<<endl;
}

inline void solveSequential(int kolt)
{
	for (int hod=0;hod<kolt;++hod)
	{
		cerr<<hod<<" "<<1.0*clock()/CLOCKS_PER_SEC<<endl;
		solvers[0]._numberOfThread=1;
		solvers[0].readInput();
		answers[hod].numberOfTest=hod;
		solvers[0].pAns=&answers[hod];
		solvers[0].run();
	}

	for (int i=0;i<kolt;++i) answers[i].output();
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int kolt=0;
	scanf("%d",&kolt);
	solveParallel(kolt);
}
