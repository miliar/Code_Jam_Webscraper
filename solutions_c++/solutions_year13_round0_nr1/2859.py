#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
int bound= 4;

// test if win for youpick in lines
bool cl ( char * a  , char youpick )
{
	for (int i = 0; i < bound; i++)
	{
		int count= 0;
		int p ;
		for (int j = 0; j < bound; j++)
		{
			p = 4*i +j ;
			if ( a[p] == 'T' || youpick == a[p] )
				count++;
		}
		if ( count == 4 )
			return true;

	}
	return false;
}
// test if win for youpick in columns
bool cc ( char *a , char youpick)
{
	for (int i = 0; i < bound; i++)
	{
		int p;
		int count =  0;
		for (int j = 0; j < bound; j++)
		{
			p = j*4 + i;
			if ( a[p] == 'T' || youpick == a[p] )
				count++;
		}
		if ( count == 4 )
			return true;

	}
	return false;
}

// test if win for youpick in dia
bool cd ( char *a , char youpick)
{
	int p;
	int count = 0;
	for (int i = 0; i < bound; i++)
	{
		p = i*4 + i;
		if ( a[p] == 'T' || youpick == a[p]  )
			count++;
	}
	if ( count == 4 )
		return true;
	else
		count = 0;
	for (int i = 0; i < bound; i++)
	{
		p = i*4 + 3 - i;
		if ( a[p] == 'T' || youpick == a[p]  )
			count++;
	}
	if (count == 4)
		return true;
	else
		return false;
}
bool is_finish( char * a  )
{
	for (int i = 0; i < bound; i++)
	{
		for (int j = 0; j < bound; j++)
		{
			if( a[i*4+j] == '.')
				return false;
		}
	}
	return true;
}


int main(){
	ifstream in ("A-large.in");
	ofstream out ("test.out" );

	int num;
	in >> num;
	char temp;
	char * all;
	all = new char[bound*bound];
	for (int ii = 0; ii < num; ii++)
	{
		for (int i = 0; i < bound; i++)
		{
			for (int j = 0; j < bound; j++)
			{
				in >> temp;
				all[i*4+j] = temp;
			}
		}

		//test lines
		// for X
		char forwhom;
		int result = -2;
		for (int i = 0; i < 2; i++)
		{
			if ( i == 0) 
				forwhom = 'X';
			else
				forwhom = 'O';

			if ( cl ( all, forwhom) )
			{

				result = i; // have reuslt
			}
			else if ( cc ( all , forwhom) )
			{
				result = i;
			}
			else if ( cd ( all , forwhom ) )
			{
				result = i;
			}
			
		}
		if (result == 0)
				out << "Case #"<<ii+1 << ": X won"<<endl;
		if (result == 1)
				out << "Case #"<<ii+1 << ": O won"<<endl;
		if (result == -2 )
		{
			// need to decide tie or unfinined 
			if ( is_finish ( all ))
				out << "Case #"<<ii+1 << ": Draw"<<endl;
			else
				out << "Case #"<<ii+1 << ": Game has not completed"<<endl;
		}
	}
	return 0;

}