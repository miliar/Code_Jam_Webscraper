#include <iostream>
using namespace std;

int main()
{
	int c,num,temp,min,nim,sum;
	cin >> c;
	for(int i=0;i<c;i++)
	{
		cin >> num;
		nim = 0;
		sum = 0;
		for(int j=0;j<num;j++)
		{
			cin >> temp;
			if(j==0) min = temp;
			else if(min > temp) min = temp;
			nim = nim^temp;
			sum += temp;
		}
		cout << "Case #" << i+1 << ": ";
		if(nim==0) cout << sum - min << endl;
		else cout << "NO" << endl;
	}
}
