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
	myfile.open("/home/pvirie/Downloads/A-large.in",ios::in);
	wfile.open("/home/pvirie/codeblocks/CodeJam/out.txt",ios::out);
	if (!myfile.is_open())
	{
	    cout <<"File not found!!"<<endl;
	    return 0;
	}

	myfile >> numCase;
	cout << numCase <<endl;

    vector< vector< char > > array;

	for(int icase = 0;icase<numCase;++icase)
	{
	    bool blue = 0,red = 0;
        int N,K;
        myfile >> N;
        myfile >> K;
        array.clear();
        Rep(i,N)
        {
            myfile >> line;
            vector< char > aline;
            aline.resize(N);
            fill(All(aline),'.');
            int k = 0;
            Repd(j,N)
            {
                if(line[j] != '.')
                 aline[k++] = (line[j]);
            }

            array.push_back(aline);
        }

        For(i,0,N-K)
            For(j,0,N-K)
            {
                char value = array[i][j];
                bool flag = 1;
                Rep(k,K)
                {
                    if(array[i+k][j+k] != value)
                    {
                        flag = 0;
                        break;
                    }
                }
                if(flag && value == 'R') red = 1;
                if(flag && value == 'B') blue = 1;

                value = array[i+K-1][j];
                flag = 1;
                Rep(k,K)
                {
                    if(array[i+K-1-k][j+k] != value)
                    {
                        flag = 0;
                        break;
                    }
                }
                if(flag && value == 'R') red = 1;
                if(flag && value == 'B') blue = 1;
            }

        Rep(i,N)
        {
            char row,col;
            row = array[i][0];
            col = array[0][i];
            int rcon = 1;
            int ccon = 1;

            For(j,1,N-1)
            {
                char r = array[i][j];
                char c = array[j][i];

                if(r != '.' && r == row) {++rcon;}
                else {
                    row = r;
                    rcon = 1;
                }

                if(c != '.' && c == col) {++ccon;}
                else {
                    col = c;
                    ccon = 1;
                }

                if(rcon >= K)
                {
                    if(row == 'R') red = 1;
                    if(row == 'B') blue = 1;
                }


                if(ccon >= K)
                {
                    if(col == 'R') red = 1;
                    if(col == 'B') blue = 1;
                }
            }

        }

		wfile<<"Case #"<<icase+1<<": ";
		cout<<"Case #"<<icase+1<<": ";

        if(red && blue)
        {
            wfile<<"Both";
            cout<<"Both";
        }else if(red)
        {
            wfile<<"Red";
            cout<<"Red";
        }else if(blue)
        {
            wfile<<"Blue";
            cout<<"Blue";
        }else
        {
            wfile<<"Neither";
            cout<<"Neither";
        }

		wfile<<"\r\n";
		cout<<"\r\n";


	}

    wfile.close();
	myfile.close();

	return 0;
}

