#include <iostream>
#include <fstream>

using namespace std;
////ring mapping="abcdefghijklmnopqrstuvwxyz";
//string mapping="ynficwlbkuomxsevzpdrjgthaq";

//ring mapping="abcdefghijklmnopqrstuvwxyz";
string mapping="yhesocvxduiglbkrztnwjpfmaq";

//ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv
//our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up
string tongue(string line)
{
       string space = " ";
       for(int i=0; i<line.length(); i++)
               if(line[i]!=space[0])
                             line[i]=mapping[(int)line[i]-97];
       return line;
}

int main()
{
	ifstream infile ("A-small-attempt0.in");
	ofstream outfile("A.out");

	int N;
	infile >> N;
	string line;
	char tab[1000];
	getline (infile,line);
	for(int i=0; i<N; i++)
	{
        outfile << "Case #" << i+1 << ": ";
        //infile >> line;
        //cout << line << endl;
        getline (infile,line);
        //cout << line[1] << endl;
        //cout << tab << endl;
        outfile << tongue(line);
        outfile << "\n";
    }


	infile.close();
	outfile.close();
	system("pause");
}
