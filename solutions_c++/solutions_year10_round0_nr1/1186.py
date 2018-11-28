#include<iostream>

using namespace std;

int main()
{
	int num;
	cin >> num;

	for(int i=1;i<=num;i++)
	{
		bool answer;
		int N, K;
		cin >> N >> K;
		//N--;
		int comp = (1 << N) - 1;
		K &= comp;
		answer = (K == comp);
//		answer = !!(((1 << N) - 1) & K);

		cout << "Case #" << i << ": ";
		if(answer)
		{
			cout << "ON" << endl;
		}
		else
		{
			cout << "OFF" << endl;
		}
	}
	return 0;
}
