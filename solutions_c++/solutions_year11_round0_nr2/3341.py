#include <cstdio>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <hash_map>
#include <hash_set>

#define mp make_pair
using namespace std;

void readdata();
void solve();

typedef pair<char,char> elempair;
map<elempair,char> combine;
typedef map<elempair,char>::iterator mci;
set<elempair> oppose;



int n,t;
int combcount,opposcount;

list<char> elemlist;
typedef list<char>::iterator lci;

char stlist[101];
map<char,int> hashl;
typedef map<char,int>::iterator hashit;


inline void outlist()
{
	cout.put('[');
	lci first = elemlist.begin(),last = elemlist.end();
	for(lci it = first;it != last;++it)
	{
		if (it != first)
			cout << ", ";
		cout.put(*it);
	}
	cout.put(']');
}
void readdata()
{
	cin >> t;
	for(int i=0;i<t;++i)
	{
		if (i)
			cout.put('\n');
		combine.clear();
		oppose.clear();
		cin >> combcount;
		for(int j=0;j<combcount;++j)
		{
			char comb[4];
			cin >> comb;
			combine.insert(mp(mp(comb[0],comb[1]),comb[2]));
			combine.insert(mp(mp(comb[1],comb[0]),comb[2]));
		}
		cin >> opposcount;
		for(int j=0;j<opposcount;++j)
		{
			char opp[3];
			cin >> opp;
			oppose.insert(mp(opp[0],opp[1]));
			oppose.insert(mp(opp[1],opp[0]));
		}
		cin >> n;
		cin >> stlist;
		stlist[n] = '\0';
		solve();
		printf("Case #%d: ",i+1);
		outlist();
	}
}


void make_combine()
{
	char c1,c2;
	{
		lci it = elemlist.end();
		c1 = elemlist.back();
		----it;
		c2 = *it;
	}
	mci it ; 
	if ( ( it = combine.find(mp(c1,c2)) ) != combine.end())
	{
		elemlist.pop_back();
		elemlist.pop_back();
		elemlist.push_back(it->second);
		hashl[c1]--;
		hashl[c2]--;
		hashl[it->second]++;
	}
}

void make_oppose()
{
	char c1;
	c1 = elemlist.back();
	lci first = elemlist.begin(),last = elemlist.end();
	for(lci it = first;it != last;++it)
	{
		if(oppose.find(mp(c1,*it)) != oppose.end())
		{
			hashl.clear();
			elemlist.clear();
			break;
		}
	}
}

void solve()
{
	elemlist.clear();
	for(int i=0;i<n;++i)
	{
		elemlist.push_back(stlist[i]);
		hashl[stlist[i]]++;
		if (elemlist.size() > 1)
		{
			make_combine();
			make_oppose();
		}
	}
}
int main()
{
#ifdef ANYKEY
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	readdata();
	return (EXIT_SUCCESS);
}