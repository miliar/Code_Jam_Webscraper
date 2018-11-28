#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t, n, s, p, w, x ,y ,z, count;
	bool flag;
	scanf("%d",&t);

	for( int a = 1; a <= t; a ++ ) {
		scanf("%d %d %d",&n,&s,&p);
		count = 0;
		for( int b = 0; b < n; b ++ ) {
			scanf("%d",&w);
			flag = true;
			x = w / 3;
			y = (w - x) / 2;
			z = (w - x - y);
			if( x >= p || y >= p || z >= p ) {
				count ++;
				flag = false;
			}

			if( p > 1 && flag == true && s > 0 ) {
				if( z == p-1 && y == p-1 && x >= p-2 ) {
					count ++;
					s --;
				}
			}
		}
		cout << "Case #" << a << ": " << count << endl;
	}
	return 0;
}
