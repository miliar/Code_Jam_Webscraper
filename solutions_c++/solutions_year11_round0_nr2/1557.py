#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;
void MagickaList(int line ,ifstream &input ,ofstream &output);

const int S_MAXLEN = 127;
const int C_MAXLEN = 40 ;
const int D_MAXLEN = 30 ;
int main()
{
	long start = GetTickCount();
	ifstream input("B-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("B-large.out",ios::out);
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	for (i=0;i<lines;i++)
	{
		MagickaList(i,input,output);
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}
void MagickaList(int line ,ifstream &input ,ofstream &output)
{
	int combineSize ,opposeSize ,i ;
	input>>combineSize ;
	char   combine[C_MAXLEN][3] ;
	for(i=0;i<combineSize ;i++)
	{
			input>> combine[i] ;
			//cout<<combine[i] <<" ";
	}	
	input >>opposeSize ;
	char oppose[D_MAXLEN][2] ;
	for(i=0;i<opposeSize ;i++)
	{
			input>> oppose[i] ;
			//cout<<oppose[i] <<" ";
	}
	int series_len ;
	char invoke_series[S_MAXLEN] ;
	input>> series_len;
	input>>invoke_series ;
	//cout<<invoke_series ;

	int final_len = 0 , j ,k ;
	char final_list[S_MAXLEN] ;
	for(i=0; i<series_len;i++)
	{
		if(final_len ==0)
		{
			final_list[0] = invoke_series[i] ;
			final_len ++;
			continue ;
		}
		char last =final_list[final_len-1];
		char new_ =invoke_series[i] ;
		bool combined = false ;
		//see if can combine 
		for(j=0 ; j<combineSize ;j++)
		{
			//can combine
			if( (    (combine[j][0] ==last)&&(combine[j][1] ==new_)     )   || 
				(    (combine[j][1] ==last)&&(combine[j][0] ==new_)     )   )
			{
				combined= true; 
				final_list[final_len-1]= combine[j][2];
				break ;
			}
		} //end of for 
		if(combined)
			continue  ;
		//see if the list would be cleared
		bool cleared = false ;
		for(j =0 ;j<final_len ;j++)
		{
			if(cleared)
				break ;
			for(k=0;k<opposeSize ;k++)
				if(  (   (new_== oppose[k][0])&& (final_list[j]==oppose[k][1])  )     || 
					 (   (new_== oppose[k][1])&& (final_list[j]==oppose[k][0])   )      )
				{
					final_len = 0;
					cleared = true ;
					break ;
				}
		}
		if(cleared)
			continue ;
		final_list[final_len] =invoke_series[i] ;
		final_len++;

	} // end of for(i=0; i<series_len;i++)
	//cout<<"Case #"<<line+1<<": [";
	output<<"Case #"<<line+1<<": [";
	for(i=0 ; i<final_len ;i++)
	{ 
		if(0!=i)
			//cout<<", "<<final_list[i];
			output<<", "<<final_list[i];
		else
			output<<final_list[i];
			//cout<<final_list[i];
	}		
	//cout<<"]\n";
	output<<"]\n";
}