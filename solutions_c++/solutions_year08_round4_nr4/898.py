#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;
char str[2000];
char perm_str[2000];


void test()
{	
	int o[4] = { 0,1,2,3};
	do
	{
		printf("%d %d %d %d\n",o[0],o[1],o[2],o[3]);
	}while  ( next_permutation( o , o+4) ) ; 

}

int main()
{
	int tn, casen= 1;
	scanf("%d",&tn);
	int min_pnt;
	while ( tn--)
	{
		int k ;  
		scanf("%d",&k);
		scanf("%s",str);
		int len = strlen(str);
		int o[5]={0,1,2,3,4};
		min_pnt = 10000000;
		do
		{
			int cur = 0 ; 
			string pstr;
			pstr="";
			if ( o[0]==0 && o[1]==2 &&o[2]==1 )
			{
				int dd;
				dd= 0 ; 
			}

			for ( int ngroup = 1; ngroup <= len/k ; ngroup++)
			{
				int ii  =0;
				for ( ; cur < k * ngroup; cur++,ii++)
				{
					int ccur = cur/k;
					perm_str[ii] = str[ccur*k+o[ii]]  ;
				}
				perm_str[ii]=0;
				pstr+= perm_str ; 
			}
			int pnt=1;
			for ( int i = 1 ; i < len ;i++)
			{
				if (pstr[i-1] != pstr[i] ) pnt++;
			}
			if ( pnt ==9 ) 
			{
				int cc;
				cc = 0 ; 
			}
			if ( min_pnt > pnt ) min_pnt= pnt;
		}while  ( next_permutation( o , o+k) ) ; 
		printf("Case #%d: %d\n",casen++,min_pnt);
	}
	return 0 ;
}

/*
2
4
abcabcabcabc
3
abcabcabcabc



021

*/
