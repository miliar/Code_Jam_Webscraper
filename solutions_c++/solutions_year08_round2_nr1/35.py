#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 17;

typedef long long ll;

int n;
long long a , b , c , d , x , y , m;
int t[MAXN][2];
int f[3][3];

void read() {
	int i;
	
	scanf ("%d",&n);
	scanf ("%lld%lld%lld%lld%lld%lld%lld",&a,&b,&c,&d,&x,&y,&m);
	
	t[1][0] = (int)x;
	t[1][1] = (int)y;
	
	t[1][0] %= 3;
	t[1][1] %= 3;
	
	for (i=2;i<=n;i++) {
		x = (a * x + b) % m;
		y = (c * y + d) % m;
		
		t[i][0] = (int)x;
		t[i][1] = (int)y;
		
		t[i][0] %= 3;
		t[i][1] %= 3;
	}
}

void slow() {
	int i , j , k;
	int ans = 0;

	for (i=1;i<=n;i++)
		for (j=i+1;j<=n;j++)
			for (k=j+1;k<=n;k++)
				if ( (t[i][0] + t[j][0] + t[k][0]) % 3 == 0 && (t[i][1] + t[j][1] + t[k][1]) % 3 == 0 )
					++ ans;
	
	printf ("%d\n",ans);
}

void fast() {
	f[0][0] = f[0][1] = f[0][2] = f[1][0] = f[1][1] = f[1][2] = f[2][0] = f[2][1] = f[2][2] = 0;
	int i , j , k , d , e , q;
	long long ans = 0;
	
	for (i=1;i<=n;i++) 
		++ f[ t[i][0] ][ t[i][1] ];
	
	for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			for (k=0;k<3;k++)
				for (d=0;d<3;d++)
					for (e=0;e<3;e++)
						for (q=0;q<3;q++)
							if ( !((i + j + k) % 3)&& !((d + e + q) % 3) ) {
						//		printf ("--%d %d       %d %d        %d %d\n",i,d,j,e,k,q);
								if ( i == j && j == k && d == e && e == q )
									ans += max ( 0LL , (ll)f[i][d] * (ll)(f[j][e] - 1) * (ll)(f[k][q] - 2));
								else
									if ( (i == j && d == e) || (i == k && d == q) )
										ans += max ( 0LL, (ll)(f[i][d] - 1) * (ll)f[j][e] * (ll)f[k][q] );
									else
										if ( j == k && e == q )
											ans += max ( 0LL , (ll)f[i][d] * (ll)f[j][e] * (ll)(f[k][q] - 1) );
										else {
							//				printf ("%d %d       %d %d        %d %d\n",i,d,j,e,k,q);
											ans += (ll)f[i][d] * (ll)f[j][e] * (ll)f[k][q];
										}
							}
	
	printf ("%lld\n",ans/6);
}

int main() {
	int k;
	int i;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		printf ("Case #%d: ",i);
		read();
		fast();
	}
	
	return 0;
}
