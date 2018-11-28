#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
	int i;
	char mapping[30] = "yhesocvxduiglbkrztnwjpfmaq";
	ifstream in("D:\\A-small-attempt0.in");
	ofstream out("D:\\A-small.txt_result.txt");

	int T;
	int caseN = 1;
	char G[110], S[110]="";

	in >> T;
	in.getline(G,2);
	while (T--)
	{
		in.getline(G, 105);

		for (i=0; G[i]!='\0'; i++)
			if (G[i] == ' ') S[i] = ' ';
			else S[i] = mapping[ G[i]-97]; 
		S[i] = 0;

		out << "Case #" << caseN++ << ": " << S << endl;
	}
	
	return 0;
}