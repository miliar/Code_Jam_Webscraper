#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int main()
{
	int cases;
	ifstream in("A-large2.in");
	ofstream out("out.txt");
	in>>cases;
	//cout<<cases<<endl;
	int count=1;
	while (cases--)	
	{
		out<<"Case #"<<count++<<": ";
		int n,k;
		in>>n>>k;
		int t=(int)pow(2.0,n*1.0);
		if ((k-t+1)%t==0)
		{
			out<<"ON";
		}
		else
		{
			out<<"OFF";
		}
		out<<endl;
	}
}