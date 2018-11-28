#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    fstream  fout;
    fout.open("1.txt",ios::out);
    int T,N,L,H;
    cin>>T;
    int data[110];
    int i;
    for(i=0;i<T;i++)
    {
                    fout<<"Case #"<<i+1<<": ";
                    cin>>N>>L>>H;
                    int j,t;
                    for(j=0;j<N;j++)
                    {
                                    cin>>data[j];
                    }
                    for(j=L;j<=H;j++)
                    {
                                     
                                     for(t=0;t<N;t++)
                                     {
                                                    // cout<<j<<' '<<data[t]<<' '<<int(j/data[t])*data[t]<<"\n";
                                                     if(int(j/data[t])*data[t]!=j&&int(data[t]/j)*j!=data[t])break;
                                     }
                                 //    cout<<t<<endl;
                                     if(t==N)break;
                    }
                    if(j>H)fout<<"NO\n";
                    else fout<<j<<"\n";
}
    fout.close();
   // cin>>i;
    return 0;
    
}
 
