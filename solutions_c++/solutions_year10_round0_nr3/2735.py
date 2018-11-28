#include<iostream>

using namespace std;

int main()
{
	int c;
	cin>>c;

	for(int i = 1; i <= c; i++)
	{
		int j, price = 0;

		int r, k, n;

		cin>>r>>k>>n;

		int arr[1000];

		for(j = 0; j < n; j++)
			cin>>arr[j];

//		for(j = 0; j < n; j++)
//			cout<<arr[j]<<", ";

		j = 0;

		for(int t = 0; t < r; t++)
		{
			int seats = 0;

			int check = 0;	

			while((seats + arr[j%n]) <= k && check < n)
			{
				seats += arr[j%n];

				j++;

				check++;
			}

			price += seats;
		}

		cout<<"Case #"<<i<<": "<<price<<"\n";
	}

	return 0;
}


