#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string name("A-small-attempt0");
	int nbCases = 0;
	ifstream in;
	ofstream out;

	//char table[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
	char table[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char str[102];
	int j;

	// Variables end -------------------------------------------------------------------------

	in.open((name + ".in").c_str());
	out.open((name + ".out").c_str()); // flux opening

	if(!(in.is_open() && out.is_open()))
	{
		cerr << "> one of the file could not be loaded" << endl;
	}

	in >> nbCases; // getting case number
	in.getline(str, 10); // to go to the line after definition of the number of cases

	for(int i=1;i<=nbCases;i++)
	{
		out << "Case #" << i << ": ";
		str[0]='\0';
		in.getline(str, 101);
		j=0;
		while(str[j] !='\0')
		{
			if(str[j]>= 'a' && str[j] <= 'z')
				out << table[str[j]-'a'];
			else if(str[j]==' ')
				out << ' ';

			j++;
		}

		if(i!=nbCases)
			out << endl;
	}

    in.close();
    out.close();

    return 0;
}
