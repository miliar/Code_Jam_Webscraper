
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	string example = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";	
	string example_ori = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	bool flag = true;
	char table [26];
	memset(table, 0, 26 * sizeof(char));
	table['y'-'a'] = 'a';table['e'-'a']='o';table['q'-'a']='z';table['z'-'a'] = 'q';
	for (char a = 'a'; a <= 'z' ; a++)
	{
		int pos = example.find(a);
		if (pos != -1 && table[a-'a'] == 0)
		{
			table[a-'a'] = example_ori[pos];
		}
	}
	fstream infile, outfile;
	infile.open("input.txt", ios::in);
	outfile.open("output.txt", ios::out);
	int T = 0, line = 1;
	infile>>T;
	infile.ignore();
	while(line <= T)
	{
		string content;
		getline(infile, content);
		outfile<<"Case #"<<line++<<": ";
		for(unsigned int i = 0; i < content.length(); i++)
		{
			if (content[i] != ' ')
				outfile<<table[content[i]-'a'];
			else
				outfile<<' ';
		}
		if (line <= T)
		outfile<<endl;
	}
	cout<<"end"<<endl;
	outfile.close();
	infile.close();
}
