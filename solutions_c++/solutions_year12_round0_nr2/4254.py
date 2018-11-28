#include<iostream>
#include<fstream>
#include<conio.h>
#include<string.h>
using namespace std;
int main()
{
    int n,c,t,N,p,d,A[100];
    char ch;
    ifstream fin;
    ofstream fout;
    fin.open("B.in",ios::in);
    fout.open("B.out",ios::out);
    fin>>n;
    
    for(int i = 0;i<n;i++)
    { c=0;
   
       fin>>N;
       fin>>p;
       fin>>d;
       t = d*3;
       
       for(int k =0;k<N;k++)
       { fin>>A[k];
       
               if(A[k]>=t-2)c++;
       else if((A[k]==t-3||A[k]==t-4)&&p>0&&A[k]>0)
                 {c++;p--;}
               }
        fout<<"Case #"<<i+1<<": "<<c;

       
                fout<<endl;
            }
    getch();
    fin.close();
    fout.close();
    }
