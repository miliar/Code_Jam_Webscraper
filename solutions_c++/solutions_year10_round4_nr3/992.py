#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

ifstream in("easy.in");
ofstream out("easy.out");
int a[1000][1000];
int b[1000][1000];
bool zero(int n)
{
	int i,j;
	for(i = 1;i < n; ++i)
		for(j = 1;j < n; ++j)
			if(a[i][j] == 1)
				return false;
	return true;
}
int main()
{
	int test_count;
	int test_it;
	int r,i,j,x,y;
	int k;
	int w,h;
	int sec = 0;
	int x_start, x_end, y_start, y_end;
	in >>  test_count;
	for(test_it = 0; test_it < test_count ; ++ test_it)
	{
		for(i = 0; i < 1000 ; ++ i)
			for(j = 0; j < 1000 ; ++ j)
				a[i][j] = 0;
		w = 0;
		h = 0;
		sec = 0;
		in >> r;
		for(k = 0 ; k < r ; k ++)
		{
			in >> y_start >> x_start >> y_end>> x_end;
			w = max(x_start,max(w,x_end));
			h = max(y_start,max(h,y_end));
			for(i =x_start ; i <= x_end; ++ i)
				for(j = y_start; j <= y_end; ++ j)
					a[i][j]=1;
		}

		w ++;
		h ++;

		while(!zero(max(w,h)))
		{
			for(i = 1; i <= w ; ++ i)
				for(j = 1; j <= h ; ++ j)
				{
					if(a[i-1][j]==1 && a[i][j-1]==1)
					{
						b[i][j]=1;
					}
					else
					if(a[i-1][j]==0 && a[i][j-1]==0)
					{
						b[i][j]=0;
					}
					else
						b[i][j] = a[i][j];
				}
				for(i = 1; i <= w ; ++ i)
					for(j = 1; j <= h  ; ++ j)
						a[i][j] = b[i][j];
			sec++;
		}
		out << "Case #" << test_it + 1 << ": " << sec << endl;
	}
	return 0;
}