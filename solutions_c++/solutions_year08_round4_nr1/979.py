#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

const int M = 10000 ;

//#define GetParent(i)  (btree[i].gate==1)?(btree[i*2].value & btree[i*2+1].value):(btree[i*2].value | btree[i*2+1].value)
typedef struct BTREE
{
	int value;
	int gate;
	int changable;
}BTree;


BTree btree[M+1];
int m, v;



int dps(int root, int v);

int GetParent(int i)
{
	if(btree[i].gate==1)
		return (btree[i*2].value && btree[i*2+1].value);
	else
		return (btree[i*2].value || btree[i*2+1].value);
}

int dps_sub(int root, int v)
{
	int left, right;
	if(btree[root].gate == 1)
	{			
		if(v == 1)
		{
			left = dps(root*2, 1);
			right = dps(root*2+1, 1);
			if(left >= 2*M || right >= 2*M)
				return 2*M;
			return left + right;
		}
		else //v == 0
		{
			return min(dps(root*2, 0), dps(root*2+1, 0));
		}
	}
	else //OR
	{
		if(v==1)
		{
			return min(dps(root*2, 1), dps(root*2+1, 1));
		}
		else //v==0;
		{
			left = dps(root*2, 0);
			right = dps(root*2+1, 0);
			if(left >= 2*M || right >= 2*M)
				return 2*M;
			return left + right;
		}
	}
}


int dps(int root, int v)
{	
	int ans=2*M;
	int temp;
	if(btree[root].value==v)
		return 0;	
	if(root*2>m) //leaf node
	{
		return 2*M;
	}
	//try change root
	if(btree[root].changable==1)
	{
		btree[root].gate = 1-btree[root].gate ;
		if(GetParent(root) == v)
		{
			btree[root].gate = 1-btree[root].gate ;
			return 1;
		}	
		ans = 1+dps_sub(root, v);
		if(ans < 1)
			ans=2*M;
		btree[root].gate = 1-btree[root].gate ;
	}
	temp = dps_sub(root, v);
	if(ans > temp)
	{
		ans = temp;
	}
	return ans;	
}

int main()
{
	int tn;
	int tt;
	int i;
	int ans;
	cin >> tn;
	tt=1;
	while(tt<=tn)
	{
		cin >> m >> v;
		memset(btree, -1, sizeof(btree));
		for(i=1; i<=(m-1)/2; i++)
		{
			cin >> btree[i].gate >> btree[i].changable;
		}
		for(i=(m+1)/2; i<=m; i++)
		{
			cin >> btree[i].value;
		}
		//get interior node value
		for(i=(m-1)/2; i>=1; i--)
		{
			btree[i].value = GetParent(i);
		}
				
		ans = dps(1, v);		
		if(ans >= 2*M)
			cout << "Case #" << tt <<": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tt <<": " << ans << endl;
		tt++;
	}
	return 0;
}