#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;


int main()
{
	ifstream in("harmony.in");
	ofstream out("harmony.out");
	
	
	int T;
	in >> T;
	for(int X=0; X<T; ++X)
	{
		out << "Case #" << X+1 << ": ";
		cout << "Case #" << X+1 << ": ";
		unsigned long long int tN, tL, tH;
		in >> tN;
		in >> tL;
		in >> tH;
		
		vector <unsigned long long int> players;
		
		unsigned long long int total=1;
		
		for(unsigned long long int i=0; i<tN; ++i)
		{
			unsigned long long int temp;
			in >> temp;
			players.push_back(temp);
		}
		
		cout << "players: ";
		for(unsigned long long int n=0; n<players.size(); ++n)
		{
			cout << players[n] << " ";
		}
		cout << '\n';
		
		bool possible=false;
		
		for(unsigned long long int i=tL; i<=tH; ++i)
		{
			possible=true;
			for(unsigned long long int n=0; n<players.size(); ++n)
			{
				if(players[n]>=i)
				{
					if(!(players[n]%i==0))
					{
						possible=false;
						break;	
					}
				}
				else
				{
					if(!(i%players[n]==0))
					{
						possible=false;
						break;
					}
				}
			}
			
			if(possible)
			{
				total=i;
				break;
			}
		}
		
		if(possible)
		{
			cout << total << '\n';
			out << total << '\n';
		}
		else
		{
			cout << "NO" << '\n';
			out << "NO" << '\n';			
		}
	}
	
}








