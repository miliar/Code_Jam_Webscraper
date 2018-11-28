#include<iostream.h>
#include<math.h>

int validate( int minFlip, int K );

int main(int argc, char** argv)
{
	int numCase, N, result;
	long K;
	long minFlip;
	
	//cout << "Num TestCase : "; 
	cin >> numCase;

	// Find min Flip to set the light on and that is always 2^N - 1

	for( int caseIndex = 0; caseIndex < numCase; caseIndex++ )
	{
		//cout << "Input N ";
		cin >> N;
		//cout << "Input K ";
		cin >> K;

		minFlip = (1 << N) - 1;

		result = validate( minFlip, K );

		cout << "Case #" << (caseIndex + 1) << ": ";

		if( result == 1)
		{
			cout << "ON" << endl;
		}
		else
		{
			cout << "OFF" << endl;
		}

	}

	return 0;
}


int validate( int minFlip, int K )
{
	int result = 1;
	

	if( (K % (minFlip + 1)) == minFlip )
	{
		result = 1;
	}
	else
	{
		result = 0;
	}

	return result;
}
