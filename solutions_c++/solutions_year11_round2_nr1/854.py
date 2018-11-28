#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

int n;
char grid[100][100];
double wp[100][100];
double owp[100];
double oowp[100];

int main()	{

	int t;
	cin >> t;
	forp(0,t,z)	{
		
		cin >> n;
		forp(0,n,i)forp(0,n,j) cin >> grid[i][j];
		// wp
		forp(0,n,k)	{
			forp(0,n,i)	{
				double win = 0;
				double tot = 0;
				forp(0,n,j)	{
					if (j == k)
						continue;
					if (grid[i][j] == '0')
						tot++;
					else if (grid[i][j] == '1')	{
						win++;
						tot++;
					}
				}
				// wp of i without k
				wp[i][k] = win / tot;
			}
		}
		
		// owp
		forp(0,n,i)	{
			double tot = 0;
			double games = 0;
			forp(0,n,j)	{
				if (grid[i][j] != '.')	{
					games++;
					tot += wp[j][i];
				}
			}
			owp[i] = tot / games;
		}
	
		//oowp
		forp(0,n,i)	{
			double tot = 0;
			double games = 0;
			forp(0,n,j)	{
				if (grid[i][j] != '.')	{
					games++;
					tot += owp[j];
				}
			}
			oowp[i] = tot / games;
		}
		
		cout << "Case #" << (z+1) << ":" << endl;
		forp(0,n,i)	{
			double rpi = wp[i][i] + owp[i] * 2 + oowp[i];
			rpi /= 4;
// 			cout << rpi << endl;
			printf("%.10lf\n", rpi);
		}
	}
}