#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <numeric>
#include <iterator>
#include <sstream>
#include <list>

#define pb push_back
#define mp make_pair
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)

template<typename T> inline bool setmin(T &a, T b) { if(a>=b) { a=b; return true; } return false; }
template<typename T> inline bool setmax(T &a, T b) { if(a<=b) { a=b; return true; } return false; }

using namespace std;

int M,V;
vector<int> type;
vector<int> tree;
vector<int> change;

inline int val(int type,int v1,int v2)
{
    if(type == 1) return v1 & v2;
    return v1 | v2;
}

int go(int a,int target);

int if0(int a,int target)
{
    if(target == 0)
    {
	int ret,tmp;
	tmp = go(a*2,0);
	if(tmp == -1) return -1;
	ret = go(a*2+1,0);
	if(ret == -1) return -1;
	return ret + tmp;
    }
    else
    {
	int r1,r2;
	r1 = go(a*2,1);
	if(r1 == -1) return go(a*2+1,1);
	r2 = go(a*2+1,1);
	if(r2 == -1) return r1;
	return min(r1,r2);
    }
}

int if1(int a,int target)
{
    if(target == 0)
    {
	int r1,r2;
	r1 = go(a*2,0);
	if(r1 == -1) return go(a*2+1,0);
	r2 = go(a*2+1,0);
	if(r2 == -1) return r1;
	return min(r1,r2);
    }
    else
    {
	int r1,r2;
	r1 = go(a*2,1);
	if(r1 == -1) return -1;
	r2 = go(a*2+1,1);
	if(r2 == -1) return -1;
	return r1+r2;
    }
}

int go(int a,int target)
{
    if(tree[a] == target) return 0;
    if(a*2 > M) return -1;

    if(change[a] == 0)
    {
	if(type[a] == 0) return if0(a,target);
	return if1(a,target);
    }

    int r1 = if0(a,target);
    int r2 = if1(a,target);

    if(type[a] == 0) 
    {
	if(r2 >= 0)
	    r2++; 
    }
    else 
    {
	if(r1 >= 0)
	    r1++;
    }

    if(r1 == -1) return r2;
    if(r2 == -1) return r1;
    return min(r1,r2);
}

void process(int tcase)
{
    cin >> M >> V;
    tree.resize(M+1,0);
    change.resize(M+1,0);
    type.resize(M+1,0);

    for(int i=1;i<=M/2;i++)
    {
	cin >> type[i] >> change[i];
    }
    for(int i=M/2+1;i<=M;i++)
    {
	cin >> tree[i];
    }

    for(int i=M/2;i>=1;i--)
    {
	tree[i] = val(type[i],tree[i*2],tree[i*2+1]);
    }

    if(tree[1] == V)
    {
	long long ret=0;
	cout << "Case #" << tcase << ": " << 0 << endl;
	return;
    }

    int ret = go(1,V);
    if(ret==-1)
    {
	cout << "Case #" << tcase << ": IMPOSSIBLE" << endl;
    }
    else
    {
	cout << "Case #" << tcase << ": " << ret << endl;
    }
}

int main(void)
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
        process(t);
    }
}
