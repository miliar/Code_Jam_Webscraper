#include <iostream>
#include <cstring>
using namespace std;

int a[10000];
int used[10000];
int n, res;
int go (int pos, int f, int l, int to, int left)
{
	
	if (left == 0) return 0;
	
	res += used[pos] == 0; used[pos] = 1;
	
	int mid = (f + l) / 2;
	if (to <= mid) go (2*pos , f, mid , to , left - 1);
	else
		go (2*pos+1 , mid+1, l , to , left - 1);
		
}

void solve ()
{
		memset (used, 0, sizeof (used));
scanf ("%d", &n);

	int i;	
	//int Min = n;
	res = 0; int o;  
	 for (i = 0 ; i < (1<<n); i ++)
	 {
		 scanf ("%d", &a[i]);
	 go (1, 1, (1<<n), i + 1,  n - a[i]);
	 
	 }
	
	
	 for (i = 0 ; i < (1<<n) - 1; i ++)
	 {
		 scanf ("%d", &o);
//		 Min = min (Min, a[i]); 
	 }

	 
	 
	 
	 cout << res<< endl;
	// cout << n - Min << endl;
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