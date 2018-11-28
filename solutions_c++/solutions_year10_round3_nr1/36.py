#include<iostream>
#include<string>
#include<map>
using namespace std;

int A[2000], B[2000];

int main()
{
	int CAS;
	cin >> CAS;
	for(int cas=1; cas <= CAS; cas++)
	{
		int N;
		cin >> N;
		int cnt = 0;
		for(int i =0; i < N; i++)
		{
			cin >> A[i]>> B[i];
			for(int j = 0; j < i; j++)
			{
				if((A[i] - A[j]) * (B[i] - B[j])< 0)
					cnt++;
			}
		}
		cout << "Case #" << cas << ": " << cnt << endl;
	}
	return 0;

}
