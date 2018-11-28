#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;

double wp[101], owp[101], oowp[101];

int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d:\n", t);
        int N;
        cin >> N;
        string s[N];
        for(int i = 0; i < N; i++)
        {
            cin >> s[i];
        }
	double n, d;
        for(int i = 0; i < N; i++)
        {
            double n = 0, d = 0;
            for(int j = 0; j < N; j++)
            {
                if(s[i][j] != '.')
                    d++;
                if(s[i][j] == '1')
                    n++;
            }
            wp[i] = n / d;
       }
       for(int i = 0; i < N; i++) {
            n = 0, d = 0;
            for(int j = 0; j < N; j++)
            {
                if(s[i][j] != '.')
                {
                    double n1 = 0, d1 = 0;
                    for(int k = 0; k < N; k++)
                    {
                        if(k != i)
                        {
                            if(s[j][k] != '.')
                                d1++;
                            if(s[j][k] == '1')
                                n1++;
                        }
                    }
                    d++;
                    n += (n1 / d1);
                }
            }
            owp[i] = n / d;
     }
     for(int i = 0; i < N; i++) {
            n = 0, d= 0;
            for(int j = 0; j < N; j++)
            {
                if(s[i][j] != '.')
                {
                    d++;
                    n += owp[j];
                }
            }
            oowp[i] = n / d;
            
    }
for(int i = 0; i < N; i++)
cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
        }
    return 0;
}

