#include"iostream"
#include"fstream"
#include"stdio.h"
#include"cmath"
using namespace std;
int main() 
{
	ifstream cin("A-large.in");
	ofstream cout("sqh.txt");
	int n,k,i,number;
	cin>>number;
	for(i=0;i<number;i++)
	{
		cin>>n>>k;
		if(k%(int)(pow((int)2,(int)n))==(int)(pow((int)2,(int)n)-1))
		{
			cout<<"Case #"<<i+1<<": ON\n";		
		}
		else cout<<"Case #"<<i+1<<": OFF\n";
	}
    return 0;
}




  
















