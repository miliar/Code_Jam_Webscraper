#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	string translated="q z ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string original="z q our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char mapping[128];

	for(int i=0;i<translated.length();i++)//Map characters
		mapping[translated[i]]=original[i];
	ifstream cin("A-small-attempt1.in");
	ofstream cout("A-small-attempt1.out");
	int T;
	cin>>T;
	string temp;
	getline(cin,temp);
	for(int i=1;i<=T;i++)
	{
		string translated;
		getline(cin,translated);
		cout<<"Case #"<<i<<": ";
		for(int i=0;i<translated.length();i++)
			cout<<mapping[translated[i]];
		if(i!=T)
			cout<<endl;
	}
	return 0;
}