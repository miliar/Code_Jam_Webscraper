#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

const char str[]="welcome to code jam";
char input[512];

int pp()
{
    int match[512][19]={0};
    if(input[0]==str[0]) match[0][0]=1;
    int i,j;
    for(i=1;input[i];++i)
    {
        if(input[i]==str[0]) match[i][0]=match[i-1][0]+1;
        else match[i][0]=match[i-1][0];
        for(j=1;str[j];++j)
        {
            if(input[i]==str[j]) match[i][j]=(match[i-1][j]+match[i-1][j-1])%10000;
            else match[i][j]=match[i-1][j];
        }
    }
    return match[i-1][18];
}

int main()
{
    int n;
    ifstream fin("C-large.in");
    ofstream fout("out.txt");
    fin>>n;
    fin.getline(input,512);
    for(int i=0;i<n;++i)
    {
        fin.getline(input,512);
        fout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<pp()%10000<<endl;
    }
    return 0;
}
