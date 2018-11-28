#include<iostream>
using namespace std;
int main()
{
	int T;
	int N;
	int *cost;
	cin >>T;
	int i;
	int j;
	bool ct[21];
	bool output=true;
	int sum=0;
	int min=0;
	int k=0;
	int remainder, number;

	while(k!=T)
	{
		for(j=0;j<21;j++){
			ct[j]=true;
		}
		output=true;
		k++;
		sum = 0;
		min=1000001;
		cin >> N;
		cost=new int[N];
		for(i=0;i<N;i++)
		{
			j=0;
			cin >>cost[i];
			if(min> cost[i])
				min=cost[i];
			sum = sum + cost[i];
			number=cost[i];
			while(true)
			{
				if(number <= 1) {
					if(number== 1)
						ct[j] = !ct[j];
					break;
				}
				remainder = number%2;
				number = number/2;
				if(remainder == 1)
					ct[j] = !ct[j];
				j++;
			}
		}
		for(j=0;j<21;j++){
			output = output && ct[j];
		}
		if(!output)
			cout << "Case #" << k << ": NO\n";
		else
			cout << "Case #" << k << ": " << sum - min << endl;
	}
}
