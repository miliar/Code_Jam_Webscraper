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
	myfile.open("/home/pvirie/Downloads/B-large.in",ios::in);
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
        int N,K,B,T;
        myfile >> N;
        myfile >> K;
        myfile >> B;
        myfile >> T;

        vector< int > X;
        vector< int > V;
        X.resize(N);
        V.resize(N);
        Rep(i,N)
        {
            myfile >> X[i];
        }
        Rep(i,N)
        {
            myfile >> V[i];
        }

        vector< float > AT;
        AT.resize(N);
        Rep(i,N)
        {
            AT[i] = (B-X[i])*1.0/V[i];
        }

        int countA = 0;
        Rep(i,N) if(AT[i] <= T) ++countA;

        bool isImpossible = 0;
        if(countA < K) isImpossible = 1;

        vector< float > ST;
        ST.resize(N);
        Rep(i,N)
        {
            int index;
            int maxV = -1;
            Rep(j,N)
            {
                if(X[j] > maxV)
                {
                    index = j;
                    maxV = X[j];
                }
            }
            ST[i] = AT[index];
            X[index] = -1;
        }

        int countSwap = 0;
        int countValid = 0;
        Rep(i,N)
        {
            if(ST[i] > T)
            {
                int localSwap = 0;
                For(j,i+1,N-1)
                {
                    if(ST[j] <= T) ++localSwap;
                    if(localSwap == (K-countValid))
                    {
                        countSwap += localSwap;
                        break;
                    }
                }
            }else{
                ++countValid;
            }
        }

        //Rep(i,N) cout<<ST[i]<<" ";
        //cout<<endl;

        if(K==0) countSwap = 0;

		wfile<<"Case #"<<icase+1<<": ";
		cout<<"Case #"<<icase+1<<": ";

        if(isImpossible)
        {
            wfile<<"IMPOSSIBLE";
            cout<<"IMPOSSIBLE";
        }else{
            wfile<<countSwap;
            cout<<countSwap;
        }


		wfile<<"\r\n";
		cout<<"\r\n";


	}

    wfile.close();
	myfile.close();

	return 0;
}

