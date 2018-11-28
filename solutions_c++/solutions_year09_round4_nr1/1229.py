#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
const double PI = acos(-1.0);
#define FOR(a,b) for(int i = a; i< b; ++i)
#define SORT(a,b) sort(a.begin(),a.end(),b)
#define MEMS(a,b) memset(a,b,sizeof(a))
template<class T>
inline T gcd(T a , T b) { if(a == 0 || b == 0 || a == b) return max(a,b); return a>b?gcd(a%b,b) : gcd(a,b%a);}
string intToStr(long long n) { char p[100];sprintf(p,"%lld",n);return string(p);}
int strToInt(string s) { istringstream sin(s); int r; sin >> r; return r;} 
const int Range = 9;
struct Node
{
	string M;
	int val;
	int step;
	Node()
	{
		M = "000000000000000000000000000000000000000000000000000000000000000000";
	}
};

queue<Node> All;

int N;
char MM[Range][Range];
string Line;
map<string,int> Have;
int ss = 1;
int BFS(Node n)
{
	All.push(n);	
	while(!All.empty()) {
		Node top = All.front();
		if(top.val == 0) return top.step;
		All.pop();
		for(int i = 0; i< N-1; i++)
		{
			Node New = top;
			New.step ++;
			/*int v1 = 0;
			for(int j = i+1; j< N; ++j) if(top.M[i*N+j] == '1') v1 ++;
			int v2 = 0;
			for(int j = i+1; j< N; ++j) if(top.M[i*N+j] == '1') v2 ++;
			New.val =  top.val-v1+v2;*/
			//swap(New.M[i],New.M[i+1]);
			char p[Range];
			for(int j = 0; j< N; ++j) p[j] = New.M[i*N+j];
			for(int j = 0 ;j< N; ++j) New.M[i*N+j] = New.M[(i+1)*N+j];
			for(int j = 0; j< N; ++j) New.M[(i+1)*N+j] = p[j];
			New.val = 0;
			for(int j = 0; j< N; ++j)
			{
				for(int k = j + 1 ; k< N; ++k)
				{
					if(New.M[j*N+k] == '1') New.val++;
				}
			}
			if(Have.find(New.M) == Have.end())
			{
				Have[New.M] = ss++;
				if(New.val <= top.val) {
					
					All.push(New);
				}
			}
		}
	}
}

int main()
{
	int TT = 1;
	int S = 0;
	cin >> S;
	for(int TT = 1; TT<= S; ++TT)
	{
		cin >> N;
		ss = 1;
		Have.clear();
		while(!All.empty()) All.pop();
		for(int i = 0; i< N; ++i)
		{
			cin >> MM[i];
			/*for(int j = 0; j< Line.length(); ++j)
			{
				M[i][j] = Line[i]-'0';
			}*/
		}
		int val = 0;
		for(int i = 0; i< N; ++i)
		{
			for(int j = i+1; j< N; ++j) 
				if(MM[i][j] == '1') val ++;
		}
		Node node;
		for(int i = 0; i< N; ++i)
			for(int j = 0;j < N; ++j)
				node.M[i*N+j] = MM[i][j];
		node.val = val;
		node.step = 0;
		printf("Case #%d: %d\n",TT,BFS(node));
		//printf("TTTT%d\n",TT-1);
	}
	return 0;
}