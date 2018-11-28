// 3.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"

#include <algorithm>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int c;
	scanf("%d", &c);
	for (int k = 1; k <= c; k++)
	{
		//input
		int t;
		scanf("%d", &t);
		char color[128];
		int stop[128];
		for (int i = 0; i < t; i++)
		{
			char tmp[2];
			scanf("%s %d",tmp, &stop[i]);
			color[i] = tmp[0];
		}

		//run
		int pos_o = 1, pos_b = 1;
		int next_o = -1, next_b = -1;
		char * ptr_o = find(color, color+t, 'O');
		if (ptr_o != color+t)
			next_o = stop[ptr_o-color];
		char * ptr_b = find(color, color+t, 'B');
		if (ptr_b != color+t)
			next_b = stop[ptr_b-color];
		int ret = 0;
		while(1)
		{
			if (next_b != -1)
			{
				if (next_o != -1)
				{
					//find [first] and move
					int m;
					if (ptr_b < ptr_o)
					{
						m = abs(next_b-pos_b);
						ret += m;
						//move b
						pos_b = next_b;
						//move o
						m++; // (add one step)
						if (m >= abs(next_o-pos_o))
							pos_o = next_o;
						else
						{
							if (next_o<pos_o) pos_o -= m;
							else pos_o += m;
						}
						//push b
						ret++;
						//next b
						next_b = -1;
						ptr_b = find(ptr_b+1, color+t, 'B');
						if (ptr_b != color+t)
							next_b = stop[ptr_b-color];
					}
					else
					{
						m = abs(next_o-pos_o);
						ret += m;
						//move o
						pos_o = next_o;
						//move b
						m++; // (add one step)
						if (m >= abs(next_b-pos_b))
							pos_b = next_b;
						else
						{
							if (next_b<pos_b) pos_b -= m;
							else pos_b += m;
						}
						//push o
						ret++;
						//next o
						next_o = -1;
						ptr_o = find(ptr_o+1, color+t, 'O');
						if (ptr_o != color+t)
							next_o = stop[ptr_o-color];
					}
				}
				else
				{
					//move b
					ret += abs(next_b-pos_b);
					pos_b = next_b;
					//push b
					ret++;
					//next b
					next_b = -1;
					ptr_b = find(ptr_b+1, color+t, 'B');
					if (ptr_b != color+t)
						next_b = stop[ptr_b-color];
				}
			}
			else
			{
				if (next_o != -1)
				{
					//move o
					ret += abs(next_o-pos_o);
					pos_o = next_o;
					//push o
					ret++;
					//next o
					next_o = -1;
					ptr_o = find(ptr_o+1, color+t, 'O');
					if (ptr_o != color+t)
						next_o = stop[ptr_o-color];
				}
				else
				{
					//end
					break;
				}
			}
		}

		//output
		printf("Case #%d: %d\n", k, ret);
	}
	return 0;
}

