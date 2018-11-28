#include<fstream>
#include<iostream>
using namespace std;

int ktore[1000], ilep, lista[1001][1001], ilef[1001], p[1001], r[1001];
bool prime[1001], zrobiony[1001];

void makeset(int x)

{
 p[x] = x;
}//make set

void unio (int x,int y)

{
 if(r[x]>r[y])
  p[y]=x;
 else
 {
  p[x]=y;
  if( r[x]=r[y])
	  r[y]++;
 }
}//union

int findset(int x)

{
 if(p[x]!=x)
	 p[x] = findset(p[x]);
 return p[x];
}//find set


int main()
{
	
	prime[1] = true;
	for(int i = 2; i < 100; i++)
		if(!prime[i])
		{
			int j = i * i;
			while(j <= 1000)
			{
				prime[j] = 1;
				j+=i;
			}
		}	
	for(int c = 2; c < 1000; c++)
		if(!prime[c])
			ktore[ilep++] = c;	
	ifstream in("B-small.in");
	ofstream out("B-small.out");
	int tests,a,b,p;
	in>>tests;
	for(int c = 0; c < tests; c++)
	{
		in >>a>>b>>p; int w;		
		for(int c = a; c <= b; c++)
		{
			makeset(c);
			w = 0; int pom = c;
			while(pom > 1)
			{				
				if(pom % ktore[w] == 0)
				{
					lista[c][ilef[c]++] = ktore[w];
					while(pom % ktore[w] == 0)
						pom /= ktore[w];
				}
				w++;
			}
		}
		/*for(int c = a; c <= b; c++)
		{
			cout<<c<<' ';
			cout<<ilef[c]<<" :";
			for(int c1 = 0; c1 <= ilef[c]; c1++)
				cout<<lista[c][c1]<<' ';cout<<'\n';
		}*/
		for(int i = a; i< b; i++)
		{
			for(int j = i + 1; j <= b; j++)
			{
				int wsk = 0, wsk1 = 0;
				while(wsk < ilef[i] && lista[i][wsk] < p) wsk++;
				while(wsk1 < ilef[j] && lista[j][wsk1] < p) wsk1++;
				while(wsk < ilef[i] && wsk1 < ilef[j])
				{
					if(lista[i][wsk] == lista[j][wsk1])
					{
						unio(findset(i),findset(j));
						break;
					}
					else if(lista[i][wsk] > lista[j][wsk1])
						wsk1++;
					else
						wsk++;
				}
			}
		}		
		int sets = 0;
		for(int c = a; c <=b; c++)
		{
			if(!zrobiony[findset(c)])
			{
				sets++;
				zrobiony[findset(c)] = 1;
			}			
		}
		for(int c = a; c <= b; c++)
		{
			ilef[c] = 0;
			zrobiony[c] = 0;
		}
		out <<"Case #"<<c+1<<":"<< " "<<sets<< '\n';
	}
	in.close();
	out.close();
	return 0;
}