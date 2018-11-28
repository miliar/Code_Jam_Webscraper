#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    long T;
    ifstream fin;
    ofstream fout;
    fin.open("A-small.in");
    fout.open("A.out");
    fin>>T;
    long i,j;
    long N,K;
    long num;
    for(i=0;i<T;i++)
    {
                    fin>>N>>K;
                    //fout<<N<<K<<endl;
                    //fscanf(stdin,"%d%d",%N,&K);
                    num=1;
                    num<<=N;
                    ++K;
                    if((K%num)==0)
                                fout<<"Case #"<<i+1<<": ON"<<endl;
                    else
                                fout<<"Case #"<<i+1<<": OFF"<<endl;        
                    
    }
    fin.close();
    fout.close();
    return 0;
}
