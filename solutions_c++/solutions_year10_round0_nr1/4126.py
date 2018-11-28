#include<iostream>
using namespace std;

void Compute(int T)
	{
		long int in;	
		int count=1;
		int N,K;	
		
		while(T!=0)
		{
			
			cin>>N>>K;
			in=(1<<N) - 1;
			int k_temp = K-in;
			in = in+1;
			if(k_temp%(in) == 0)
			    cout<<"Case #"<<count<<": ON\n";
			else
			    cout<<"Case #"<<count<<": OFF\n";
			count++;
			T--;
					
		}	
	}



int main()
{
	int T;
	cin>>T;

	Compute(T);
return(0);
}
