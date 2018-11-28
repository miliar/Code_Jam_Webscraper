#include<iostream>
#include<cmath>
using namespace std; 

int ts, no;
int n, m, id; 
int d[110][3]; 
double ans; 

double cal(int x, int y)
{
	double ret=sqrt((d[x][0]-d[y][0])*(d[x][0]-d[y][0])+
					(d[x][1]-d[y][1])*(d[x][1]-d[y][1])); 
	ret = (ret+d[x][2]+d[y][2])/2; 
	return ret; 
}

main() {
	freopen("d0.in", "r", stdin);
	freopen("4.out", "w", stdout);

	cin >> ts;
	for (int no=0; no<ts; no++) {
		cin >> n;
		ans = 0; 
		for( int i=1; i<=n; i++ )
		{
			cin >> d[i][0] >> d[i][1] >> d[i][2];
			ans >?= d[i][2];
		}
		if (n == 3)
		{
		ans = max(cal(1, 2), double(d[3][2])); 
		ans <?= max(cal(2, 3), double(d[1][2])); 
		ans <?= max(cal(1, 3), double(d[2][2])); 
		}
		printf("Case #%d: %.8lf\n", no+1, ans);
	}
}
