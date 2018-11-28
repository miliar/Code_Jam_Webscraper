#include<iostream>
#include<fstream>

using namespace std;

int two(int);

main()
{
         int cases;
         int i,n,k;
         
         ifstream fin;fin.open("in.txt");           
         ofstream fout;fout.open("out.txt");       
                           
         fin>>cases;         
         
         for(i=1;i<=cases;i++)
         {
                    fin>>n;
                    fin>>k;
                    
                    if((k%two(n))==(two(n)-1))
                        fout<<"Case #"<<i<<": ON"<<endl;
                    else
                        fout<<"Case #"<<i<<": OFF"<<endl;
         }  
               
         fin.close();fout.close();            
}         

int two(int exp)
{
    int ans=1;
    for(int i=0;i<exp;i++)
            ans=ans*2;
    return ans;        
}
