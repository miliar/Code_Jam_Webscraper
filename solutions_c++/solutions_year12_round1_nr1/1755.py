#include <fstream> 
#include <iomanip> 

using namespace std;

float method1( float* p , int A, int B );
float method2( float* p , int A, int B );
float method3( float* p , int A, int B );
float getCorrProba( float* p, int n );

int main()
{
	//open files
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");

	//data will be used
	float* p;
	float smallest;

	//read from file
	int T;
	long int A, B;
	in >> T;
	for( int i = 0; i < T; i ++ )
	{
		in >> A >> B;
		p = new float[ A ];
		for( int j = 0; j < A; j ++ )//read the possibilities
		{
			in >> p[ j ];
		}

		smallest = method2( p, A, B );
		if( smallest > method3 ( p, A, B ) )
		{
			smallest = method3( p, A, B );
		}
		out.setf(ios::fixed);
		out << "Case #" << i + 1 << ": " << setprecision(6) << smallest << endl;
	}

	//close files
	in.close();
	out.close();

	return 0;
}

float method1( float* p , int A, int B )
{
	int remainType = B - A + 1;
	float remProba = getCorrProba( p, A );
	
	return remainType * remProba + ( 1 - remProba ) * ( remainType + B + 1);
}
float method2( float* p , int A, int B )
{
	float left_corr_proba = 1;
	int type_times = B + A + 1;

	float smallest = left_corr_proba * type_times;
	float var;

	for( int i = 0; i < A; i++ )
	{
		left_corr_proba *= p [ i ];
		type_times -= 2;

		var = left_corr_proba * type_times + (1 - left_corr_proba) * ( type_times + B + 1 );

		if( smallest > var )
		{
			smallest = var;
		}
	}

	return smallest;
}
float method3( float* p , int A, int B )
{
	return B + 2;
}


float getCorrProba( float* p, int n )
{
	float result = 1;
	for ( int i = 0; i < n; i ++ )
	{
		result *= p[ i ] ;
	}
	return result;
}