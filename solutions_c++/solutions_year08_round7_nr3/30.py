#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("C-small-attempt1.in");
ofstream fout("c.out");

const int maxt = (2 << 14);
double t[maxt], p[7][4];
int num, m, q;

void calp(int dep, double tmp)
{
	int i;
	if (dep >= q) {
		t[num] = tmp;
		num ++;
		return;
	}
	//if (dep > 7) cout <<" error" << endl;
	for (i =0;i < 4;i ++) {
		if (p[dep][i] == 0) continue;
		
		calp(dep + 1, tmp + log(p[dep][i]));			
	}
		
}
int main()
{
	int c, k, i, j;
	double r, tmp;
	cin >> c;
	for (k = 1;k <= c;k ++)
	{
		cin >> m >> q;
		for (i = 0;i < q;i ++)
			for (j = 0;j < 4;j ++)
				cin >> p[i][j];
		num = 0;
		calp(0, 0);
		r = 0;
		for (i = 0;i < num;i ++)
		{
		//	cout << t[i] << endl;
			for (j = i + 1;j < num;j ++)
				if (t[i] < t[j]) {
					tmp = t[i];
					t[i] = t[j];
					t[j] = tmp;
				}
		}
		for (i = 0;i < m && i < num;i ++)
			r += exp(t[i]);
		cout << "Case #" << k <<": " << r << endl;
	}
    
    return 0;
}
