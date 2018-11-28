#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("B-large.in");
ofstream fout("b.out");


void check(int n, int m, int a)
{
	int i , j , left, k;
	for (i = 1;i <= n;i ++)
			for (j = (a - 1) / i + 1;j <= m; j ++)
			if (i * j >= a)
			{
				left = i * j - a;
				if (left == 0) {
					k = 0;
					cout << "0 "<< 0 << " " << i - k << " " << j << " " << i << " 0" << endl;
					return ;				
				}
				for (k = (left - 1) / j + 1;k <= i; k ++)
					if (left % k == 0 && left / k <= j) {
						cout << "0 "<< left / k << " " << i - k << " " << j << " " << i << " 0" << endl;
						return ;
					}
				for (k = 1;k <= n - i;k ++)
					if (left % k == 0 && left / k + j <= m) {
						cout << "0 " << left / k + j <<" " << i <<" " << j << " " << i + k <<" 0" << endl;
						return;
					}
			}
	cout << "IMPOSSIBLE" << endl;
}

int main()
{
	int num, c,  n , m, a;

	
	cin >> c;
	for (num= 1;num <= c;num ++)
	{
        cin >> n >> m >> a;
		cout << "Case #" << num << ": ";
		check(n, m ,a);
	}
	return 0;
}

