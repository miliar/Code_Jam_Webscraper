#include<iostream>
#include<fstream>

using namespace std;

int power(int ,int);

int main()
{
         int num;
         int n,k;
         
         fstream fin,fout;
         fin.open("input.txt",ios::in);         
         fout.open("output.txt",ios::out);         
         fin>>num;         
         cout<<num<<endl;
         for(int i=1;i<=num;i++)
         {
                    fin>>n;fin>>k;
                    //cout<<"i:"<<i<<"n:"<<n<<"k:"<<k;
                    if((k%power(2,n))==(power(2,n)-1))
                        fout<<"Case #"<<i<<": ON"<<endl;
                    else
                        fout<<"Case #"<<i<<": OFF"<<endl;
         }  
               
         fin.close();
         fout.close();            
         return 0;
}         

int power(int b,int e)
{
    int res=1;
    for(int i=0;i<e;i++)
            res*=2;
    return res;        
}
