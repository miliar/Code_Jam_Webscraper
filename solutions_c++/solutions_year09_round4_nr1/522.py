#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <iomanip>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <sstream>
#include <strstream>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

char a[45][45];
int last[45];

int main()
{
	int test,i,j,lst,t,n,verj,k;
	in >> test;
	for (t=1;t<=test;t++)
	{
		in >> n;
		for (i=0;i<n;i++)
		{
			lst = 0;			
			in >> a[i];
			for (j=0;j<n;j++)			
				if (a[i][j] == '1')
					lst = j;
			last[i] = lst;			
		}				
		int answer = 0;
		for (i=0;i<n;i++)
			if (last[i] > i)
			{
				for (j=i+1;j<n;j++)
					if (last[j] <= i)
					{
						verj  = last[j];							
						for (k=j;k>i;k--)
							last[k] = last[k-1];
						last[i] = verj;						
						answer += (j-i);
						break;
					}
				/*cout << answer << endl;
				for (j=0;j<n;j++)
					cout << last[j] << " ";
				cout << endl;*/
			}		
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}
