#include<iostream>
#include<string>
#include<fstream>
using namespace std;

const int MAXC = 5000+1;
const int MAXL = 15;

string dic[MAXC];
bool check[MAXL][26];
int l,d,n;

int main()
{
	ifstream fin("input");
	ofstream fout("output");
	fin >> l >> d >> n;
	for( int i = 0 ; i < d ; i++ )
		fin >> dic[i];
	for ( int i = 0 ; i < n ; i ++ )
	{
		string szword;
		fin >> szword;
		int flag = 0;
		memset( check,0,sizeof(check) );
		for( int j = 0,k = 0 ; j < l&&k<szword.length() ; k++)
		{
			if( flag == 0 )
			{
				if( szword[k] == '(' )
				{					
					flag = 1;
				} 
				else 
				{
					check[j][szword[k]-'a']=1;				
					j++;
				}
			}
			else if ( flag == 1 )
			{
				if( szword[k] == ')')		
				{
					flag = 0;
					j++;
				}
				else 
				{
					check[j][szword[k]-'a']=1;									
				}
			}
		}//for j
		int res = 0;
		for( int j = 0 ; j < d ; j++ )
		{
			bool isok = true;
			for(int k = 0 ; k < l ; k++)
			{
				if( !check[k][dic[j][k]-'a'] )
				{
					isok = false;
					break;
				}
			}
			if( isok )
				res++;			
		}
		//Case #1:
		fout << "Case #" << i+1 << ": ";
		fout << res << endl;
	}
}