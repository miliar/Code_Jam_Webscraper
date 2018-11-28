# include <iostream>
# include <fstream>

using namespace std;

void sortArr ( int *arr, int size )
{
	int temp;

	for ( int i=0; i<size; i++ )
	{
		for ( int j=i+1; j<size; j++ )
		{
			if ( arr[i] > arr[j] )
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	
	}

}

int calculate ( int *arr, int size)
{
	int patric=0, ptemp=0, sean=0, stemp=0; 

	for ( int i=0; i<size; i++ )
	{
		patric += arr[i];

		ptemp ^= arr[i];

		for ( int j= size-1; j>i; j--)
		{
			sean += arr[j];

			stemp ^= arr[j];
		}

		if ( ptemp == stemp )
			return sean;

		stemp = 0;
		sean  = 0;
	}

return 0;
}

void readFromFile ()
{

	int T, counter =1, size, i;
	int temp;
	int arr[1005];

	ofstream ofptr;
	ifstream ifptr;
	
	ifptr.open ( "C-small-attempt0 (1).in");
	ofptr.open ( "out.in" );

	ifptr>>T;

	while ( T )
	{

		ifptr>>size;

		for ( i=0; i<size; i++ )
		{
			ifptr>>arr[i];
		}
		
		sortArr ( arr, size );
		temp = calculate (arr, size);

		if ( temp )
			ofptr << "Case #" << counter <<": "<< temp <<endl;

		else
			ofptr << "Case #" << counter <<": NO"<<endl;
		counter++;
		T--;
	}
}

int main ()
{
	readFromFile();

	return 0;
}
