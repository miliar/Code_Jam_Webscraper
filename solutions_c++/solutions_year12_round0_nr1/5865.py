#include <iostream>
#include <fstream>
using namespace std;

int main ()
{
    char g[26];
    g[0]='y';
    g[1]='h';
    g[2]='e';
    g[3]='s';
    g[4]='o';
    g[5]='c';
    g[6]='v';
    g[7]='x';
    g[8]='d';
    g[9]='u';
    g[10]='i';
    g[11]='g';
    g[12]='l';
    g[13]='b';
    g[14]='k';
    g[15]='r';
    g[16]='z';
    g[17]='t';
    g[18]='n';
    g[19]='w';
    g[20]='j';
    g[21]='p';
    g[22]='f';
    g[23]='m';
    g[24]='a';
    g[25]='q';
    int n;
    ifstream input("A-small-attempt0.in");
    ofstream output ("out.txt", ios::app);
    input>>n;
    string in;
    getline(input,in);
    for(int j=1; j<=n; j++)
{

    getline(input,in);

    for(int i=0; i<in.size(); i++)
    {
        if(in[i]!=' ')
        in[i]=g[in[i]-97];
    }
    output<<"Case #"<<j<< ": " << in <<endl;
}
    input.close();
    output.close();
return 0;
}
