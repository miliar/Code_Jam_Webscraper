#include <iostream>
#include <stdio.h>

using namespace std;

int arena[100][100] ;
char labels[100][100] ;
int h; int w;
char letter ;
int it ;

char findLabel(int i, int j) 
{
	int min = arena[i][j] ; 
	int k=0,l=0 ;
	if(i!=0 && arena[i-1][j] < min) { min = arena[i-1][j] ; k=-1; l=0; }
	if(j!=0 && arena[i][j-1] < min) { min = arena[i][j-1] ; k=0; l=-1; }
	if(j!=w-1 && arena[i][j+1] < min) { min = arena[i][j+1] ; k=0; l=1; }  
	if(i!=h-1 && arena[i+1][j] < min) { min = arena[i+1][j] ; k=1; l=0;}
 



	if(min == arena[i][j])
	{
	    labels[i][j] = letter ;
	    return letter++ ;
	}
	

	if(labels[i+k][j+l] != 0)
	{
	    labels[i][j] = labels[i+k][j+l] ;
	    return labels[i+k][j+l] ;
	}

	char c = findLabel(i+k, j+l) ;
	labels[i][j] = c ;
	return c ;

	      
}

void doLabels()
{
    for(int i=0;i<h;i++)
	for(int j=0;j<w;j++)
	    labels[i][j]= 0 ;

    letter = 'a' ;

    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++)
	  if(labels[i][j] == 0)
	      labels[i][j] = findLabel(i,j) ;     

    cout << "Case #" << it << ":\n" ;
    for(int i=0;i<h;i++)
    {
      cout << labels[i][0] ;
      for(int j=1;j<w;j++)
	  cout << " " << labels[i][j] ;
      cout << endl ;
    }
    
}

int main()
{
    int n;
    scanf("%d", &n) ;

    for(it=1;it<=n;it++)
    {
	scanf("%d %d", &h, &w) ;
	
	for(int j=0;j<h;j++)
	  for(int k=0;k<w;k++)	     
	      scanf("%d", &arena[j][k]);	      	 
	
	doLabels() ;
    }


    return 0;
} 
