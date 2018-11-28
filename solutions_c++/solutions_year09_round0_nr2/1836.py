#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>

#include <boost/regex.hpp>

using namespace std;

char evaluate(int **ap, char **bp, int h, int w, int i, int j, char &ch);
int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		int h, w;
		cin >> h >> w;
		int a[h][w];
		char b[h][w];

		int *ap[h];
		char *bp[h];
		//XXX  -- Read input --  XXX
		for(i=0; i<h; i++)
		{
			ap[i]=a[i];
			bp[i]=b[i];
			for(j=0; j<w; j++)
			{
				cin>>a[i][j];
				b[i][j]='\0';
			}
		}

		
		//XXX  -- Process input --  XXX
		char basin='a';
		for(i=0; i<h; i++)
		for(j=0; j<w; j++)
		{
			if (b[i][j]=='\0')
			{
				b[i][j]=evaluate(ap,bp,h,w,i,j,basin);
			}
		}


		//XXX  -- Print output --  XXX
		printf("Case #%d:\n",testId);
		for(i=0; i<h; i++)
		{
			for(j=0; j<w; j++)
			{
				cout << b[i][j];
				if (j<w-1) cout << " ";
			}
			cout << endl;
		}
	}

	return 0;
}

char evaluate(int **a, char **b, int h, int w, int i, int j, char &ch)
{
    //cout << "eval " << i << " " << j << endl;

	//North, West, East, South.
	int low_val=20000, low_h=-1, low_w=-1;
	if (i+1 < h && a[i+1][j]<a[i][j] && a[i+1][j] <= low_val) //south
	{
		low_val=a[i+1][j];
		low_h=i+1;
		low_w=j;
	}
	if (j+1 < w && a[i][j+1]<a[i][j] && a[i][j+1] <= low_val) //east
	{
		low_val=a[i][j+1];
		low_h=i;
		low_w=j+1;
	}
	if (j-1 >= 0 && a[i][j-1]<a[i][j] && a[i][j-1] <= low_val) //west
	{
		low_val=a[i][j-1];
		low_h=i;
		low_w=j-1;
	}
	if (i-1 >= 0 && a[i-1][j]<a[i][j] && a[i-1][j] <= low_val) //north
	{
		low_val=a[i-1][j];
		low_h=i-1;
		low_w=j;
	}

	char res;
	if (low_val==20000)//this itself is sink
	{
		res=ch;
		ch++;
		return res;
	}
	else if (b[low_h][low_w] != '\0')
	{
		return b[low_h][low_w];
	}
	else
	{
		b[low_h][low_w] = evaluate(a,b,h,w,low_h,low_w,ch);
		return b[low_h][low_w];
	}
}
