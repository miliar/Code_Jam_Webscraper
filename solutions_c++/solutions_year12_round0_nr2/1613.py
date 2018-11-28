#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>

using namespace std;

int computeBest(int N, int S, int p, int* arr)
{
	// max results without surprises
	int* max_arr_n = new int[N];
	// max results with surprises
	int* max_arr_s = new int[N];
	for (int i=0; i<N; i++)
	{
		switch ( arr[i]%3 )
		{
			case 0:
			{
				max_arr_n[i] = arr[i]/3;
				max_arr_s[i] = ( arr[i]==0 ) ? 0 : arr[i]/3+1;
				break;
			}
			case 1:
			{
				max_arr_n[i] = arr[i]/3+1;
				max_arr_s[i] = arr[i]/3+1;
				break;
			}
			case 2:
			{
				max_arr_n[i] = arr[i]/3+1;
				max_arr_s[i] = arr[i]/3+2;
				break;
			}
		}
		if(max_arr_n[i] > 10 )
			max_arr_n[i] = 10;
		if(max_arr_s[i] > 10 )
			max_arr_s[i] = 10;

	}

	int number = 0;
	for( int i=0; i<N; i++ )
		if( max_arr_n[i] >= p )
			number++;
		else if ( S > 0 && max_arr_s[i] >= p )
			{
			number++;
			S--;
			}

	delete[] max_arr_n;
	delete[] max_arr_s;

	return number;
}

int main() {
	ifstream is("B-large.in");
	ofstream os("B-large.out");
	if(!is)
		return -1;
	int T = 0; is >> T;
	int* arr = NULL;
	int N,S,p;
	for(int cnt=1; cnt<=T; cnt++)
	{
		is >> N; is >> S; is >> p;
		arr = new int[N];
		for(int i=0; i < N; i++)
			is >> arr[i];
		int tmp = computeBest(N, S, p, arr);
		cout << "Case #" << cnt << ": " << tmp << endl;
		os << "Case #" << cnt << ": " <<  tmp << endl;
		delete[] arr;
	}
	is.close();
	os.close();
}

