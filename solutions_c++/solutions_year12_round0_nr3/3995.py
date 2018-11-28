#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <deque>

using namespace std;

#define maxN 2000010

int ans;
bool Cont[maxN];
deque <int> D;


void valid (int X, int A, int B)
{	
	int KX = 0, cX = X, cX2 = X;
	int zece = 1;
	
	while (cX) cX /= 10, KX ++, zece *= 10;
	zece /= 10;
	
	for (int i = 1; i < KX; ++ i)
	{
		int ucx = X % 10;
		X /= 10;
		X += zece * ucx;
		
		if (X == cX2) continue;
		
		if (X < A || X > B) continue;
		if (cX2 < X && ! Cont[X])
		{
			++ ans;
			Cont[X] = true;
			D.push_back (X);
		}
	}
	
	while (! D.empty ())
	{
		int y = D.front();
		D.pop_front();
		Cont[y] = false;
	}
}


int main()
{
	freopen ("date.in", "r", stdin);
	freopen ("date.out", "w", stdout);
	
	int T;
	scanf ("%d", &T);
	
	for (int t = 1; t <= T; ++ t)
	{
		ans = 0;
		int A, B;
		
		scanf ("%d %d", &A, &B);
		
		for (int i = A; i <= B; ++ i) valid (i, A, B);
		printf ("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
