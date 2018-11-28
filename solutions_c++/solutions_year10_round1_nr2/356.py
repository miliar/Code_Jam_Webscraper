/*
Problem
You have a one-dimensional array of N pixels. Each pixel has a value, represented by a number between 0 and 255, inclusive. The distance between two pixels is the absolute difference of their numbers.


You can perform each of the following operations zero or more times:


With cost D, delete any pixel, so its original neighbors become neighboring pixels.

With cost I, insert one pixel of any value into any position -- either between two existing pixels, or before the first pixel, or after the last pixel.

You can change the value of any pixel. The cost is the absolute difference of the old value of the pixel and the new value of the pixel. 

The array is smooth if any neighboring pixels have distance at most M. Find the minimum possible cost of a sequence of operations that makes the array smooth. 

Note: The empty array -- the array containing no pixels -- is considered to be smooth. 

Input
The first line of the input gives the number of test cases, T. T test cases follow, each with two lines. The first line is in the form "D I M N", the next line contains N numbers ai: the values of the pixels from left to the right. 

Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the minimum cost to make the input array smooth. 

Limits
All the numbers in the input are integers.
1 ¡Ü T ¡Ü 100
0 ¡Ü D, I, M, ai ¡Ü 255


Small dataset
1 ¡Ü N ¡Ü 3. 

Large dataset
1 ¡Ü N ¡Ü 100. 

Sample

Input 
   
Output 
   
2
6 6 2 3
1 7 5
100 1 5 3
1 50 7
 Case #1: 4
Case #2: 17

 

Explanation
In Case #1, decreasing the 7 to 3 costs 4 and is the cheapest solution. In Case #2, deleting is extremely expensive; it's cheaper to insert elements so your final array looks like [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 50, 45, 40, 35, 30, 25, 20, 15, 10, 7]. 


*/

#include <stdio.h>
#include <string.h>
#include <math.h>

int C;

int b[100];
long a[100][300];
int c[100][300];

int D,I,M,n;

int delta(int i,int j)
{
	return i>j?i-j:j-i;
}

int main()
{
//	freopen("b.txt","r",stdin);
	freopen("B-small-attempt0.in.txt","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&C);
	int i,j,k,l;
	int tt;
	int cost;
	int cost_i;
	long ans;
	
	for (tt=1;tt<=C;tt++)
	{

		scanf("%d %d %d %d",&D,&I,&M,&n);

		memset(b,0,sizeof(b));
		memset(a,127,sizeof(a));
		for (i=0;i<n;i++)
		{
			scanf("%d",&b[i]);
		}

		for (j=0;j<=255;j++)
		{
			a[0][j]=delta(j,b[0]);
		}
		a[0][256]=D;



		for (i=1;i<n;i++)
		{
			for (j=0;j<=255;j++)
			{
				for (k=0;k<=255;k++)
				{
					if (M>0)
					{
						cost=delta(k,b[i])+a[i-1][j];
						if (delta(j,k)>M)
						{
							cost+=I*ceil(double(delta(j,k))/M-1);
						}
						if (cost<a[i][k]) a[i][k]=cost;
					}
					else if (M==0)
					{
						//M==0
						if (j!=k)
						{
							continue;
						}
						else
						{
							cost=delta(k,b[i])+a[i-1][j];
							if (cost<a[i][k]) a[i][k]=cost;
						}
					}


				}

				//delete b[i]
				// n - 256
				cost=a[i-1][j]+D;
				if (cost<a[i][j])
				{
					a[i][j]=cost;
				}

			}


			// 256 - n
			for (k=0;k<=255;k++)
			{
				cost=a[i-1][256]+delta(b[i],k);
				if (cost<a[i][k])
				{
					a[i][k]=cost;
				}
			}

			// 256 - 256
			cost=a[i-1][256]+D;
			if (cost<a[i][256])
			{
				a[i][256]=a[i][j];
			}

		}

		ans=a[n-1][256];
		for (k=0;k<=255;k++)
		{
			if (a[n-1][k]<ans)
			{
				ans=a[n-1][k];
			}
		}

		printf("Case #%d: %d\n",tt,ans);


//		if (i) printf(" ON\n"); else printf(" OFF\n");
		
	}

	return 0;
}
