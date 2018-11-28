#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int T,N;
    int i,j;
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    fin>>T;
    unsigned long long min=1000001,C,fv=0,total=0;
    for(i=0;i<T;i++)
    {
                    fin>>N;
                    fv=0;
                    total=0;
                    min=1000001;
                    for(j=0;j<N;j++)
                    {
                                    fin>>C;
                                    fv^=C;
                                    if(C<min)
                                    min=C;
                                    total+=C;
                    }
                    if(fv==0)
                    {
                             fout<<"Case #"<<i+1<<": "<<total-min<<"\n";
                             cout<<"Case #"<<i+1<<": "<<total-min<<"\n";
                    }
                    else
                    {
                    fout<<"Case #"<<i+1<<": "<<"NO"<<"\n";
                    cout<<"Case #"<<i+1<<": "<<"NO"<<"\n";                        
                    }
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
