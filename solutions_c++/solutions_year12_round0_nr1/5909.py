//danging

#include <iostream>
#include <map>
#include <fstream>

using namespace std;


int main(void)
{
	map<char,char> encodedecodemap;

	ifstream infile1;
	infile1.open("1.txt");

	ifstream infile2;
	infile2.open("2.txt");
	
	while(!infile1.eof() && !infile2.eof())	
	{
		string line1;
        	getline(infile1,line1);
		string line2;
		getline(infile2,line2);
		if(line1.length()==0) continue;
		encodedecodemap[line1[0]]=line2[0];
	}

	char space=' ';
	encodedecodemap[space]=space;
	encodedecodemap['q'] = 'z';
	encodedecodemap['z'] = 'q';

	/*map<char,char>::iterator itr = encodedecodemap.begin();
	while(itr!=encodedecodemap.end())
	{
		cout<<(*itr).first<<"-->"<<(*itr).second<<endl;
		itr++;
	}*/

	infile1.close();
	infile2.close();

        infile1.open("test.txt");
	string current_line;
	getline(infile1,current_line);
	int count = atoi(current_line.c_str());

	int i=1;
	while(count>0)
	{
		cout<<"Case #"<<i<<": ";
		getline(infile1,current_line);
		for(int i=0;i<current_line.length();i++)
		{
				cout<<encodedecodemap[current_line[i]];
		}
		cout<<endl;
		count--;
		i++;
	}

}
