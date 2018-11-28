#include <iostream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	unsigned int R, N, k, total, i, n, j, tmp, turn;
	unsigned long long euro = 1000000000000000, subtotal;
	unsigned int groups[1000];
	
	fin.open("C-small.in");
	fout.open("my.out");
	
	fin >> total;
	
	cout << "total: " << total << " "<< euro <<endl;
	
	for(n = 0; n < total; n ++)
	{
		subtotal = 0;
		fin >> R >> k >> N;
		//cout << "R = " << R << ", K = " << k << ", N = " << N << "groups: " ;
		
		for(i = 0; i < N; i ++)
		{
			fin >> groups[i];
		//	cout << groups[i] << " ";
			subtotal += groups[i];
			
		}
		//cout << endl;
		
		//start = 0;
		//end = 0;
		//turn = 0;
		euro = 0;
		
		
		if(subtotal <= k)
		{
			euro = (unsigned long long) R * subtotal;
		}
		else {
			j = 0;
			
			for(i = 0; i < R; i ++)
			{
				subtotal = 0;
		//	j = start;
				while(1)
				{
					tmp = subtotal + groups[j];
					if(tmp <= k)
					{
						subtotal = tmp;
						j = (j + 1) % N;
					}
					else {
					break;
					}
				}
			   // cout << " " << subtotal ;	
				euro += subtotal;
			
			}
			
		}
		cout << " Case #" << n + 1 << ": " << euro << endl;
		fout << "Case #" << n + 1 << ": " << euro << endl;
	}
}
