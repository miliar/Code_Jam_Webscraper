#include<iostream>
using namespace std;

int main()
{
int T ; 
cin>>T;
int N, K, tmp ;
for (int i=0 ; i< T; i++)
{
	cout << "Case #" << i +1 <<": " ;	
	cin>> N >> K ;
	if ( K % (1<<(N)) ==  ((1<< N) -1) )
			cout << "ON" << endl;
	else
			cout << "OFF" << endl;
}
return 0;
}
