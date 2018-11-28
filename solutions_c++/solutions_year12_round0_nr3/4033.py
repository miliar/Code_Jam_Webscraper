/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/14/2012 18:21:16
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>


using namespace std;


int main(int argc, char ** argv)
{
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	int n;
	fin >> n;

	int i,j,k,len,base,m,ans,a,b;
	bool temp[3000000];
	memset(temp, true, sizeof(temp));
	int res[10];
	for (i = 1;i <= n;i ++)
	{
				
		fout << "Case #" << i << ": ";
		fin >> a >> b;
		base = 1;
		len = 0;
		k = a / 10;
		while (k > 0) {
			base = base * 10;
			len ++;
			k = k / 10;
		}
		ans = 0;

		for (j = a; j < b;j ++) {
			m = j;
			for (k = 0;k < len; k ++) {
				m = m / 10 + (m % 10) * base;
				if (j < m && a < m && m <= b && temp[m]) {
				  ans ++;
				  temp[m] = false;
				  res[k] = m;
				  
				}
			}
			for (k = 0;k < len;k ++) {
			  temp[res[k]] = true;
			}
		}
		fout << ans;
		fout << endl;
	}
	fin.close();
	fout.close();
    return 0;
}
