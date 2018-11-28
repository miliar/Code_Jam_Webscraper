#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)
#define FOR(i,s,e) for(int i = s; i < e; i++)
#define FORD(i,e,s) for(int i = e; i > s; i--)
#define ALL(x) x.begin(), x.end()
#define OUT(x) cout<<#x<<" = "<<x<<endl;
#define PB push_back
typedef long long ll;

struct node{
	node(){left=right=p=0;feature="";}
string feature;
double weight;
node* left, *right, *p;
};

bool isNumber(char x)
{ return (x>='0' && x<='9') || x=='.'; }

int main()
{
	int N;
	cin>>N;

	REP(tests, N)
	{
		string in, t;
		int L;
		cin>>L;
		char buf[200];
		cin.getline(buf, 200);
		REP(i,L)
			cin.getline(buf, 200), in+=buf;
		//cout<<in<<endl;

		node* root = 0;
		node* cur = root;

		int pos=0;
		int S = in.size();
		while(pos<S)
		{
			if(in[pos]=='(')
			{
				if(cur == 0)
					root = cur =new node();
				else if(cur->left==0)
					cur->left = new node(), cur->left->p = cur, cur = cur->left;
				else
					cur->right = new node(), cur->right->p = cur, cur = cur->right;
				pos++;
			}
			else if(in[pos]==')')
			{
				pos++;
				if(cur->p !=0)
					cur = cur->p;
			}
			else if(isalpha(in[pos]))
			{
				char buf[200];
				int start=pos;
				while(isalpha(in[pos]))
					buf[pos-start] = in[pos], pos++;
				buf[pos-start]=0;
				cur->feature = buf;
			}
			else if(isNumber(in[pos]))
			{
				char buf[200];
				int start=pos;
				while(isNumber(in[pos]))
					buf[pos-start] = in[pos], pos++;
				buf[pos-start]=0;
				cur->weight = atof(buf);
			}
			else pos++;
		}
		//cout<<"tree created"<<endl;

		int A;
		cin>>A;
		printf("Case #%d:\n", tests+1);
		REP(i,A)
		{
			string t;
			int features;
			cin>>t>>features;
			map<string, bool> M;
			REP(j,features)
				cin>>t, M[t] = true;
			node* cur = root;
			double res = 1.0;
			while(1)
			{
				//cout<<cur->weight<<"   "<<cur->feature<<endl;
				res*=cur->weight;
				if(cur->feature=="")
				{
					printf("%llf\n",  res);
					break;
				}
				else if(M.find(cur->feature)!=M.end())
					cur = cur->left;
				else
					cur = cur->right;
			}
		}		
	}

	return 0;
}

