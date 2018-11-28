// quaWelcome.cpp : Defines the entry point for the console application.
// 
#include <iostream>
#include <string>
#include <vector>
using namespace std ;

const char * wel = "welcome to code jam"; 

struct cell
{
	int v ;
	bool flag ;
public :
	cell() : flag(false) {}
};

cell ** matrix  ;

int get_match_num( const string& text,int text_index,const string& pattern,int pat_index )
{	 

	if ( (matrix[pat_index][text_index]).flag )
	{
		return (matrix[pat_index][text_index]).v ;
	} 
 
	if ( pat_index == text_index)
	{
		if ( 0 == strncmp(text.data(), pattern.data(),pat_index) ) 
			(matrix[pat_index][text_index]).v = 1 ; 
		else
			(matrix[pat_index][text_index]).v = 0 ;
		(matrix[pat_index][text_index]).flag = true ;
	}
	else if ( pat_index > text_index )
	{
		(matrix[pat_index][text_index]).v = 0 ;
		(matrix[pat_index][text_index]).flag = true ;
	}
	else
	{
		if ( text[text_index-1] != pattern[pat_index-1]  )
		{
			(matrix[pat_index][text_index]).v = get_match_num(text,text_index-1,pattern,pat_index) ;
			(matrix[pat_index][text_index]).flag = true ;
		}
		else
		{
			(matrix[pat_index][text_index]).v = (get_match_num(text,text_index-1,pattern,pat_index-1) 
				+ get_match_num(text,text_index-1,pattern,pat_index) ) %10000;
			(matrix[pat_index][text_index]).flag = true ;
		}
	}

	return (matrix[pat_index][text_index]).v ;
}


int  main( )
{ 
    int group ;
	cin>>group ;
	string signline; 
	getline(cin,signline) ;
	vector<int> results(group,0);

	for (size_t i=0;i<group;i++)
	{
		string text ;
		getline(cin,text) ;
		if (strlen(text.data()) == strlen(wel))
		{
			results[i] = (0==strcmp(wel,text.data()))? 1 :0; 
			continue ;
		}
		else if (strlen(text.data()) < strlen(wel))
		{
			results[i] = 0 ;
			continue ;
		}
		else
		{ 
			int tlen = strlen(text.c_str()); 
			int slen = strlen(wel);  

			matrix = new cell*[slen+1];
			for ( size_t ii=0;ii<slen+1;ii++ )
			{
				matrix[ii] = new cell[tlen+1] ;
			} 
		   
			for ( size_t ii=0;ii<tlen;ii++ ) 
			{
				(matrix[0][ii]).v = 1; (matrix[0][ii]).flag = true;
			}
			for (size_t ii=0;ii<slen;ii++ )
			{
				(matrix[ii][0]).v = 0; (matrix[ii][0]).flag = true;
			}
			 
			results[i] = get_match_num(text,tlen,wel,strlen(wel));	
			for ( size_t ii=0;ii<slen+1;ii++ ) delete[] matrix[ii];
			delete []matrix;
		}
	} 
	for (size_t i=0;i<group;i++) printf("Case #%d: %04d\n",i+1,results[i]%10000); 
	return 0;
}

