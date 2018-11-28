#include <iostream>
#include <cmath>
#define SQR(x) ((x)*(x))
using namespace std;



struct polong
{
    long int x;
};

 int main()
{
    long int NoOfInputs;
    cin >> NoOfInputs;
    for( long int i = 0; i < NoOfInputs; i++ )
    {
	long int  max_let, keys, letters, temp;
	cin >>max_let >> keys >> letters;
	int  * freq;
	freq = new int[letters];
	long int count = 0;
	for(int j=0; j < letters; j++)
	{
		cin >> freq[j];
	}
	//cout <<max_let << " " << keys << " " << letters << endl;
	//sort freq array here

	for( int j = 0; j < letters -1 ; j++ )
        {
            int minimum = freq[j] ;
            int position = j;
            for( int k = j + 1; k < letters; k++ )
            {
                int current = freq[k] ;
                if( minimum > current )
                {
                    minimum = current;
                    position = k;
                }
            }
            if( position != j )
            {
                temp = freq[j];
                freq[j] = freq[position];
                freq[position] = temp;
            }
        }


	int rank = 1;
	int temp2 = 0;
	for(int j=letters-1; j>=0; j--)
	{
		temp2++;
		count += freq[j]*rank;
		//cout << freq[j]*rank << " " << temp2 << " rank" << rank<< " " << endl;
		if(temp2==keys)
		{
			temp2=0;
			rank++;
		}
	}
	cout << "Case #" << i+1 << ": " << count << endl;
	
    }

    return 0;
}
