#include <string>
#include <vector> 
#include <iostream>
#include <fstream> 
#include <stdio.h>
 
using namespace std;   
 
int main()
{ 
    ifstream inf("D:\\in.txt");
    ofstream outf("D:\out.txt");
    int T;
    string s;
    getline(infile, s);
    T = atoi(s.c_str()); 	
    int ind[50];
    ind[0] = 0;

    for (int j = 1; j < 50; ++j)
    {
	ind[j] = 2 * ind[j - 1] + 1;
    }
 
    for (int i = 0; i < T; ++i)
    {	
	string res;
	getline(infile, s);		 
	int p = s.find(' ');						
	int N = atoi(s.substr(0, p).c_str());
	int K = atoi(s.substr(p).c_str());
	K = K % (ind[N] + 1);
	if (K == ind[N])
	{
		res = "ON";
	}
	else
	{
		res = "OFF";		
	}
	outfile << "Case #" << i + 1 << ": " << res << endl;		
    }
    inf.close();
    outf.close();	 
 
    return;
} 
 