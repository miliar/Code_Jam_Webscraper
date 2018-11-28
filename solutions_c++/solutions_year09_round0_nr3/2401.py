#include<iostream>
#include<cstring>

#define NMAX 502
#define T(a,b) Table[a][b]

#define P(a,b) Place[a][b]
#define N(a) Number[a]

using namespace std;

char Str[]=" welcome to code jam";
int Table[20][NMAX];
int N,M=19,Tx;
char Line[NMAX];
	
void yaz()
	{
	for(int i=1; i<=Tx; i++)
		printf("%c ",Line[i]);printf("\n");
	for(int i=1; i<=M; i++,printf("\n"))
		for(int j=1; j<=Tx; j++)
			printf("%d ",T(i,j)); 
	}	
	
int Count()
	{
	for(int j=1; j<=Tx; j++)
		T(1,j) = (Str[1]==Line[j]) ? T(1,j-1)+1 : T(1,j-1);
	
//	yaz();
	
	for(int i=2; i<=M; i++)
		{
		for(int j=1; j<=Tx; j++)
			T(i,j) = (Str[i]==Line[j]) ? (T(i,j-1)+T(i-1,j-1))%1000 : T(i,j-1);
		if(T(i,Tx)==0)return 0;
		}
//	yaz();	
	return T(M,Tx);
	}	
	
int main()
	{
	cin>>N;
	
	for(int i=0; i<N; i++)
		{
		scanf(" %[^\n]",Line);
		int t=strlen(Line);
		Tx=t;
		while(t)
			{
			Line[t]=Line[t-1];
			t--;
			}
		Line[t]=0;
		
		t=Count();
		cout<<"Case #"<<i+1<<": ";
		cout<<t/1000;
		t%=1000;
		cout<<t/100;
		t%=100;
		cout<<t/10;
		cout<<t%10<<endl;
		}
			
	return 0;
	}
