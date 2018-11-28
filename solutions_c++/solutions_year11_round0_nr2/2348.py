#include<iostream> 
#include<cstdio>
#include<stack>
#include<string>
#include<fstream>
using namespace std;

//class node{
//	public:
	//	char c[27][2];
		//char d[27][2];
//};

//node v[27];
//stack<char> s;

int main()
{
	int n , t , T;
	int i , j , k , kk;
	char tmp , tt;
	int output = 0;
	char r[101];
	bool out = false;

	int C , D , N;
	string a[40] , b[30] , c;


	ifstream fin ("B-large.in");
	ofstream fout ("B-large.out");

	fin >> T;
	for( t = 1 ; t <= T ; ++t )
	{
		for( i = 0 ; i < 40 ; ++i )
			a[i].clear();
		for( i = 0 ; i < 30 ; ++i )
			b[i].clear();
		fin >> C;
		for( i = 0 ; i < C ; ++i )
		{
			fin >> a[i];
		}
		fin >> D;
		for( i = 0 ; i < D ; ++i )
		{
			fin >> b[i];
		}
		fin >> N;
		fin >> c;
		for( i = 1 ; i < N ; ++i )		
		{
			tmp = c[i-1];
			tt = c[i];
			for( j = 0 ; j < C ; ++j )
			{ 
				if(   tmp == a[j][0] && tt == a[j][1]   )
				{
					c[i] = a[j][2];
					c[i-1] = 0;
					break; 
				}
				else if(   tmp == a[j][1]  &&  tt == a[j][0]   )
				{
					c[i-1] = 0;
					c[i] = a[j][2];
					break; 
				}
			}
			if( c[i-1] == 0 )	//ªí¥Ü¦³combine
				; 
			else
			{
				for(    kk = 0  ;  kk < D  &&  c[i] != 0  ;  ++kk    )
				{
					if( tt == b[kk][0] )
					{
						for( j = 0 ; j <= i-1 ; ++j )
						{
							if(  c[j] == b[kk][1] )
							{
								for( k = 0 ; k <= i ; ++k )
									c[k] = 0;
								break;
							}
						}
					}
					else if( tt == b[kk][1] )
					{
						for( j = 0 ; j <= i-1 ; ++j )
						{
							if(  c[j] == b[kk][0] )
							{
								for( k = 0 ; k <= i ; ++k )
									c[k] = 0;
								break;
							}
						}
					}
				}
			} 
		}
		//for( n = 0 ; n < N ; ++n )
		//{
		//	fout << c[n];
		//}
		//fout << endl;
		out = false;
		//fout << "a: " << a << "  b:  " << b << endl; 
		fout << "Case #" << t << ": [";
		for( n = 0 ; n < N ; ++n )
		{
			if( c[n] != 0 )
			{
				if( out == false )
					out = true;
				else
					fout << ", ";
				fout << c[n];
			}
		}
		fout << "]" << endl;
		//printf( "Case #%d: %d\n" , t , output );
//		fout << "Case #" << t << ": " << output << endl; 
	}//end while(cin)
}
