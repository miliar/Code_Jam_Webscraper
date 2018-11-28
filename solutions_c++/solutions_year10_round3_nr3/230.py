#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>
#include <list>
#define PI 3.14159265358979323846264338327950288
using namespace std;
int board[512][512];
int bc[513]={0};
int M,N;
int isboard(int size,int R,int C)
{
	int nextbit,i,j,k,RR,CC;
	if(board[R][C]==2)
	    return 0;
	else
	{
		nextbit=board[R][C];
		RR=R+size,CC=C+size;
		if(RR>M||CC>N)
		    return 0;
		for(i=R;i<RR;i++)
		{
			if(i!=R)
				nextbit=(board[i-1][C]+1)%2;
	    	for(j=C;j<CC;j++)
		    {
				if(board[i][j]!=nextbit||board[i][j]==2)
				    return 0;
				nextbit=(nextbit+1)%2;
			}
		}
	}
	for(i=R;i<RR;i++)
    	for(j=C;j<CC;j++)
			board[i][j]=2;
	return 1;
}
int main()
{
	int t,T,i,j,k,count,a,b;
	char temp;
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("CS.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("CL.out","w",stdout);
	cin>>T;
	int min;
	for(t=0;t<T;t++)
	{
		cin>>M>>N;
		min=N;
		for(i=0;i<513;i++) bc[i]=0;
		if(M<N) min=M;
		for(i=0;i<M;i++)
		{
			scanf("%c",&temp);
		    for(j=0;j<N/4;j++)
		    {
				cin>>temp;
				if(temp>='A')
				    temp=temp-55;
				else
				    temp=temp-0x30;
				for(k=0;k<4;k++)
				    board[i][j*4+k]=(temp>>(4-k-1))&1;
			}
		}
/*		cout<<endl;
		for(i=0;i<M;i++)
		{
		    for(j=0;j<N;j++)
		        cout<<board[i][j];
			cout<<endl;
		}*/
		for(k=min;k>=1;k--)
			for(i=0;i<M;i++)
			    for(j=0;j<N;j++)
		    	{
//					R=i;C=j;
					if(isboard(k,i,j))
					    bc[k]++;
/*		          	cout<<endl<<"Size "<<k<<"count "<<bc[k]<<endl;
					for(a=0;a<M;a++)
					{
		    			for(b=0;b<N;b++)
					        cout<<board[a][b];
						cout<<endl;
					}*/
				}
		count=0;
		for(i=min;i>=1;i--)
			if(bc[i]!=0)
		    	count++;
/*      	cout<<endl;
		for(i=0;i<M;i++)
		{
		    for(j=0;j<N;j++)
		        cout<<board[i][j];
			cout<<endl;
		}*/
		cout<<"Case #"<<t+1<<": "<<count<<endl;
		for(i=min;i>=1;i--)
			if(bc[i]!=0)
		    	cout<<i<<" "<<bc[i]<<endl;
	}
	return 0;
}
