#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include "string.h"

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

std::ostream& operator<<(std::ostream& str,Token const& data)

{

	return str << data.value;

}

int getMoney(const int& rotation, const int& maxcapacity, vector<int> vtVals)
{
    int totalmoney = 0;
    for(int i=0; i<rotation; ++i)
    {
            bool flag = true;
            int j = 0;
            int sum = 0;
            int previoussum;
            while(flag )
            {
                    previoussum = sum;
                    if(j < vtVals.size())
                    {
                         sum += vtVals[j];
                    }
                    if(sum > maxcapacity)
                    {
                         flag = false;  
                    }
                    else 
                    {
                         if(j<vtVals.size())
                         {
                              j = j+1;
                         }
                         else
                         {
                             flag = false;
                         }
                    }
            }
            for(int k=0; k<j; ++k)
            {
                    vtVals.push_back(vtVals[k]);
            }
            for(int l=0; l<j; ++l)
            {
                    vtVals.erase(vtVals.begin());        
            }
            totalmoney += previoussum;
    }
    return totalmoney;
}
int main(int argc, char *argv[])
{
    ifstream myfile;
    ofstream outfile("Output.txt");
    myfile.open("Indra.txt");
    if (!myfile) {
    cout << "Unable to open file datafile.txt";
    }
    Token x;
    int numberofcases;
    myfile>>numberofcases;
    //numberofcases = atoi(x.value.c_str());
    //cout<<numberofcases; 
    for(int j=0; j<numberofcases; ++j)
    {
    int rotation_val , capacity ,totalgroups;
    myfile>>rotation_val;
    //cout<<rotation_val;
    myfile>>capacity;
    //cout<<capacity;
    myfile>>totalgroups;
    //cout<<totalgroups;
    vector<int> vals;
    vals.resize(totalgroups);
    for(int i=0; i<totalgroups; ++i)
    {
            myfile>>vals[i];
    }
    int out = getMoney(rotation_val,capacity,vals);
    outfile<<"Case #"<<j+1<<":"<<" "<<out<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
