#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	
	ifstream in_data;
	ofstream out_data;
	int num_of_case, N, S, p, total, hit, check;


	in_data.open("input.txt");
	out_data.open("output.txt");

	in_data >> num_of_case;

	for(int k=0; k<num_of_case; k++)
	{
		hit = 0;
		check = 0;
		in_data >> N >> S >> p;

		out_data << "Case #" << k+1 << ": ";

		for(int m = 0; m<N; m++)
		{
			in_data >> total;
			if(total>=2 && total <= 28)
			{
				check++;
			}
			if((p==0 && total==0) || 3*p-2<= total )
			{
				hit ++;
			}
			else if(p>1 && 3*p-4<= total && S>0)
			{
				hit++;
				S--; 
			}
			
		}

		if(check < S)
		{
			out_data << "0" << endl;
		}
		else
		{
			out_data << hit << endl;
		}

	}

	
	return 0;
}