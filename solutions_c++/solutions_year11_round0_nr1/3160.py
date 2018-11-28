#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int n;
char player[150];
int bottom[150];

void solve(int id)
{
	scanf("%d ", &n);
	for (int i = 0; i < n; i++)
	 	scanf("%c %d ", &player[i], &bottom[i]);
	int ans, k = 0;
	int O, B, nO, nB;
	O = B = 1;
	nO = nB = -1;
	for (int i = 0; i < n; i++)
	{
		if (player[i] == 'O')
			if (nO == -1) nO = bottom[i];
		if (player[i] == 'B') 	
			if (nB == -1) nB = bottom[i];
	}
	for (ans = 1; ; ans++)
	{
		switch (player[k])
		{
		 	case 'O': 
		 	{
		 		if (bottom[k] == O) 
		 		{
		 			k++;
		 			int i = k;
		 			while (i < n && player[i] != 'O') i++;
		 			if (i == n) goto here;
		 			nO = bottom[i];
		 		}
		 		else
		 		{ 
		 			if (O < nO && nO != -1) O++;
		 			if (O > nO && nO != -1) O--;	
		 		}	
		 		here:{};
		 		if (B < nB && nB != -1) B++;
		 		if (B > nB && nB != -1) B--;
		 	 	break;
			}
			case 'B':
			{
			   	if (bottom[k] == B)
			   	{
			   	 	k++;
			   	 	int i = k;
			   	 	while (i < n && player[i] != 'B') i++;
			   	 	if (i == n) goto here2;
			   	 	nB = bottom[i];
			   	}
			   	else 
			   	{
			   		if (B < nB && nB != -1) B++;
			   		if (B > nB && nB != -1) B--;
			   	}
			   	here2:{};
			   	if (O < nO && nO != -1) O++;
			   	if (O > nO && nO != -1) O--;
				break;
			}
		}
		if (k == n) break;	 	
	}
	printf("Case #%d: %d\n", id, ans);
}

int main() 
{
 	freopen("A.in", "r", stdin);
 	freopen("A.out", "w", stdout);

	int test; scanf("%d\n", &test);
	for (int i = 1; i <= test; i++)
		solve(i);

 	return 0;
}
