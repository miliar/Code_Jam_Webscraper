#include <iostream>

using namespace std;

const int MAXLEN=1000+5;
const unsigned long LARGE=2147483647;

int T, N;
unsigned long item[MAXLEN];

unsigned long Compute()
{
	unsigned long bitXor=0;
	for (int i=0; i<N; i++)
		bitXor^=item[i];
	if (bitXor!=0)
		return LARGE+1;
	else
	{
		unsigned long min=LARGE;
		unsigned long sum=0;
		for (int i=0; i<N; i++)
		{
			sum+=item[i];
			if (item[i]<min)
				min=item[i];
		}
		return sum-min;
	}	
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin>>T;
	for (int i=0; i<T; i++)
	{
		cin>>N;
		for (int j=0; j<N; j++)
			cin>>item[j];

		unsigned long ret=Compute();
		cout<<"Case #"<<(i+1)<<": ";
		if (ret>LARGE)
			cout<<"NO"<<endl;
		else
			cout<<ret<<endl;
	}


	return 0;
}