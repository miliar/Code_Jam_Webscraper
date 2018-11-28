#include <iostream>

char s[41];
int a[41];

bool check(int *a , int n)
{
	int i;
	for( i = 0 ; i < n ; i++)
		if(a[i] > i)return false;
	return true;
}

int bubble_sort(int *a , int n)
{
	int i , j , t, cn = 0;
	n--;
	while(n>0)
	{
		j = 0;
		if(check(a , n)) return cn;
		for( i = 0 ; i < n ; i++)
		{

			if( a[i] > a[i+1] )
			{
				std::swap(a[i] , a[i+1]);
				cn++;
				j = i;
			}

		}
		n = j;
	}
	return cn;
}

int bubble_sort2(int *a , int n)
{
	int i , j , t, cn = 0;

	for( i = n - 1 ; i >= 0 ; i--)
	{
		for( j = 0 ; j <= i - 1  ; j++)
		{
			if(check(a , n)) return cn;
			if( a[j] > a[j+1] )
			{
				std::swap(a[j] , a[j+1]);
				cn++;
			}
		}
	}
	return cn;
}

int bubble_sort1(int *a , int n)
{
	int i , j , t, k , cn = 0;

	for( i = 0 ; i < n  ; i++)
	{
		if( a[i] > i )
		{
			for( j = i + 1 ; j < n ; j++)
				if( a[j] <= i )break;
			t = a[j];
			for( k = j ; k>= i + 1 ; k--)
				a[k] = a[k-1];
			a[i] = t;
			cn += ( j - i );
		}
	}
	return cn;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int n , t , ca;
	scanf("%d" , &t);
	for( ca = 1 ; ca <= t ; ca++)
	{
		scanf("%d" , &n);
		int i , j;
		for( i = 0 ; i < n ; i++)
		{
			scanf("%s" , s);
			for( j =  n - 1 ; j >= 0  ; j--)
				if(s[j] == '1' )break;
			a[i] = j;
		}
		int re = bubble_sort1( a , n);
		printf("Case #%d: %d\n" , ca , re);

	}
	return 0;
}

/*

5
2
10
11
3
001
100
010
4
1110
1100
1100
1000
3
010
100
000
3
001
010
000

*/