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

using namespace std;

int trans_atoi (string x)
{
	return atoi(x.c_str());
}

float trans_atof (string x)
{
	return atof(x.c_str());
}




int main(int argc, char* argv[])
{

	int numCase;
	FILE* wfile;
	string line;
	char output[255];
	vector<string> tempString;
    vector< int > tempInt;

	printf("Starting... \n");

	ifstream myfile;
	myfile.open("/home/pvirie/Desktop/C-small-attempt0.in",ios::in);
	if (!myfile.is_open())
	{
	    cout <<"File not found!!"<<endl;
	    return 0;
	}
	wfile = fopen("/home/pvirie/Desktop/out.txt","w");

	getline(myfile,line);

	numCase = atoi(line.c_str());
	cout << numCase <<endl;

	for(int icase = 0;icase<numCase;++icase)
	{
		tempString.clear();
        getline(myfile,line);
		StringSplit(&line,' ',&tempString);
        tempInt.clear();
		tempInt.resize(3);
        transform(All(tempString),tempInt.begin(),trans_atoi);
        int R = tempInt[0];
        int k = tempInt[1];
        int N = tempInt[2];
		tempString.clear();
        getline(myfile,line);
		StringSplit(&line,' ',&tempString);
        tempInt.clear();
		tempInt.resize(N);
        transform(All(tempString),tempInt.begin(),trans_atoi);

        long ans = 0;
        int index = 0;
        long temp = 0;
        Rep(i,R)
        {
            temp = 0;
            Rep(j,N)
            {
                if(temp+tempInt[index] > k) break;
                temp += tempInt[index];
                index = (index+1)%N;
            }
            ans += temp;
        }

		fprintf(wfile,"Case #%d: ",icase+1);
		printf("Case #%d: ",icase+1);

        fprintf(wfile,"%d",ans);
        printf("%d",ans);

		fprintf(wfile,"\r\n");
		printf("\r\n");


	}

	fclose(wfile);
	myfile.close();

	return 0;
}

