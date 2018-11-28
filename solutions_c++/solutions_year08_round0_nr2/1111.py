#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <strstream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

ifstream in("b2.in");
ofstream out("b2.out");

struct poez
{
	int startH;
	int startM;
	int endH;
	int endM;
};

poez gnal[110];
poez gal[110];

int st[130][130];
int en[130][130];

int main()
{
	int Test,i,j,num = 0;	
	int T,NA,NB;
	int answer1,answer2;
	string start,end;
	in >> Test;
	while (Test>0)
	{
		num++;
		Test--;
		answer1 = 0;
		answer2 = 0;
		in >> T;
		in >> NA >> NB;
		for (i=0;i<NA;i++)
		{
			in >> start >> end;
			gnal[i].startH = (int)(start[0]-'0')*10+(start[1]-'0');
			gnal[i].startM = (int)(start[3]-'0')*10+(start[4]-'0');
			gnal[i].endH   = (int)(end[0]-'0')*10+(end[1]-'0');
			gnal[i].endM   = (int)(end[3]-'0')*10+(end[4]-'0');
		}

		for (i=0;i<NB;i++)
		{
			in >> start >> end;
			gal[i].startH = (int)(start[0]-'0')*10+(start[1]-'0');
			gal[i].startM = (int)(start[3]-'0')*10+(start[4]-'0');
			gal[i].endH   = (int)(end[0]-'0')*10+(end[1]-'0');
			gal[i].endM   = (int)(end[3]-'0')*10+(end[4]-'0');
		}		

		for (i=0;i<100;i++)
			for (j=0;j<100;j++)
			{
				st[i][j] = 0;
				en[i][j] = 0;
			}
		int hour = 0,min = 0;
		while (hour<25)
		{
			for (i=0;i<NA;i++)
				if (gnal[i].startH == hour && gnal[i].startM == min)
				{
					if (st[hour][min]>0)
					{
						//cout << st[hour][min] << " gnal " << gnal[i].startH << ":" << gnal[i].startM 
						//	 << "    " << gnal[i].endH+(gnal[i].endM+T)/60 << " "<< (gnal[i].endM+T)%60 << endl;
						st[hour][min]--;						
						en[gnal[i].endH+(gnal[i].endM+T)/60][(gnal[i].endM+T)%60]++;
					}
					else
					{
						answer1++;
						//cout << "gnal " << gnal[i].startH << ":" << gnal[i].startM 
						//	 << "    " << gnal[i].endH+(gnal[i].endM+T)/60 << " "<< (gnal[i].endM+T)%60 << endl;
						en[gnal[i].endH+(gnal[i].endM+T)/60][(gnal[i].endM+T)%60]++;
					}
				}
			for (i=0;i<NB;i++)
				if (gal[i].startH == hour && gal[i].startM == min)
				{
					if (en[hour][min]>0)
					{
						//cout << en[hour][min] << " gal " << gal[i].startH << ":" << gal[i].startM 
						//	 << "    " << gal[i].endH+(gal[i].endM+T)/60 << " "<< (gal[i].endM+T)%60 << endl;
						en[hour][min]--;
						st[gal[i].endH+(gal[i].endM+T)/60][(gal[i].endM+T)%60]++;
					}
					else
					{
						answer2++;
						//cout << "gal " << gal[i].startH << ":" << gal[i].startM
						//	 << "    " << gal[i].endH+(gal[i].endM+T)/60 << " "<< (gal[i].endM+T)%60 << endl;
						st[gal[i].endH+(gal[i].endM+T)/60][(gal[i].endM+T)%60]++;
					}
				}
			int minn = min,hourr = hour;
			min++;
			if (min == 60)
			{
				min = 0;
				hour++;
			}
			st[hour][min] += st[hourr][minn];
			en[hour][min] += en[hourr][minn];
		}
		//cout << endl;
		out << "Case #" << num << ": " << answer1 << " " << answer2 << endl;
	}
	return 0;
}