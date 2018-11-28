#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

char mat[55][55];
bool flag[130];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A_output.txt","w",stdout);

	int _kase,kase=0,n,i,j,k,ii,jj,kk;
	scanf("%d",&_kase);
	while( _kase-- )
	{
		scanf(" %d %d",&n,&k);
		for(j=n;j>=1;j--)
		{
			for(i=1;i<=n;i++)
			{
				scanf(" %c",&mat[i][j]);
			}
		}
/*
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				printf("%c",mat[i][j]);
			cout<<endl;
		}
*/
		for(i=n;i>=1;i--)
		{
			for(j=n;j>=1;j--)
			if( mat[i][j]=='.' )
			{
				for( ii=i; ii>1; ii--)
					if( mat[ii][j]!='.' )
						break;

				mat[i][j]=mat[ii][j];
				mat[ii][j]='.';
			}
		}
/*
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				printf("%c",mat[i][j]);
			cout<<endl;
		}
*/
		flag['B']=flag['R']=false;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			if( mat[i][j]!='.' && !flag[mat[i][j]] )
			{
				// same row
				if( n-j+1>=k )
				{
					ii=i;
					jj=j;
					for(kk=0;kk<k;kk++)
						if( mat[ii][jj++]!=mat[i][j] )
							break;

					if( kk==k )
					{
						flag[mat[i][j]]=true;
						continue;
					}
				}
				// same column
				if( n-i+1>=k )
				{
					ii=i;
					jj=j;
					for(kk=0;kk<k;kk++)
						if( mat[ii++][jj]!=mat[i][j] )
							break;

					if( kk==k )
					{
						flag[mat[i][j]]=true;
						continue;
					}
				}
				// diagonal1
				if( (n-j+1>=k) && (n-i+1>=k) )
				{
					ii=i;
					jj=j;
					for(kk=0;kk<k;kk++)
						if( mat[ii++][jj++]!=mat[i][j] )
							break;

					if( kk==k )
					{
						flag[mat[i][j]]=true;
						continue;
					}
				}
				// diagonal2
				if( (j>=k) && (n-i+1>=k) )
				{
					ii=i;
					jj=j;
					for(kk=0;kk<k;kk++)
						if( mat[ii++][jj--]!=mat[i][j] )
							break;

					if( kk==k )
					{
						flag[mat[i][j]]=true;
						continue;
					}
				}
			}
		}

		printf("Case #%d: ",++kase);
		if( flag['B'] && flag['R'] ) cout<<"Both"<<endl;
		else if( flag['B'] ) cout<<"Blue"<<endl;
		else if( flag['R'] ) cout<<"Red"<<endl;
		else cout<<"Neither"<<endl;
	}
	return 0;
}