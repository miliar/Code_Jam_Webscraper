#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    int i;
    long long T,N,K;
    long long pwr_2[33];
    pwr_2[0]=1;
    for(i=1;i<33;++i)
    {
        pwr_2[i]=2*pwr_2[i-1];
    }
    fin>>T;
    for(i=0;i<T;++i)
    {
        fin>>N>>K;
        fout<<"Case #"<<i+1<<": "<<(((K+1)%pwr_2[N]==0)?"ON":"OFF")<<endl;
    }
    //system("pause");
    return 0;
}
