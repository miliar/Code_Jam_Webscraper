#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
int L,D,N,i,k,j,coun[550][450],chk,cnt,y,test;
char str[1000],arra[5002][20];
int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d %d %d",&L,&D,&N);

		for(i = 0 ; i < D ; i++ )
			scanf("%s",arra[i]);
		for(i = 0 ; i < N ; i++ )
		{
			scanf("%s",str);
			k=0;chk=1;
			for(j=0;str[j]!=NULL;j++)
			{
				if(str[j]==')' )k++,chk=1;
				else if(isalpha(str[j]))
				{
					coun[k][str[j]-97]=1;
					if(chk)k++;
				}
				if(str[j]=='(')chk=0;
			}
			if(!k)k++;
			/*for(y=0;y<k;y++)
				for(j=0;j<5;j++)
					printf("coun[ %d ][ %d ] = %d\n",y+97,j+97,coun[y][j]);*/
			for(j = chk = 0 ; j < D ; j++ )
			{
				for( y = cnt = 0 ; y < k ; y++ )
				{
					if( coun [ y ][ arra[ j ][ y ] - 97 ] )
						cnt++;
					else
					{
						y++;break;
					}
				}
				if( cnt == y )chk++;
			}
			printf("Case #%d: %d\n",++test,chk);
			for(y=0;y<k;y++)
				for(j=0;j<27;j++)coun[y][j]=0;

	}
	return 0;
}






















/*for(y=0;y<k;y++)
				for(j=0;j<5;j++)
					printf("coun[ %d ][ %d ] = %d\n",y+97,j+97,coun[y][j]);*/
