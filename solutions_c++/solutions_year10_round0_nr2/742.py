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

long gcd(long a, long b)
{
	if(b == 0)
	{
        return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}


int main(int argc, char* argv[])
{

	int numCase;
	FILE* wfile;
	string line;
	char output[255];
	vector<string> tempString;
    vector< int > tempInt;
    vector< long > tempLong;

	printf("Starting... \n");

	ifstream myfile;
	myfile.open("/home/pvirie/Downloads/B-small-attempt2.in",ios::in);
	if (!myfile.is_open())
	{
	    cout <<"File not found!!"<<endl;
	    return 0;
	}
	wfile = fopen("/home/pvirie/Desktop/out.txt","w");

	getline(myfile,line);

	numCase = atoi(line.c_str());
	cout << numCase <<endl;

    vector<long> diff;

	for(int icase = 0;icase<numCase;++icase)
	{
		tempString.clear();
		int N;
		myfile>>N;
        tempLong.clear();
		tempLong.resize(N);
        Rep(i,N) myfile>>tempLong[i];

        diff.clear();
        Rep(i,N)
            For(j,i+1,N-1)
            {
                diff.push_back(abs(tempLong[i]-tempLong[j]));
            }

        int M = diff.size();

        Repd(i,M)
        {
            Rep(j,i) diff[j] = gcd(diff[j],diff[j+1]);
        }
        long ans = 0;
        if(tempLong[0]%diff[0] != 0)
            ans = (tempLong[0]/diff[0] + 1)*diff[0] - tempLong[0];

//        Rep(i,N) cout<<" "<<tempLong[i]+ans;
//        cout<<endl;
//        cout<<"GCD "<<diff[0]<<endl;

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

