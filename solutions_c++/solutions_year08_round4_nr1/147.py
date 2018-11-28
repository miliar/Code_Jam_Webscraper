
#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("A-large.in");
ofstream fout("a.out");

const int maxm = 10005;

int t[maxm],c[maxm], b[maxm][2];


int check(int a, int b, int c)
{
    if (a < 0 || b < 0) return -1;

    return a + b + c;
}

int myMin(int a, int b)
{
    if (a < 0) return b;
    if (b < 0 || a < b) return a;
    return b;
}

int main()
{
    
	int num, n, m, v, i, j ,k;

	cin >> n;
	for (num= 1;num <= n;num ++)
	{
        cin >> m >> v;
        for (i = 1;i <= (m - 1) / 2;i ++)
          cin >> t[i] >> c[i];
        memset(b, -1, sizeof(b));
        
        for (i = (m - 1) / 2 + 1;i <= m;i ++) {
            cin >> t[i];
            b[i][t[i]] = 0;
        }
        
        for (i = (m - 1)/ 2;i>= 1;i --)
        {
            j = i * 2;
            k = i * 2 + 1;
            if (t[i] == 1) {
              b[i][1] = check(b[j][1], b[k][1], 0);
              b[i][0] = check(b[j][0], b[k][0], 0);
              b[i][0] = myMin(check(b[j][1],b[k][0], 0), b[i][0]);
              b[i][0] = myMin(check(b[j][0], b[k][1], 0), b[i][0]);
              if (c[i] == 1) {
                 b[i][0] = myMin(b[i][0], check(b[j][0], b[k][0], 1) );
                 b[i][1] = myMin(b[i][1], check(b[j][0], b[k][1], 1));
                 b[i][1] = myMin(check(b[j][1], b[k][0], 1), b[i][1]);
                 b[i][1] = myMin(check(b[j][1], b[k][1], 1), b[i][1]);
              }
            }
            else {
                 b[i][0] = check(b[j][0], b[k][0], 0);
                 b[i][1] = check(b[j][0], b[k][1], 0);
                 b[i][1] = myMin(check(b[j][1], b[k][0], 0), b[i][1]);
                 b[i][1] = myMin(check(b[j][1], b[k][1], 0), b[i][1]);
                 if (c[i] == 1) {
                   b[i][1] = myMin(b[i][1],  check(b[j][1], b[k][1],1));
                   b[i][0] = myMin(b[i][0], check(b[j][0], b[k][0], 1));
                   b[i][0] = myMin(check(b[j][1],b[k][0], 1), b[i][0]);
                   b[i][0] = myMin(check(b[j][0], b[k][1], 1), b[i][0]);
                          
                 }
            }
			//cout << i << " " << b[i][0] << " " << b[i][1] << endl;
        }
        cout << "Case #" << num << ": ";
        if (b[1][v] < 0) 
           cout << "IMPOSSIBLE" << endl;
        else 
           cout << b[1][v] << endl;
	}
	return 0;
}
