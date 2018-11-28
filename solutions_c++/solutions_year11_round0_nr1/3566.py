/*
ID: tecnoyo1
PROG: brownie
LANG: C++
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <utility>
#include <map>
#include "math.h"
#include "string.h"
#include "stdio.h"

using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define mp(x,y) make_pair(x,y)
#define fr(fl) freopen(fl,"r",stdin)
#define fw(fl) freopen(fl,"w",stdout)
#define getBit(code,i) (code &  (1 << i))
#define setBit(code,i) (code |  (1 << i))
#define resetBit(code,i) (code & ~(1 << i))

int needed;
pair<int,int> Osteps[200];
pair<int,int> Bsteps[200];
int O,B;


int main()
{
	fr("in.txt");
	fw("gcjb.txt");
	int N;
	cin >> N;
	rep(kase,N)
	{
		cin >> needed;
		O = B = 0;
		char tmp;
		rep(i,needed)
		{
			cin >> tmp;
			if(tmp == 'O')
			{

				cin >> Osteps[O].first;
				Osteps[O].second = i;
				O++;
			}
			else
			{
				cin >> Bsteps[B].first;
				Bsteps[B].second = i;
				B++;
			}
		}
		int res = 0;
		int crO=1,crB=1;
		int indxO=0,indxB=0;
		int tm = 0;
		int prsd = 0;
		while(indxO < O || indxB < B)
		{
			bool flg = true;
			if(indxO < O)
			{
				if(Osteps[indxO].first < crO)
					crO--;
				else if(Osteps[indxO].first > crO)
					crO++;
				else if(Osteps[indxO].second == prsd)
				{
					flg = false;
					//printf("pressed %d O @ %d\n",Osteps[indxO].first,tm);
					indxO++;
					prsd++;
				}
			}
			if(indxB < B)
			{
				if(Bsteps[indxB].first < crB)
					crB--;
				else if(Bsteps[indxB].first > crB)
					crB++;
				else if(flg && Bsteps[indxB].second == prsd)
				{
					//printf("pressed %d B @ %d\n",Bsteps[indxB].first,tm);
					indxB++;
					prsd++;
				}
			}
			tm++;
		}
		printf("Case #%d: %d\n",kase+1,tm);
	}
	return 0;
}