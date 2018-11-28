#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;


int main()
{
	ifstream cin("A-small-attempt1.in");
	ofstream cout("output.txt");
	long n;
	cin>>n;
	char alf1[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	vector <char> alf(alf1,alf1+26);
	
	string s;
	getline(cin,s);

	for(long q=0;q<n;q++)
	{
		getline(cin,s);
		for(long i=0;i<s.size();i++)
			if(s[i]!=' ')
				s[i]=alf[s[i]-'a'];
		
		cout<<"Case #"<<q+1<<": "<<s<<"\n";
	}
}
