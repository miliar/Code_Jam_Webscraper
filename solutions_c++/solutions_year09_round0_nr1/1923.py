/*
Task: A 
Lang: C++
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>

#define SP system("pause")

using namespace std;

ifstream ff;
ofstream of;

vector< string > words; 

int main()
{
    int L,D,N;
    int otg=0;
    ff.open("A-la.in");
    of.open("A-lang.out");
    ff>>L>>D>>N;
    words.resize(D);
    for(int i=0; i<D; i++)
    {
            ff>>words[i];
           // cout<<words[i]<<"  !@ ";
    }
    string f;
    for(int i=0; i<N; i++)
    {
            otg=0;
            ff>>f;
            //cout<<f<<endl;
            //SP;
            for(int j=0; j<D; j++)
            {
                    int l=0;
                    int k=0;
                    int k1=0;
                    for(int z=0; z<f.size(); z++)
                    {
                            if(f[z]=='(')k=1;
                            else
                            if(f[z]==')'){k=0;if(k1==0)break; k1=0;l++;}
                            else
                            if(k==0 && words[j][l]==f[z] )l++;
                                else
                                if(k==0 && words[j][l]!=f[z] )break;
                                else
                                if(k==1 && words[j][l]==f[z] )k1=1;
                            
                    }
                    if(l>=L)otg++;
            }
            //cout<<otg<<endl;
            //SP;
            of<<"Case #"<<i+1<<": "<<otg<<endl;
    }
   // SP;
    return 0;
}
