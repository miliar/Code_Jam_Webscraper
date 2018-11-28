#include<iostream>
#include<fstream>
#include<cstring>


using namespace std;
typedef struct st
{
        char r;
        int p;
};
st seq[100];

long long N;

long int solution()
{
    long long po=1,pb=1;
    long long timeo=0,timeb=0,time=0,addt;
    long long i;
    long long k=0;
    for(i=0;i<N;i++)
    {
                    cout<<seq[i].p<<" ";
                    if(seq[i].r=='O')
                    {
                                     addt=max((abs(po-seq[i].p)-timeb),(long long)0)+1;
                                     //cout<<"addt"<<addt<<"\n";
                                     timeo+=addt;
                                     timeb=0;
                                     po=seq[i].p;
                    }
                    else
                    {
                        addt=max(abs(pb-seq[i].p)-timeo,(long long)0)+1;
                                     //cout<<"addt"<<addt<<"\n";
                        timeb+=addt;
                        timeo=0;
                        pb=seq[i].p;
                    }
                    time+=addt;
    }
    return time;
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    long long i,j;
    long long ans;
    char x;
    for(i=0;i<T;i++)
    {
                    fin>>N;
                    for(j=0;j<N;j++)
                    {
                                    fin>>seq[j].r;
                                    //fflush()stdin
                                    fin>>seq[j].p;
                                    //cout<<seq[j].r<<seq[j].p<<"\n";
                    }
                    ans=solution();
                    fout<<"Case #"<<i+1<<": "<<ans<<"\n";
                    cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
