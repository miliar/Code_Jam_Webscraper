#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>
#include <string.h>

using namespace std;

int L,D,N ;

char words[5000][15];
int segments[15]['z'+1] ;

int checkWord(int i)
{
    for(int j=0;j<L;j++)
	if(segments[j][words[i][j]] == 0) return 0 ;

    return 1 ;
}

int main()
{
   scanf("%d %d %d", &L, &D, &N) ;
   

   for(int i=0;i<D;i++)
	scanf("%s", words[i]) ;

   

   string line;
   getline(cin, line) ;
   for(int i=1;i<=N;i++)
   {
	
	for(int a=0;a<L;a++)
	  for(int b='a';b<='z';b++)
	      segments[a][b] = 0 ;

	int k=0 ;
	getline(cin, line) ;
	int j=0 ;
	while(j<line.size() )
	    if(line[j] == '(') 
	    {
		j++;
		while(line[j] != ')')
		{
		  segments[k][line[j]] = 1 ;
		  j++ ;
		}
		k++ ; j++ ;
	    }
	    else 
	    {
		  segments[k][line[j]] = 1 ;
		  j++ ;
		  k++ ;
	    }


	int count = 0 ;
	for(int j=0;j<D;j++)
	    count += checkWord(j) ;
	    
	
	
	cout << "Case #" << i << ": " << count << endl ;

   }
   
   return 0 ;
}