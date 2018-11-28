#include <fstream>
#include <iostream>
using namespace std;


int main()
{
	char dest[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	/*ifstream fin ("A-small-attempt1.in");
	ofstream fout ("Googlerese.out");*/

	int tests;
	cin>>tests;

	char t[2];
	cin.getline(t,10,'\n');//Go to the next line

	for (int i=0;i<tests;i++)
	{
		char s[110];
		cin.getline(s,105,'\n');
		streamsize n = cin.gcount();
		n--;
		cout<<"Case #"<<i+1<<": ";
		for (int j=0;j<n;j++)
		{
			if (s[j]==' ') cout<<s[j];
			else cout<<dest[s[j]-'a'];
		}
		cout<<endl;
	}
	return 0;
}