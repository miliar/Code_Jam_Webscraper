#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <cstdlib>


using namespace std;

bool increment(bool* arr, int n)
{
	for (int i=0;i<n;i++)
	{
		if (arr[i]==false) 
		{
			arr[i]=true;
			return false;
		}
		else 
		{
			arr[i] = false;
		}
	}

	return true;
}

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int N=0;
		cin>>N;
		
		int num[N]; 
		bool cond[N];

		for (int n=0;n<N;n++)
		{
			cin>>num[n];
			cond[n]=false;
		}
		
		bool done = false;
		bool found = false;
		int max = 0;

		while (!done)
		{
			int sum1 = 0;
			int sum2 = 0;
			int s1 = 0;
			int s2 = 0;
//			for (int i=0;i<N;i++) cerr<<cond[i]<<" ";
//			cerr<<endl;
			for (int i=0;i<N;i++)
			{
				if (cond[i]) sum1 = sum1^num[i]; else sum2 = sum2^num[i];
				if (cond[i]) s1 = s1+num[i]; else s2 = s2+num[i];
			} 

			if (sum1 == sum2 && sum1!=0) 
			{
//				cerr<<"setting found to true"<<endl;
				
				found = true;
				if (s1>s2) 
				{
					if (max < s1) max = s1;
				}
				else 
					if (max < s2) max = s2;
			}

			done = increment(cond, N);
		}
		
		if (!found)
			cout<<"Case #"<<t+1<<": NO"<<endl; 
		else 
			cout<<"Case #"<<t+1<<": "<<max<<endl; 
	
	}//test case for ends

}
