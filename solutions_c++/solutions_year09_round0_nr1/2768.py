#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
	int L, D, N;
	int CaseNo = 1;
	ifstream in("input.in");
	ofstream out("output.out");
	
	in >> L >> D >> N;
	string s[5000];

	for(int i=0;i<D;i++)
		in >> s[i];

	for(int i=0;i<N;i++)
	{
		string word[15];
		string caseString;
		in >> caseString;

		for(int index=0, w=0;w<L;)
		{
			if(isalpha(caseString[index]))
			{
				word[w++]=caseString[index];
			    index++;
			}else{
				int endIndex = caseString.find_first_of(')',index);
				word[w++] = caseString.substr(index+1, endIndex-index-1 );
				index = endIndex+1;
			}
		}

		int x=0, count=0;
		for(x=0, count=0;x<D;x++)
		{
			bool isMatch = true;
			for(int k=0;k<L;k++)
			{
				if(word[k].find_first_of(s[x][k])==-1)
					isMatch = false;
			}
			if(isMatch)
				count++;
		}

		out << "Case #" << CaseNo++ << ": " << count << endl;
	}

	return 0;
}