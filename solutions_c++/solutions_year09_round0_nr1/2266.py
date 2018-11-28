#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;



struct  node
{
	node* child[26];
	node(){for (int i = 0; i <26; ++i)
	{
		child[i]  = NULL;
	}
	}
} ;

node * root = new node;
int L,D,N;

int st[16];
int ed[16];
	
void parse(char * w)
{
	int seg = 0;
	int i = 0;
	bool inner = false;
	while (w[i])
	{
		if (inner)
		{
			if (w[i] == ')')
			{
				ed[seg++] = i-1;
				inner = false;
			}
			else if (w[i] == '(')
			{
				throw 1;
			}
		}
		else
		{
			if (w[i] == '(')
			{
				inner = true;
				st[seg] = i+1;
			}
			else if (w[i] == ')')
			{
				throw 1;
			}
			else
			{
				st[seg] = ed[seg] = i;
				++seg;
			}

		}
		++i;
	}

}
	void solve(node * r,char * word, int lev, int &cnt)
	{

		if (lev == L && r)
		{
			++cnt;
			return;
		}
		else{
			if (r == NULL)
				return;
			for(int index = st[lev] ; index <= ed[lev]; ++index)
			{
				solve(r->child[word[index] - 'a'], word,lev+1, cnt );
			}
		}

	}
int main()
{
	cin >> L >> D >> N;


	for (int i = 0; i < D; ++i)
	{
		char word[20] = {0};
		cin >> word;
		node * r = root;
		for (int j = 0; j < L; ++j)
		{
			int c = word[j] - 'a';
			if (r->child[c] == NULL)
			{
				node * cur = new node();
				r->child[c] = cur;
			}
			r = r->child[c];
		}
	}
	
	for (int i = 0; i < N; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		char word[400] = {0};
		cin >> word;
		int cnt = 0;
		node * r = root;
		memset(st, 0, sizeof st);
		memset(ed, 0, sizeof ed);
		
		parse(word);
		solve(r,word,0,cnt);

		cout << cnt << endl;

	}
	return 1;
}