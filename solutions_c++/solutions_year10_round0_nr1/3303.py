#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<fstream>
#include<cmath>

#define FILE "input.txt"
#define OUTPUT_FILE "output.txt"

#define MAX 30
typedef long long unsigned int llu;

using namespace std;

ifstream in;
ofstream out;

int main()
{
in.open(FILE);
out.open(OUTPUT_FILE);

int t;
in>>t;


for(int i=0;i<t;i++)
{
        llu n,k;
        in>>n; in>>k;

        llu k_mod = (k+1) % (llu) pow(2.0,(double)n);
        
        out<<"Case #"<<i+1<<": ";
        
        if(k_mod==0) 
                       out<<"ON"<<endl;
        else                              
                       out<<"OFF"<<endl;
}

in.close();
out.close();

system("Pause");
return 0;
}
