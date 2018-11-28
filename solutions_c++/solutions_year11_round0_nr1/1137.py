#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

struct Seq
{
	int robot;
	int pos;
};
int N;
Seq seqs[10000];

int FindNext(int st, int id, int& index)
{
	for(int i=st+1; i<N; i++) if(seqs[i].robot == id)
	{
		index = i;
		return seqs[i].pos;
	}
	index = N;
	return -1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		cin>>N;
		int i, j;

		for(i=0; i<N; i++)
		{
			char robot[5];
			int pos;
			scanf("%s%d", robot, &pos);
			seqs[i].pos = pos;
			if(robot[0] == 'O') seqs[i].robot = 1;
			else seqs[i].robot = 2;
		}

		int ans = 0;
		i = j = 1;
		int t1, t2;
		int cur1 = FindNext(-1, 1, t1);
		int cur2 = FindNext(-1, 2, t2);
		while(1)
		{
			if(cur1==-1 && cur2==-1) break;
			int tt1 = t1, tt2 = t2;

			if(cur1!=-1)
			{
				if(i>cur1) i--;
				else if(i<cur1) i++;
				else
				{
					if(t1<t2)
						cur1 = FindNext(t1, 1, tt1);
				}
			}
			if(cur2!=-1)
			{
				if(j>cur2) j--;
				else if(j<cur2) j++;
				else
				{
					if(t2<t1)
						cur2 = FindNext(t2, 2, tt2);
				}
			}
			t1 = tt1;
			t2 = tt2;
			ans++;
		}
		
		cout << "Case #" << cas++ << ": ";

		cout << ans << endl;
	}
	return 0;
}