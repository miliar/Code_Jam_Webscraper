#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <iostream>
#include <fstream>

using namespace std;

int f[1005][1005];

void Three() 
{ 
    int i,j,k;
	f[0][0]=1;
	for (i=0;i<=505;++i) 
	{
		f[0][i]=1;
		f[i][0]=0;
	}
	f[0][0]=1;
	for (i=1;i<=505;++i) 
	{
		for (j=1;j<=505;++j) 
		{
			for (k=1;k<=j && k<=i;++k)
			{
				f[i][j]+=f[i-k][j];
				f[i][j]%=100003;
			}
		}
	}
}



int main() 
{
    int z, i ,j,zz,ans;

	//FILE * fp = ( "d:\\in.in" , "r" );
    freopen("d:\\in.in","r",stdin);
	freopen("d:\\three","w",stdout);
    
	Three();
	int answer[505];
	for(   i = 1 ; i <= 500 ; i ++ )
	{
		for (j=answer[i]=0;j<i;++j) 
		{
			answer[i]+=f[i-1-j][j];
			answer[i]%=100003;
		}
	}

	for (scanf("%d",&zz),z=1;z<=zz;++z) 
	{
		scanf("%d",&i);
		printf("Case #%d: %d\n",z,answer[i]);
	}
    

	
	
	return 0;
}