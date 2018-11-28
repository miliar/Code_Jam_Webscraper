#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	//========read in input==========//
	char* input = "e:\\C-large.in";
	ifstream fin;
	fin.open(input,ios_base::binary);
	//========create output=========//
	ofstream fout;
	fout.open("output_l_2.txt", ios_base::binary);
	
	//==========begin here==========//
	int T;
	fin >> T;
	long long int R = 0, k = 0, total = 0;
	int N = 0;
	for(int i = 1; i <= T; i++)
	{
		//initiaiize for each case
		total = 0;

		fin >> R;
		fin >> k;
		fin >> N;
		int temp;
		int *a = new int[N];
		int *jump = new int[N]; //before gi
		long long int arraysum = 0;
		for(int j = 0; j < N; j++)
		{
			fin >> temp;
			a[j] = temp;
			arraysum += a[j];
			jump[j] = 0;
		}
		//-------------initial jump array------------------//
		if(N == 1)
		{ 
			jump[0] = 0;
		}
		else 
		{
			for(int j = 0; j< N; j++)
			{
/*			int sum = 0;
			int stop = j;
			while(1)
			{
				sum += a[stop%N];
				if(sum > k )
				{
					break;
				}
				stop ++;
			}
*/
				long long int sum = a[j];
				int stop = j+1;
				int tcount = 1;   //already add one to sum
				while(sum <= k && tcount <= N)
				{	
					tcount ++;
					sum += a[stop%N];
					stop ++;
				}
				stop --;
				jump[j] = stop%N;
			}
		}
		
		//----------------calculate how many rounds -----------------//
		int pr = 0, newpr = 0;
		int round = 0;
		for(int count = 1; count <= R; count ++)
		{
			newpr = jump[pr];
			if(newpr <=  pr)
				round ++;
			pr = newpr;
		}
		//-------------------calculate total-----------------------//
		total = round * arraysum;
		for(int l = 0; l< pr; l++)
		{
			total += a[l];
		}
		fout<< "Case #" << i <<": " << total << endl;
	}

	return 0;
}