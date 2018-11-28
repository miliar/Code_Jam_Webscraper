#include<fstream>
#include <string>
using namespace std;

#ifndef loop(size)
#define loop(size) for ( int i=0 ; i < size ; i++ )
#endif

int main()
{
	ifstream in;  ofstream out;
	in.open("in.txt");
	int T ,  *N , *S , *P , **values , *result;
	in>>T;
	N = new int[T];
	S = new int[T];
	P = new int[T];
	values = new int * [T];
	result = new int[T];
	for ( int i=0 ; i < T ; i++ )
	{
		in>>N[i]>>S[i]>>P[i];
		int size  =N[i];
		values[i] = new int[size];
		for ( int j=0 ; j < size ; j++ )
			in >> values[i][j];
	}
	in.close();
	for ( int i=0 ; i < T ; i++ )
	{
		result[i]=0;
		for ( int j=0 ; j < N[i] ; j++ )
		{
			switch ( values[i][j] % 3)
			{
			case 0:
				{
					if ( values[i][j] / 3 >= P[i] )
						result[i]++;
					else if ( (values[i][j] / 3 + 1 >= P[i]) && values[i][j]!= 0 )
					{ 
						if ( S[i] > 0 )
						{ S[i]--;result[i]++;}
					}
					break;
				}
			case 1:
				{
					if ( values[i][j] / 3 + 1 >= P[i] )
						result[i]++;
					break;
				}
			case 2:
				{
					if(values[i][j] / 3 + 1 >= P[i] )
						result[i]++;
					else if ( S[i] > 0 )
					{
						if ( (values[i][j] / 3 + 2 >= P[i])  )
							{ result[i]++ ; S[i]--;}
					}
				}
			}
		}
	}

	out.open("out.txt");

	for ( int i=0 ; i < T; i++ )
	{
		out<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}
	out.close();
	return 0;
}

