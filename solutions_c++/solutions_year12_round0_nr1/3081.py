#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

void main()
{
	char real[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
				// 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
	ifstream inp("A-small-attempt1.in");
	ofstream outp("output.txt");
	stringstream buffer;
	char c;
	buffer<<inp.rdbuf();
	int lineCount=1;
	int n=0;
	while(buffer.str().at(n)!=10)
			n++;
	for(int i=n+1;i<buffer.str().size();i++)
	{
		if(i==n+1)
			outp<<"Case #1: ";
		if(buffer.str().at(i)==32)
			outp<<' ';
		else if(buffer.str().at(i)==10)
		{
			lineCount++;
			outp<<endl;
			outp<<"Case #"<<lineCount<<": ";
		}
		else
		{
			inp>>c;
			int x=buffer.str().at(i)-97;
			outp<<real[x];
		}
		buffer.clear();
	}
}