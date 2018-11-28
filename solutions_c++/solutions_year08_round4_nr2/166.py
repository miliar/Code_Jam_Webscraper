#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
using namespace std;


int N, M, A;


void Read()
{
	scanf("%d %d %d", & N, & M, & A);
}

bool ok(int xb, int yb, int xc, int yc)
{
	if(!(0 <= xb && xb <= N)) return false;
	if(!(0 <= xc && xc <= N)) return false;
	if(!(0 <= yb && yb <= M)) return false;
	if(!(0 <= yc && yc <= M)) return false;
	if(xb == 0 && yb == 0) return false;
	if(xc == 0 && yc == 0) return false;
	if(xb == xc && yb == yc) return false;
	
	return (A == (xc) * (yb) - (xb) * (yc));
}

void Solve(int test)
{
	int B, xb, yb, xc, yc;
	
	for(xc = 0; xc <= N; xc ++)
	{
		for(yb = 0; yb <= M; yb ++)
		{
			if(A <= xc * yb)
			{
				B = xc * yb - A;
				
				if(B == 0)
				{
					for(xb = 0; xb <= N; xb ++)
					{
						yc = 0;
						
						if(ok(xb, yb, xc, yc))
						{
							printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, xb, yb, xc, yc);
							
							return;
						}
					}
					
					for(yc = 0; yc <= M; yc ++)
					{
						xb = 0;
						
						if(ok(xb, yb, xc, yc))
						{
							printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, xb, yb, xc, yc);
							
							return;
						}
					}
				}
				else
				{
					for(int i = 1; i * i <= B; i ++)
					{
						if(B % i == 0)
						{
							xb = i;
							yc = B / i;
							
							if(ok(xb, yb, xc, yc))
							{
								printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, xb, yb, xc, yc);
								
								return;
							}
							
							xb = B / i;
							yc = B;
							
							if(ok(xb, yb, xc, yc))
							{
								printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, xb, yb, xc, yc);
								
								return;
							}
						}
					}
				}
			}
		}
	}
	
	printf("Case #%d: IMPOSSIBLE\n", test);
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve(i);
	}
	
//	system("pause");
	
	return 0;
}
