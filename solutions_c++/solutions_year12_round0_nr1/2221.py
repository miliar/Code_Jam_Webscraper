#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
	int t, i;
	char tem[2];
	cin>>t;
	cin.getline(tem, '\n');
	char std[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	for (i = 0; i < t; i++)
	{
		char temp[101];
		cin.getline(temp,200, '\n');
		for (int j = 0; temp[j]!='\0' ; j++)
		{
			if(temp[j]>=97 && temp[j]<=122)
				temp[j] = std[temp[j]-97];
		}
		cout<<"Case #"<<i+1<<": "<<temp<<endl;
	}
}
