#include <iostream>
#include <fstream>
#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "string.h"
#include "limits.h"
#include <algorithm>
#include <map>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
#include "djs.h"
#include "V_Utilities.h"
#include "mVect.h"
#include "bigint/BigIntegerLibrary.h"

using namespace std;

int trans_atoi (string x)
{
	return atoi(x.c_str());
}

float trans_atof (string x)
{
	return atof(x.c_str());
}

struct DIR
{
  string name;
  vector< DIR > child;

  DIR()
  {

  }

  DIR(string n)
  {
     name = n;
  }

  int contains(string n)
  {
     Rep(i,child.size())
     {
        if(child[i].name.compare(n) == 0)
        {
            return i;
        }
     }
     return -1;
  }

};

int main(int argc, char* argv[])
{

	int numCase;
	string line;
	char output[255];
	vector<string> tempString;
    vector< int > tempInt;
    vector< BigUnsigned > tempLong;
    vector< double > tempDouble;

	printf("Starting... \n");

	ifstream myfile;
	ofstream wfile;
	myfile.open("/home/pvirie/Downloads/A-large.in",ios::in);
	wfile.open("/home/pvirie/codeblocks/CodeJam/out.txt",ios::out);
	if (!myfile.is_open())
	{
	    cout <<"File not found!!"<<endl;
	    return 0;
	}

	myfile >> numCase;
	cout << numCase <<endl;


	for(int icase = 0;icase<numCase;++icase)
	{
        int N,M;
        myfile >> N;
        myfile >> M;

        DIR root;

        Rep(i,N)
        {
            myfile >> line;
            tempString.clear();
            StringSplit(&line,'/',&tempString);
            DIR *node = &root;
            Rep(j,tempString.size())
            {
                int temp = node->contains(tempString[j]);
                if(temp >= 0)
                {
                    node = &((node->child)[temp]);
                }else{
                    node->child.push_back(DIR(tempString[j]));
                    node = &((node->child)[node->child.size()-1]);
                }
            }
        }

        int count = 0;

        Rep(i,M)
        {
            myfile >> line;
            tempString.clear();
            StringSplit(&line,'/',&tempString);
            DIR *node = &root;
            Rep(j,tempString.size())
            {
                int temp = node->contains(tempString[j]);
                if(temp >= 0)
                {
                    node = &((node->child)[temp]);
                }else{
                    ++count;
                    node->child.push_back(DIR(tempString[j]));
                    node = &((node->child)[node->child.size()-1]);
                }
            }
        }

		wfile<<"Case #"<<icase+1<<": ";
		cout<<"Case #"<<icase+1<<": ";

        wfile<<count;
        cout<<count;

		wfile<<"\r\n";
		cout<<"\r\n";


	}

    wfile.close();
	myfile.close();

	return 0;
}

