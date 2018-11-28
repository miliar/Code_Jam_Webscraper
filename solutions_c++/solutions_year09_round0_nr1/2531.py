#include<iostream>
#include<string>

#define MAX 1000
#define LMAX 17
#define DMAX 5002
#define NMAX 5002
#define AMAX 27+'a'

#define T(a,b) Table[a][b]
#define W(a) Word[a]
#define W2(a,b) Word[a][b]
#define P(a) Pattern[a]

#define FOR(a,b) for(int a=0; a<b; a++)

using namespace std;

int L,D,N;
bool Table[LMAX][AMAX];
char Word[DMAX][LMAX];
char Pattern[MAX]	;

void createTable()
	{
	char c;
	int t=strlen(Pattern);
	
	FOR(i,LMAX) FOR(j,AMAX) T(i,j)=false;
	
	int i=0;
	FOR(j,L)
		{
		if(P(i)=='(')
			{
			i++;
			while(P(i)!=')')
				{ 
				T(j,P(i))=true; 
				i++; 
				}
			i++;
			}
			
		else
			{
			T(j,P(i))=true;
			i++;
			}
		}
	}

int countDict()
	{
	int count=0;
	FOR(i,D)
		{
		bool label=false;
		FOR(j,L)
			if(!T(j,W2(i,j)))
				{
				label=true;
				break;
				}
				
		if(label==false)
			count++;	
		}
	return count;
	}

void yaz()
	{
	for(int i=0; i<4; i++,cout<<endl)
		for(int j='a'; j<='z'; j++)
			if(T(i,j))cout<<"1";
			else cout<<"0";
	}

int main()
	{
	cin>>L>>D>>N;
	
	FOR(i,D) cin>>W(i);
	
	FOR(i,N)
		{
		cin>>Pattern;
//		cout<<Pattern<<endl;
		createTable();
//		yaz();
		cout<<"Case #"<<i+1<<": "<<countDict()<<endl;
		}	
	return 0;
	}
