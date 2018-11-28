#include <iostream>
using namespace std;

int main()
{
	int c;
	cin >> c;
	for(int i=1;i<=c;i++)
	{
		int temp;
		int num,sum=0;
		cin >> num;
		for(int j=1;j<=num;j++)
		{
			cin >> temp;
			if(temp!=j) sum++;
		}
		cout << "Case #" << i <<": ";
		cout << sum << ".000000" << endl;
	}	
}
