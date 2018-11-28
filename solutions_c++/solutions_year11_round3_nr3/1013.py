#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
#include<iostream>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))
int GCD(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

typedef long long ll;
int n;
int l,h;
int so[10001];
int main() {
    int e = 0, T;

    scanf("%d",&T);
	int g;
    while(T--) {
        scanf("%d%d%d",&n,&l,&h);
		g = -1;
		for ( int i = 0 ; i < n; ++i){
			scanf("%d",&so[i]);
		}
		for ( int i = l ; i <=h ; ++i)
		{
			bool check=true;
			for ( int j = 0 ; j < n ; ++j)
			{
				if ( i>=so[j] && i % so[j] !=0 || i<=so[j] && so[j] % i !=0)
				{
					check=false;
					break;
				}
			}
			if (check){
				g = i;
				break;
			}
		}

		printf("Case #%d: ", ++e);
		if ( g != -1 )
			printf("%d\n", g);
		else{
			printf("NO\n");
		}
// NO or number		printf("\n", ++e);
    }
    return 0;
}

