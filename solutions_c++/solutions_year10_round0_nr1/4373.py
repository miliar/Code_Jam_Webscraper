#include <queue>
#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for(int i=0; i<T; i++)
	{		
		int N,s;
		
		cin >> N >> s;
		
		bool bulb[N];
		
		for(int j=0; j<N; j++)
			bulb[j] = false;
		
		for(int j=0; j<s; j++)
		{
			for(int k=0; k<N; k++)
			{
				bulb[k] = !bulb[k];
				if(bulb[k])
					break;
			}
		}
		
		bool ans=true;
		for(int j=0; j<N; j++)
			ans = ans && bulb[j];
			
		if(ans)
			cout<<"Case #" << i+1 << ": ON" << endl;
		else
			cout<<"Case #" << i+1 << ": OFF" << endl;
	}
}