#include<iostream>
#include<fstream>
#include<string>

using namespace std;

void fileIO()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
}
main()
{
	int t,i,j,k;
	//cout  << "test";
	char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };
	
	string input;
	fileIO();
//	cout << "test";
	cin >> t;
		getline(cin,input);
	for(i=0;i<t;i++)
	{
		getline(cin,input);
		cout << "Case #" << i+1 << ": ";
		for(j=0;j<input.length();j++)
		{
			if(input.at(j)-'a'>=0)
				cout << map[input.at(j)-'a'];
			else
				cout << " "; 
		}
		cout << "\n";
	}

}
