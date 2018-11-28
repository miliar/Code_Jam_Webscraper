#include"cstdio"
#include"iostream"
#include"cstring"
#include"algorithm"
#include"cmath"

using namespace std;

bool Judge(int p , int q)
{
	if((int)log10(p) != (int)log10(q)) return false;
	int x = (int)log10(p) + 1;
	for(int i = x - 1 ; i > 0 ; i--)
	{
		int tmp = 1 , multi = 1;
		for(int j = 1 ; j <= x - i ; j++) tmp *= 10;
		for(int j = 1 ; j <= i ; j++) multi *= 10;
		if((p % tmp) * multi + (p - (p % tmp)) / tmp == q) return true;
	}
	return false;
}

int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n , a , b;
	scanf("%d\n" , &n);
	
	for(int i = 1 ; i <= n ; i++)
	{
		scanf("%d %d\n" , &a , &b);
		
		int ans = 0;
		for(int p = a ; p <= b ; p++)
			for(int q = p + 1 ; q <= b ; q++)
				ans += Judge(p , q);
				
		printf("Case #%d: %d\n" , i , ans);
	}
}
