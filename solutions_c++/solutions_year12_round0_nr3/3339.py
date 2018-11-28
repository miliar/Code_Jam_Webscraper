#include <stdio.h>
#include <string.h>
char bufA[32];
char bufB[32];
char bufC[32];
bool check(int n,int m)
{
	memset(bufA,0,sizeof(bufA));
	memset(bufB,0,sizeof(bufB));
	sprintf(bufA,"%d",n);
	sprintf(bufB,"%d",m);
	int lenA = strlen(bufA);
	int lenB = strlen(bufB);
	if( lenA != lenB )
		return false;
	for( int step=1; step < lenA ; ++ step)
	{
		memcpy(bufC,bufA+step,lenA-step);
		memcpy(bufC+lenA -step,bufA,step);
		bufC[lenA] = 0 ;
		if( !strcmp(bufC,bufB))
		{
		//	printf("%s\n",bufC);
			return true;
		}
	}
	return false;
}
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c_out.txt","w",stdout);
	int T;
	int A,B;
	int R = 0;
	scanf("%d",&T);
	
	for(int i = 1; i <= T ; i ++ )
	{
		R = 0 ;
		scanf("%d%d",&A,&B);
		for( int j=A; j<=B; ++j )
		{
			for( int k = j+1; k<=B; ++k )
			{
				
				if( check(j,k))
				{
					//printf("%d %d\n",j,k);
					++ R;
				}
			}
		}
		printf("Case #%d: %d\n",i,R);
	}
	return 0;
}