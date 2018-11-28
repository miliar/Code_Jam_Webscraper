#include <iostream>
#include <vector>
#include <string>
using namespace std; 

int main()
{
	int N ; 
	cin>>N ; 

	for(int i = 1 ;i <= N ; i++)
	{
		int n , k ; 
		cin>>n >> k ; 

		k = k & ((1<<n)-1) ; 
		string ret = (k == ((1<<n)-1))?"ON" :"OFF" ; 		
		cout<<"Case #"<<i<<": "<<ret<<endl ;
	}
	return 0; 
}