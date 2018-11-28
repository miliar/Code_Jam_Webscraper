#include<iostream>
#include<fstream>
using namespace std;

const char trans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	ifstream infile("input.txt");
	ofstream outfile("output.txt");
	int n;
	char ch;
	infile>>n;
	infile.get(ch);
	for (int i=0;i<n;i++)
	{
		infile.get(ch);
		outfile<<"Case #"<<i+1<<": ";
		while (((ch>='a')&&(ch<='z'))||(ch==' '))
		{
			if (ch==' ') outfile<<' ';
			else outfile<<trans[ch-'a'];
			infile.get(ch);
		}
		outfile<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
