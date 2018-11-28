#include<iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T,A,B;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cin >> A >> B;
		double P[A];
		double N[A+2];
		for(int j = 0; j<A; j++)
		{
			cin >> P[j];
			if(j != 0)P[j] = P[j] * P[j-1];
			//cout << P[j] << endl;
		}
		for(int j = 0; j<A+2; j++)
		{
			if(j == A+1)N[j] = B+2;
			else N[j] = (A-j)+(B-j)-1+(1-P[j])*(1+B);
			//cout << N[j] << endl;
		}
		double temp = N[0];
		//cout << "temp: " << endl;
		for(int j = 0; j<A+2; j++)
		{
			if (N[j] <= temp)
			temp = N[j];
			//cout << "temp change: " temp << endl;
		}
		cout << "Case #" << i+1 << ": " << fixed << setprecision(6) << temp << endl;
	}
	//cout << "hw" << endl;
	//system("pause");
	return 0;
}
