#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

ifstream fin("C:\\C-large.in");
ofstream fout("C:\\A-small-attempt6.out");
 
#define cin fin
#define cout fout

int main()
{
	 int Case;
	 cin>>Case;
	 for( int i = 1; i<=Case; i++)
	 {
		 int n,in,stand,min,sum = 0;
		 cin>>n>>stand;
		 min = stand;
		 sum = min;
		 for( int j = 2; j<=n; j++)
		 {
			 cin>>in;
			 if( in < min) min = in;
			 sum += in;
			 stand = stand^in;
		 }
		 cout<<"Case #"<<i<<": ";
		 if( stand ) cout<<"NO"<<endl;
		 else
			 cout<<sum-min<<endl;
	 }		 
     return 0;
}