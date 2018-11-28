#include <iostream>

using namespace std;

int main()
{
	std::cout.precision(12);
	int T, cs = 1;
	cin>>T;

	while(T--)
	{
		unsigned long long N, L, H;
		unsigned long long notes[1001] = {0};
		unsigned long long freq, finalFreq;
		int flag = 1;
		cin>>N>>L>>H;

		for(int i = 0; i < N; i ++)
		{
			cin>>notes[i];
		}

		for(freq = L; freq <= H; freq++)
		{
			for(int i = 0; i < N; i ++)
			{
				if(freq > notes[i])
				{
					if(freq % notes[i] != 0)
						break;
				}
				else
				{
					if(notes[i] % freq != 0)
						break;
				}
				
				if(i == N - 1)
				{
					finalFreq = freq;
					flag = 0;
					break;
				}
			}
			if(!flag)
				break;
		}
				
		cout<<"Case #"<<cs++<<": ";
		if(flag) cout<<"NO"<<endl;
		else cout<<finalFreq<<endl;
	}

	return 0;
}
