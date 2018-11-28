#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.txt","w",stdout);

	int N=0;
	int casenow=0;
	cin>>N;
	while (N-->0)
	{
		bool result=false;
		casenow++;
		int nn=0,k=0;
		cin>>nn>>k;
		k++;
		if( k&( (1<<nn) -1))
		{
		  result=false;
		}
		else
			result=true;

		cout<<"Case #"<<casenow<<": ";
		if(result)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
}