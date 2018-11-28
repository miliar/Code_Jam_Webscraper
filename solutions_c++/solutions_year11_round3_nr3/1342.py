#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;

long long freq [1005];

int main () 
{
	ifstream in("in.in");
	ofstream out("out.out");
	
	int T;
	in >> T;
	
	for(int i = 0; i < T; ++i)
	{		
		long long N, L, H; //check int is big enough for 10^16
		in >> N >> L >> H;
		
		for(int j = 0; j < N; ++j)
			in >> freq[j];
		
		bool divides = false;
		for(int j = L; j <= H; ++j) //each frequency
		{
			bool good_so_far = true;
			for(int k = 0; k < N; ++k) // each team member
			{
				double div1;
				int div2;
				
				if(j > freq[k])
				{
					div1 = 1.0*j/freq[k];
					div2 = j/freq[k];
				}
				else
				{
					div1 = 1.0*freq[k]/j;
					div2 = freq[k]/j;
				}
				
				if(div1 != div2)
				{
					good_so_far = false;
					break;
				}
			}
			if(good_so_far)
			{
				out << "Case #" << i+1 << ": " << j << "\n";
				divides = true;
				break;
			}
		}
		
		if(!divides)
			out << "Case #" << i+1 << ": NO" << "\n";
	}
}