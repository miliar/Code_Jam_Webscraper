#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<stack>
#include<math.h>
using namespace std;
bool bin(long desired_state,long N,long K)
{
	
	if(desired_state%2==0)
		return false;
	int count=-1;
	long div=desired_state;
	while(div!=0)
	{
		if(div%2==0)
			return false;
		div=div/2;
		count++;
	}
	
	if(count<(N-1))return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long test_cases=0,N=0,K=0;
	cin>>test_cases;
	for(int i=0; i<test_cases;i++)
	{
		cin>>N;
		cin>>K;
		long num_of_states=pow((double)2,(double)N);
		long desired_state;
		desired_state=K%num_of_states;
		
		bool result=bin(desired_state,N,K);
		if(result)
			cout<<"Case #"<<(i+1)<<": ON\n";
		else
			cout<<"Case #"<<(i+1)<<": OFF\n";

	}
	
	return 0;
}
