#include <iostream>
#include <vector>
using namespace std;

unsigned long long int gcd(unsigned long long int a, unsigned long long int b)
{
	while(b)
	{
		unsigned long long int t = b;
		b = a % b;
		a = t;
	}
	
	return a;
}

int main(void)
{
	unsigned long long int T, N, L, H;
	
	cin >> T;
	for(unsigned int numCase = 1; numCase <= T; numCase++)
	{
		vector<unsigned long long int> frecs;
		
		cin >> N >> L >> H;
		for(unsigned int i = 0; i < N; i++)
		{
			unsigned long long int f;
			
			cin >> f;
			frecs.push_back(f);
		}
		
		unsigned int i = L;
		bool found = false;
		
		while(i <= H)
		{
			bool valid = true;
			
			for(unsigned int j = 0; j < N && valid; j++)
			{
				if(frecs[j] % i == 0 || i % frecs[j] == 0) continue;
				valid = false;
			}
			
			if(valid)
			{
				found = true;
				break;
			}
			else i++;
		}
		
		if(found) cout << "Case #" << numCase << ": " << i << endl;
		else cout << "Case #" << numCase << ": NO" << endl;
	}
}
