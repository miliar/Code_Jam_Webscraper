#include<iostream>
#include<stdio.h>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

/*
 * This program reads from stdin and writes to stdout.
 * Run it with
 *     program < input.txt > output.txt
 */

char INc[501][501];
long double  IN[501][501] , X[501][501] , Y[501][501] , M[501][501];

long double abs1(long double x)
{
	return (x > 0) ? x : -x;
}

int main()
{
    int T;
    cin >> T;
    for(int t = 0 ; t < T ; t++)
    {
        cerr << "Test " << t + 1 << "\n";
        int R , C , D;
        cin >> R >> C >> D;
        for(int i = 0 ; i < R ; i++)
        	cin >> INc[i];
        for(int i = 0 ; i < R ; i++)
        	for(int j = 0 ; j < C ; j++)
        		IN[i][j] = (INc[i][j] - '0') + D;
        for(int i = 0 ; i <= 500 ; i++)
        	X[0][i] = X[i][0] = Y[0][i] = Y[i][0] = M[0][i] = M[i][0] = 0;
        for(int i = 0 ; i < R ; i++)
        {
        	long double x = 0 , y = 0 , m = 0;
        	for(int j = 0 ; j < C ; j++)
        	{
        		x += IN[i][j] * j;
        		y += IN[i][j] * i;
        		m += IN[i][j];
        		X[i + 1][j + 1] = X[i][j + 1] + x;
        		Y[i + 1][j + 1] = Y[i][j + 1] + y;
        		M[i + 1][j + 1] = M[i][j + 1] + m;
        	}
        }
        /*for(int i = 0 ; i <= R ; i++)
        {
        	for(int j = 0 ; j <= C ; j++)
        		cerr << "(" << X[i][j] << " , " << Y[i][j] << " , " << M[i][j] << ")" << " ";
        	cerr << "\n";
        }*/
        bool flag = 0;
        for(int k = min(R , C) ; (k >= 3) && !flag ; k--)
        {
        	for(int i = 0 ; (i <= R - k) && !flag ; i++)
        		for(int j = 0 ; (j <= C - k) && !flag ; j++)
        		{
        			long double x = 0 , y = 0 , m = 0;
        			x += X[i + k][j + k]; y += Y[i + k][j + k]; m += M[i + k][j + k];
        			x -= X[i    ][j + k]; y -= Y[i    ][j + k]; m -= M[i    ][j + k];
        			x -= X[i + k][j    ]; y -= Y[i + k][j    ]; m -= M[i + k][j    ];
        			x += X[i    ][j    ]; y += Y[i    ][j    ]; m += M[i    ][j    ];
        			x -= IN[i        ][j        ] * (j    ); y-= IN[i        ][j        ] * (i    ); m -= IN[i        ][j        ];
        			x -= IN[i + k - 1][j        ] * (j    ); y-= IN[i + k - 1][j        ] * (i+k-1); m -= IN[i + k - 1][j        ];
        			x -= IN[i        ][j + k - 1] * (j+k-1); y-= IN[i        ][j + k - 1] * (i    ); m -= IN[i        ][j + k - 1];
        			x -= IN[i + k - 1][j + k - 1] * (j+k-1); y-= IN[i + k - 1][j + k - 1] * (i+k-1); m -= IN[i + k - 1][j + k - 1];
        			//cerr << i << " " << j << " " << k << " " << x << " " << y << " " << m << " " << x / m << " " << x / m << "\n";
        			if(     abs1(0.5 + x / m - (j + k / 2.0)) < 1e-5 &&
        					abs1(0.5 + y / m - (i + k / 2.0)) < 1e-5)
        			{
        				cout << "Case #" << t + 1 << ": " << k << "\n";
        				flag = 1;
        			}
        		}
        }
        if(!flag)
        	cout << "Case #" << t + 1 << ": IMPOSSIBLE\n";
    }
}





