#include <iostream>
#include <string>
using namespace std;
//Input
//3
//ejp mysljylc kd kxveddknmc re jsicpdrysi
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//de kr kd eoya kw aej tysr re ujdr lkgc jv


//Output
//Case #1: our language is impossible to understand
//Case #2: there are twenty six factorial possibilities
//Case #3: so it is okay if you want to just give up

int main()
{
	int T;
		char buffer [255];	cin>>T;cin.getline(buffer,255);
	for (int t = 0;t<T;t++)
	{

		cout<<"Case #"<<t+1<<": ";
		string inpa = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvyeqz";
		string inpb = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upaozq";
		cin.getline(buffer,255);
		string x (buffer);
		for (int i = 0;i<x.length();i++)
			for (int j = 0;j<inpa.length();j++)
				if (x[i]==inpa[j])
				{
					cout<<inpb[j];
					break;
				}
		cout<<endl;
	}
	return 0;
}
