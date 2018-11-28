// GoogleProblem1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
class Token

{

    private:

        friend std::ostream& operator<<(std::ostream&,Token const&);

        friend std::istream& operator>>(std::istream&,Token&);

public:

        std::string     value;

};

std::istream& operator>>(std::istream& str,Token& data)

{

    // Check to make sure the stream is OK.

    if (!str)

    {   return str;

    }

    char    x;

    // Drop leading space

    do

    {

        x = str.get();

    }

    while(str && isspace(x) && (x != '\n'));



    // If the stream is done. exit now.

    if (!str)

    {

        return str;

    }



    // We have skipped all white space up to the

    // start of the first token. We can now modify data.

    data.value  ="";



    // If the token is a '\n' We are finished.

    if (x == '\n')

    {   data.value  = "\n";

        return str;

    }



    // Otherwise read the next token in.

    str.unget();
    str >> data.value;
    return str;

}

std::ostream& operator<<(std::ostream& str,Token const& data) {
    return str << data.value;
}

struct InputPattern
{
	vector<char> data;
	bool bVariable;
	InputPattern():bVariable(false){}
};

void FindingTheInput(vector<InputPattern>& data,string strVal) 
{
	int i=0;
	while(i<strVal.size())
	{
		InputPattern input;
		if(strVal[i] == '(')
		{
			++i;
			while( strVal[i] !=')')
			{
				input.data.push_back(strVal[i]);
				input.bVariable = true;
				++i;
			}
			data.push_back(input);
			++i;
		}
		else
		{
			input.data.push_back(strVal[i]);
			data.push_back(input);
			++i;
		}
	}
}

int CalculateCase(vector<InputPattern> data,vector<string> strVals)
{
	int Case = 0;
	for(int i=0; i<strVals.size(); ++i)
	{
		int k=0;
		bool ProceedFlag = true;
		while(ProceedFlag && k<strVals[i].size())
		{
			ProceedFlag = false;
			if(data[k].bVariable)
			{
			for(int j=0; j<data[k].data.size(); ++j)
			{
				if(data[k].data[j] == strVals[i][k])
				{
					ProceedFlag = true;
				}
			}
			}
			else if(data[k].data[0] == strVals[i][k])
			{
				ProceedFlag = true;
			}
			else
			{
				ProceedFlag = false;
			}
			k++;
		}
		if(k == strVals[i].size())
		{
			if(ProceedFlag)
			{
				Case++;
			}
		}
	}
	return Case;
}

int _tmain(int argc, _TCHAR* argv[])
{
	vector<string> aliendictinary;
	ifstream f("C:\\indrajitpractice.txt");
	ofstream fout("C:\\Output.txt");
	Token x;
	int length = 0;
	int numWords = 0;
	int numCases = 0;
	f >> x;
	if(x.value == "")
	{
		f>>x;
	}
	length = atoi(x.value.c_str());
	f>>x;
	if(x.value == "")
	{
		f>>x;
	}
	numWords = atoi(x.value.c_str());
	f>>x;
	if(x.value == "")
	{
		f>>x;
	}
	numCases = atoi(x.value.c_str());

	for(int i=0; i<numWords; ++i)
	{
		f>>x;
		if(x.value == "\n")
		{
			f>>x;
		}
		aliendictinary.push_back(x.value);
	}
	for(int i=0; i<numCases; ++i)
	{
		vector<InputPattern> dataInput;
		f>>x;
		if(x.value == "\n")
		{
			f>>x;
		}
		FindingTheInput(dataInput,x.value);
		int Case = CalculateCase(dataInput,aliendictinary);
		fout<<"Case #"<<i+1<<": "<<Case<<"\n";
	}
	f.close();
	fout.close();
	return 0;
}

