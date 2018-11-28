#include <iostream>
#include <set>
#include <cstring>
using namespace std;

#define mp make_pair

int a1[128][128];
int a2[128][128];

 
int n;
void solve () 
{
	
	memset (a1, 0, sizeof (a1));
	
	cin >> n;
	
	int i ;
	int x, y;
	for (i = 0; i < n; i++)
	{
		int u1, v1, u2, v2;
		scanf ("%d%d%d%d", &u1, &v1, &u2, &v2);
		
		for (x = u1; x <= u2; x ++)
		for (y = v1; y <= v2; y ++)
				a1[x][y] = 1;
			
	}
	 
	int change = 1;
	
	int res = 0, j;
	while (change)
	{
		memset (a2, 0, sizeof (a2));
		
		change = 0; 
		
		for (i = 1; i < 128; i ++)
			for (j = 1; j < 128; j ++)
				if (a1[i-1][j] && a1[i][j-1]) a2[i][j] = 1, change =  1; 
				else
					if (a1[i][j] && (a1[i-1][j] || a1[i][j-1])) a2[i][j] = 1, change =  1;
		/*
		for (i = 1; i < 7; i ++)
		{
			for (j = 1; j < 7; j ++)
				cout << a1[i][j];
			cout << endl;
			}
			cout << "-------------\n";
		*/
		res ++;
		
		memcpy (a1 , a2, sizeof (a1));
	}
	
	
	cout << res << endl; 
	 
}


int main ()
{
	
	int o;
	
	scanf ("%d", &o);
	
	int i;
	for (i =1; i <= o; i++)
	{
		printf ("Case #%d: ", i);
		solve ();
	}
	
	
	return 0; 
	
	
}