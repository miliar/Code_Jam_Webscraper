#include<iostream>
#include<stdio.h>

#define MAX 55
#define T(a,b) Table[a][b]

using namespace std;

int N,K;
int Table[MAX][MAX];

int Control(int a,int b,char c)
	{
	int flag=0;
	for(int i=a; i>a-K && i>=0; i--)
		if(T(i,b)==c)flag++;
	
	if(flag==K)return 1;
	
	flag=0;
	for(int i=b; i<b+K && i<N; i++)
		if(T(a,i)==c)flag++;
	
	if(flag==K)return 2;
	
	flag=0;	
	for(int i=a, j=b; i>a-K && i>=0 && j<b+K && j<N; i-- , j++)
		if(T(i,j)==c)flag++;
	
	if(flag==K)return 3;
	
	flag=0;	
	for(int i=a, j=b; i>a-K && i>=0 && j>b-K && j>=0; i--, j--)
		if(T(i,j)==c)flag++; 
	
	if(flag==K)return 4;
	return 0;
	}

int Solve()
	{
	char c;
	int x=0,y=0;
	int a,b;
	for(int i=0; i<N; i++)
		{
		for(int j=0; j<N; j++)
			{
			if(T(i,j)!='.')
				if(Control(i,j,T(i,j)))
					{
					a=i;b=j;c=T(i,j);
					if(c=='R')
						y=2;
					else
						x=1;
					break;	
					}
			}
		if(x || y)break;
		}
	
	for(int i=a; i<N; i++)
		{
		for(int j=0; j<N; j++)
			{
			if(T(i,j)!='.' && T(i,j)!=c)
				if(Control(i,j,T(i,j)))
					{
					a=i;b=j;
					if(T(i,j)=='R')
						y=2;
					else
						x=1;
					break;	
					}
			}
		if(x && y)break;
		}				
	
	return x+y;
	}

void Rotate()
	{
/*	char temp[MAX][MAX];
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
			temp[j][i]=T(i,j);
	
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
			T(i,j)=temp[i][j];
	*/
	int a,b;
	for(int i=0; i<N; i++)
		{
		a=b=N-1;
		
		while(b>=0)
			{
			if(T(i,b)=='.')b--;
			else
				{
				T(i,a)=T(i,b);
				if(a!=b)T(i,b)='.';
				a--, b--;
				}
			}
		}	
	/*
	for(int a=0; a<N; a++,cout<<endl)
			for(int b=0; b<N; b++)
				printf("%c",T(a,b));
	cout<<endl;*/
	}

int main()
	{
	int T;
	char result[4][10] = {"Neither","Blue","Red","Both"};
	int x,y;
	cin>>T;
	
	for(int i=1; i<=T; i++)
		{
		cin>>N>>K;
		for(int a=0; a<N; a++)
			for(int b=0; b<N; b++)
				scanf(" %c ",&T(a,b));
		x=Solve();
		Rotate();
		y=Solve();
		
		cout<<"Case #"<<i<<": ";
		if(x!=y)printf("%s\n",result[x+y]);
		else printf("%s\n",result[x]);
		}
	return 0;
	}
