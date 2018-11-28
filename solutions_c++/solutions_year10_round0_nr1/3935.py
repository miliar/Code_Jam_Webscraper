#include <iostream>
#include <map>
#include <sstream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
	int T,N,K;
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>N>>K;
		cout<<"Case #"<<i+1<<": ";
		if(K%(1<<N)==(1<<N)-1)
			cout<<"ON";
		else
			cout<<"OFF";
		cout<<endl;
	}
	return 0;
}
