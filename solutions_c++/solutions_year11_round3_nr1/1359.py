#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <climits>
#include <cstdlib>
using namespace std;

#define pi (2 * acos(0))
#define eps 1e-9
#define li(v) v.begin(),v.end()
#define fo(i,j,n) for(i=j; i<n; ++i)

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned uint32;

int main()
{
	 freopen("A-large(1).in", "r", stdin);
	 freopen("largea.txt", "w", stdout);
	 int t, cno = 1;
	 scanf("%d%*c",&t);
	 while(t--)
	 {
              int cnt = 0;
	 int r, c;
	 scanf("%d%*c%d%*c",&r,&c);
	 char ch[r][c];
	 for(int i = 0; i < r; i++)
	 {
				for(int j = 0; j < c; j++)
				{
						 
						  scanf("%c",&ch[i][j]);
		  		}
		  		scanf("%*c");
	 }
	 for(int i = 0; i < r; ++i)
	 {
				for(int j = 0; j < c; j++)
				        if(ch[i][j] == '#'){cnt++;}
	 }
	 
	 
	 
	 for(int i = 0; i < r - 1; ++i)
	 {
				for(int j = 0; j < c - 1; j++)
				{

						 if(ch[i][j] == '#' && ch[i][j + 1] == '#' && ch[i + 1][j] == '#' && ch[i + 1][j + 1] == '#')
						 {
									ch[i][j] = '/';
									ch[i][j + 1] = '\\';
									ch[i + 1][j] = '\\';
									ch[i + 1][j + 1] = '/';
  				 		 }
				}
	 }
	 printf("Case #%d:\n", cno++);
	 bool flag1 = false;
	 for(int i = 0; i < r; ++i)
	         for(int j = 0; j < c; j++)
	                 if(ch[i][j] == '#'){flag1 = true; break;}
	 //printf("%d\n",cnt);
	 if(flag1){printf("Impossible\n");continue;}
	 else if(cnt % 4 != 0){printf("Impossible\n");continue;}
	 else
	 {
		  for(int i = 0; i < r; ++i)
		  {
		          for(int j = 0; j < c; ++j)
		          {
								printf("%c",ch[i][j]);
 					 }
 					 printf("\n");
					 }
  	 }
	 }
	 return 0;
}
