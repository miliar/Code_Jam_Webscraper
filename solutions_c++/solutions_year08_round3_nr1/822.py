#include <iostream>
using namespace std;

int n;
int result[100];
int p,k,l;
int msg[1000];

void sort(int);

void main()
{
	cout<<"Enter number of inputs :";
	cin>>n;
	cout<<"Enter entire input set, all at once"<<endl;

	int temp, round;

	for(int i=0; i<n; i++)
	{
		result[i]=0;
		cin>>p>>k>>l;
		for(int j=0; j<l; j++)
		{
			cin>>msg[j];
		}

		sort(l);

		for(int j=0; j<l; j++)
		{
			temp = j%k;
			round = j/k+1;
			result[i] += round*msg[j];
		}
	}

	for(int i=0; i<n; i++)
	{
		cout<<endl<<"Case #"<<i+1<<": "<<result[i];
	}
}

void sort(int l)
{
	int temp;

	for(int i=0; i<l; i++)
	{
		for(int j=i+1; j<l; j++)
		{
			if(msg[i]<msg[j])
			{
				temp=msg[i];
				msg[i]=msg[j];
				msg[j]=temp;
			}
		}
	}
}
