#include <iostream>
using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for(int i = 0; i<T; i++)
	{
		int N = 0;
		cin >> N;
		int S = 0;
		cin >> S;
		int p = 0;
		cin >> p;
		int count = 0;
		for(int i = 0; i<N; i++)
		{
			int temp = 0;
			int temp2 = 0;
			cin >> temp;
			temp2 = temp/3;
			if(temp%3 != 0) temp2+=1;
			if(temp2 > p-1) count++;
			else if(temp >= p)
			{
				if(p - (temp-p)/2 <= 2 && S>0)
				{
				count++;
				S--;	
				}
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
		
	}
	
	//system("pause");
	return 0;	
}
