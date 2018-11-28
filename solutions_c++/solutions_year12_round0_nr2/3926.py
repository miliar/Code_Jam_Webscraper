#include<iostream>
using namespace std;
int main()
{
	int T, S, N, p, arr[105], lt, total;
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		cin>>N>>S>>p;
		for(int j = 0; j < N; j++)
			cin>>arr[j];
		lt = (p * 3) - 2; 
		total = 0;
		for(int j = 0; j < N; j++) 
		{
			if (arr[j] >= lt) 
				total++;
			else if (S > 0 && lt > 2)
				if((arr[j]==lt-1)||(arr[j]==lt-2)) 
					{
						S--;
						total++;
					}
		}
		cout<<"Case #"<<i+1<<": "<<total<<endl;
	}
}
