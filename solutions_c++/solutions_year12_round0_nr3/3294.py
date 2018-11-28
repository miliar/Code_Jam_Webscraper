#include <fstream>

using namespace std;

int getLength( int long B )
{
	int length = 1;
	while( B >= 10 )
	{
		B /= 10;
		length++;
	}
	return length;
}

int long getMoved( int long a , int long& A, int long& B, int length )
{//move to right
	//length
	int rightest = 0, count = 0, var = a;

	if( length == 1 )
	{
		return 0;
	}

	for( int i = 1; i < length; i ++ )
	{//turn right
		rightest = a - a/10*10;
		for( int j = 1; j < length; j++ )
		{
			rightest *= 10;
		}
		var = a/10 + rightest;
		
		if( var >= A && var <= B && var != a )
		{
			count ++;
		}
		a = var;
	}
	return count;
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("C-small-attempt0.in");
	out.open("C-small-attempt0.out");

	int NUM_OF_CASES; 
	long int A, B, pair_count;
	int length;

	//read in
	in >> NUM_OF_CASES;
	for( int i = 0; i < NUM_OF_CASES; i++ )
	{
		in >> A >> B;
		length = getLength(B);

		out << "Case #" << i + 1 << ": ";

		pair_count = 0;

		//get twice as pairs
		for( long int j = A; j <= B; j++ )
		{
			pair_count += getMoved( j, A, B, length );
		}

		out << pair_count/2 << endl;
	}

	in.close();
	out.close();

	return 0;
}