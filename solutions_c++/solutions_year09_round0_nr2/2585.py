#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#include <stdio.h>
#include <stdlib.h>

struct POINT
{
	int value;
	int rx;
	int ry;
};

int i , j , n , h , w , k , flag = 0 , oldx , oldy , tj , tk , tflag , min , q , b ;
char mark[2] , ans[150][2][150] , *temx , *temy;
POINT p[150][150];

int conversion(char y[50])
{
	for(b = 0 ; b < q ; b++)
	{
		if(strcmp(ans[b][0] , y) == 0)
		{
			return b;
		}
	}
	strcpy(ans[q][0] , y);
	mark[0]++;
	strcpy(ans[q][1] , mark);

	q++;
	return q - 1;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	cin >> n;
	for(i = 1 ; i <= n ; i++)
	{
		mark[0] = 'a';
		memset(ans , 0 , sizeof(ans));
		cin >> h >> w;
		for(j = 0 ; j < h ; j++)
		{
			for(k = 0 ; k < w ; k++)
			{
				cin >> p[j][k].value;
			}
		}

		for(j = 0 ; j < h ; j++)
		{
			for(k = 0 ; k < w ; k++)
			{
			
				flag = 0;
				tflag = 0;
				p[j][k].rx = j;
				p[j][k].ry = k;
				tj = j;
				tk = k;
				oldx = j;
				oldy = k;
				while(1)
				{
					min = 999999;
					flag = 0;
					tflag = 0;
					
					if( ( (tj - 1) >= 0 ) && (tj < h) && ( tk >= 0) && (tk < w)  && (p[tj][tk].value > p[tj - 1][tk].value) )
					{
						if(min == 999999)
						{
							min = p[tj - 1][tk].value;
						}
						else
						{
							if(p[tj - 1][tk].value >= min)
							{
								flag++;
								goto L1;
							}
							else 
							{
								min = p[tj - 1][tk].value;
							}
						}
						p[oldx][oldy].rx = tj - 1;
						p[oldx][oldy].ry = tk;
						tflag = 1;
					}
					else
					{
						flag++;
					}
					
				
L1:					if( ( (tk - 1) >= 0 ) && (tk < w) && (tj >= 0) && (tj < h) && (p[tj][tk].value > p[tj][tk - 1].value) )
					{
						if(min == 999999)
						{
							min = p[tj][tk - 1].value;
						}
						else
						{
							if(p[tj][tk - 1].value >= min)
							{
								flag++;
								goto L2;
							}
							else
							{
								min = p[tj][tk - 1].value;
							}
						}
						p[oldx][oldy].rx = tj;
						p[oldx][oldy].ry = tk - 1;
						tflag = 2;
					}
					else
					{
						flag++;
					}

L2:					if( ( (tk + 1) < w ) && (tk >= 0) && (tj < h) && (tj >= 0) && (p[tj][tk].value > p[tj][tk + 1].value) )
					{
						if(min == 999999)
						{
							min = p[tj][tk + 1].value;
						}
						else
						{
							if(p[tj][tk + 1].value >= min)
							{
								flag++;
								goto L3;
							}
							else
							{
								min =  p[tj][tk + 1].value;
							}
						}

						p[oldx][oldy].rx = tj;
						p[oldx][oldy].ry = tk + 1;
						tflag = 3;
					}
					else
					{
						flag++;
					}

			
L3:					if( ( (tj + 1) < h ) && (tj >= 0) && (tk < w) && (tk >= 0) && (p[tj][tk].value > p[tj + 1][tk].value) )
					{
						if(min == 999999)
						{
							min = p[tj + 1][tk].value;
						}
						else
						{
							if(p[tj + 1][tk].value >= min)
							{
								flag++;
								goto L4;
							}
							else
							{
								min = p[tj + 1][tk].value;
							}
						}
						p[oldx][oldy].rx = tj + 1;
						p[oldx][oldy].ry = tk;
						tflag = 4;
					}
					else
					{
						flag++;
					}
L4:					if(flag == 4)
						break;
					if(tflag == 0)
						break;
					switch(tflag)
					{
					case 1:
						{
							tj--;
							break;
						}
					case 2:
						{
							tk--;
							break;
						}
					case 3:
						{
							tk++;
							break;
						}
					case 4:
						{
							tj++;
							break;
						}
					default:
						break;
					}
				}
			}
		}

		printf("Case #%d:\n" , i);
		for(j = 0 ; j < h ; j++)
		{
			for(k = 0 ; k < w ; k++)
			{
				temx = new char[50];
				temy = new char[10];
				itoa(p[j][k].rx , temx , 10);
				itoa(p[j][k].ry , temy , 10);
				strcat(temx,temy);
				if(j == 0 && k ==0)
				{
					strcpy(ans[0][0] , temx);
					strcpy(ans[0][1] , "a");
					mark[0] = 'a';
					q = 1;
				}
				if(k != w - 1)
				{
					cout << ans[conversion(temx)][1] << " ";
				}
				else
				{
					cout << ans[conversion(temx)][1] ;
				}
				delete temx;
				delete temy;

			}
			
				cout << endl;
		
		}


	}
	return 0;
}



