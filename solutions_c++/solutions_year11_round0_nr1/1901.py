//      a.cxx
//      
//      Copyright 2011 crbtmac <crbtmac@ubuntu>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define OO 1
#define BB 2
#define PB push_back
using namespace std;

vector<int>O, B, Q;

void init() 
{
	O.clear();
	B.clear();
	Q.clear();
}

inline int Abs(int x)
{
	if(x > 0) return x;
	return -x;
}

int main(int argc, char **argv)
{
	
	freopen("A-large.in", "r", stdin);
	
	//freopen("ans", "w", stdout);
	int t, n;
	
	cin >> t;
	for(int cas = 1; cas <= t; cas++)
	{
		cin >> n;
		init();
		char who;
		int button;
		while(n--)
		{
			cin >> who >> button;
			if(who == 'O')
				O.PB(button), Q.PB(OO);
			else
				B.PB(button), Q.PB(BB);
		}

		int Op = 0, Bp = 0, Qp = 0;
		int ans = 0, Opos = 1, Bpos = 1;
		int all = Q.size();
		while(Qp < all)
		{
			if(Q[Qp] == OO)
			{
				int c1 = Abs(O[Op] - Opos) + 1;
				ans += c1;
				Opos = O[Op++];
				while(c1-- && Bpos != B[Bp])
					if(Bpos < B[Bp]) Bpos++;
					else Bpos--;
			}
			else
			{
				int c1 = Abs(B[Bp] - Bpos) + 1;
				ans += c1;
				Bpos = B[Bp++];
				while(c1-- && Opos != O[Op])
					if(Opos < O[Op]) Opos++;
					else Opos--;
			}
			Qp++;
		}
		cout << "Case #" << cas << ": " << ans << endl;
		
	}
	
	return 0;
}

