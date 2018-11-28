#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tstatic = t;
	while(t--)
	{
		int googlers, surprise, minimum;
		int jn1, jn2, jn3, js1, js2, js3;
		int n[100], cases = 0;
		cin>>googlers>>surprise>>minimum;
		for(int i=0;i<googlers;i++)
			cin>>n[i];
		for(int i=0;i<googlers;i++)
		{
			int average = n[i]/3;
			if(n[i] % 3 == 0)
			{
				if(average >= minimum)
				{
					cases++;
//					cout<<n[i]<<endl;
				}
				else if(surprise > 0 && average > 0 && average+1 >= minimum)
				{
					cases++;
					surprise--;
				}
			}
			else if(n[i] % 3 == 1)
			{
				if(average >= minimum || average+1 >= minimum)
					cases++;
				else if(surprise > 0 && average+1 >= minimum)
				{
					cases++;
					surprise--;
				}

			}
			else if(n[i] % 3 == 2)
			{
				if(average >= minimum || average+1 >= minimum)
					cases++;
				else if(surprise > 0 && average + 2 >= minimum)
				{
					cases++;
					surprise--;
				}
			}
//			cout<<cases<<" for "<<n[i]<<endl;
		}
		cout<<"Case #"<<(tstatic-t)<<": "<<cases<<endl;
	}
}
