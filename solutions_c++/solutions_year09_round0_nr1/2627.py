#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>




using namespace std;

int main()
{
	int length,totalline,test;
	ifstream infile;
	infile.open("in");
    if (!infile) {
		cerr << "error: unable to open input file: "
			 << endl;
	    return -1;
	}
	ofstream outfile;
	outfile.open("out.txt");

	string meta;
	getline(infile,meta);
	istringstream stream(meta);
	stream >> length >> totalline >> test;
	
	// malloc size for string L
	vector<string> totalstring;
	for (int i=0;i<totalline;i++)
	{
		string temp;
		getline(infile,temp);
		totalstring.push_back(temp); 
	}
	// malloc record list;
	char *record = (char *)malloc(sizeof(char)*totalline);
	memset(record,0,totalline*sizeof(char));
	// answer;
	int *answer = (int *)malloc(sizeof(int)*test);
	memset(answer,0,test*sizeof(int));
	// check the pattern
	for (int j=0;j<test;j++)
	{
		string pattern;
		getline(infile,pattern);
		int num = 0,inside = 0;
		for (int k=0;k<(signed)pattern.size();k++)
		{
			if(pattern[k] == '(')
			{
				num++;
				inside = 1;
				continue;
			}
			if (pattern[k] == ')')
			{
				inside = 0;
				continue;
			}
			if (pattern[k] >= 'a' && pattern[k] <= 'z')
			{
				if (inside == 0)
					num++;
				for (int m=0;m<totalline;m++)
				{
					if (totalstring[m][num-1] == pattern[k])
					{
						record[m]++;
					}
				}

			}
		}
		for (int l=0;l<totalline;l++)
		{
			if (record[l]==length)
			{
				answer[j]++;
			}
		}
		memset(record,0,totalline*sizeof(char));
	}
	for (int q=0;q<test;q++)
	{
		outfile << "Case #"<<q+1<<": "<<answer[q]<<endl;
	}
	infile.close();
	outfile.close();
}

