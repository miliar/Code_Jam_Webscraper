#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

#define All(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define Sort(c) sort((c).begin(),(c).end())

// using boost
// http://www.boost.org/
#include <boost/algorithm/string.hpp>

typedef struct node
{
	string name;
	vector<struct node*> list;
} Node;

int solve(vector<string> &ex, vector<string> &cr)
{
	int N = sz(ex);
	int M = sz(cr);
	
	Node tree;
	vector<Node*>* vp = &tree.list;
	
	for(int n=0; n<N; n++)
	{
		vector<string> vs;
		boost::algorithm::split(vs, ex[n], boost::is_any_of("/"));
		vp = &(tree.list);
		for(int i=1; i<sz(vs); i++)
		{
			int pos = -1;
			for(int j=0; j<sz(*vp); j++)
			{
				if((vp->at(j)->name).compare(vs[i])==0)
				{
					pos = j;
					break;
				}
			}
			if(pos<0)
			{
				Node* new_ = new Node;
				new_->name = vs[i];
				vp->pb(new_);
				vp = &(new_->list);
			}
			else
			{
				vp = &(vp->at(pos)->list);
			}
		}
	}
	int cnt = 0;
	for(int m=0; m<M; m++)
	{
		vector<string> vs;
		boost::algorithm::split(vs, cr[m], boost::is_any_of("/"));
		vp = &(tree.list);
		for(int i=1; i<sz(vs); i++)
		{
			int pos = -1;
			for(int j=0; j<sz(*vp); j++)
			{
				if((vp->at(j)->name).compare(vs[i])==0)
				{
					pos = j;
					break;
				}
			}
			if(pos<0)
			{
				Node* new_ = new Node;
				new_->name = vs[i];
				vp->pb(new_);
				vp = &(new_->list);
				cnt++;
			}
			else
			{
				vp = &(vp->at(pos)->list);
			}
		}
	}
	return cnt;
}

int main(int argc, char* argv[])
{
	uint T;
	cin >> T;
	
	for(uint t=0;t<T;t++)
	{
		uint N, M;
		cin >> N >> M;
		vector<string> ex(N);
		vector<string> cr(M);
		for(uint n=0;n<N;n++)
		{
			cin >> ex[n];
		}
		for(uint m=0;m<M;m++)
		{
			cin >> cr[m];
		}
		int r = solve(ex, cr);
		cout << "Case #" << t+1 << ": " << r << endl;
	}
	
	return 0;
}
