// quaAlien.cpp : Defines the entry point for the console application.
// 
#include <iostream>
#include <string>
#include <vector>
using namespace std ;


int  main( )
{
	int L,D,N;
	cin>>L>>D>>N;
	string signline;
	getline(cin,signline);

	vector<string> phrases(D);
	for (size_t i=0;i<D;i++)  getline(cin,phrases[i]) ; 

	vector<int>    results(N,0);
	for (size_t i=0;i<N;i++)
	{
		int g_count =0;
		string pattern ;
		getline(cin,pattern) ; 
		const char * p = pattern.c_str();
		int len = strlen( p) ;  
		// pre charge :
		vector<int>  descriptors(L,0);
		size_t iL = 0; 
		for ( size_t ii=0;ii<len;ii++ ) 
		{  
			if( '(' == *(p+ii) )
			{ 
				ii ++ ; 
				for ( ;ii<len;ii++ )
				{
					if ( ')' == *(p+ii) )
					  break ;
					else
						descriptors[iL] |= (1<<(*(p+ii)-'a')) ; 
				}
			}
			else  
			    descriptors[iL] |= (1<<(*(p+ii)-'a')) ;  

			iL ++ ;
		}

		for ( size_t k=0;k<D;k++ )
		{
			size_t kk=0 ;
			for ( ;kk<L;kk++ )
			{
				if ( descriptors[kk] &  (1<<(phrases[k][kk]-'a')) ) 
					continue ;
				else 
					break ;
			} 
			if ( kk == L )  
				g_count ++ ; 
		}

		results[i] = g_count ;
	}

	for ( size_t i=0;i<N;i++ )  printf("Case #%d: %d\n",i+1,results[i]); 
 
	return 0;
}

