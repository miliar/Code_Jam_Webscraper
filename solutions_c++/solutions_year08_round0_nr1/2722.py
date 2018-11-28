#include<stdio.h>
#include<iostream>
#include<string>
#include<fstream>
#include<stdlib.h>

using namespace::std;
using std::ofstream;
#define MAX_ENGINE 9


int main()
{
    int N;
    int S;
    int Q;
    int i,j,k,l;
    int a,b,c,d,e,f;

    ofstream writeToFile;
    writeToFile.open("text.txt");
    if(!writeToFile)
    {
        cout<<"Error opening file";
        exit(1);
    }
       
    
    cin>>N;
    if((N <= 0) || (N > 20))
    {
        cout<<"Not a Valid number for cases"<<endl;
        exit(1);
    }
    for(i =1 ;i<=N;i++)
    {
        cin>>S;
        if((S < 2) || (S >10))
        {
            cout<<"Not a Valid number for search engine"<<endl;
            exit(1);
        }
        char engine_name[S][100];
        for(j=0; j<=S;j++)
            gets(engine_name[j]);
        

        cin>>Q;
        if((Q < 0) || (Q >100))
        {
            cout<<"Not a Valid number for query"<<endl;
            exit(1);
        }
        
        char query_name[Q][100];
        for(k=0;k<=Q;k++)
            gets(query_name[k]);
   
        int count_arr[S];
        for(l =0;l<S;l++)
            count_arr[l]=0;

        int switching = 0;
        for(a=0;a<S;a++)
        {
            for(b=0;b<Q;b++)
            {
                if(strcmp(engine_name[a],query_name[b]) == 0)
                   ++count_arr[a];
            }
        }

     
        int temp;
        for(int p =0;p<S;p++)
        {
            for(int q = 0;q<S-1;q++)
            {
                if(count_arr[q+1]<count_arr[q])
                {
                    temp = count_arr[q];
                    count_arr[q] = count_arr[q+1];
                    count_arr[q+1]=temp;
                }
            }
        }


        if(count_arr[0] == 0)
        {
            switching = 0;
            writeToFile <<"Case #"<<i<<": "<<switching<<endl;
        }
        else
        {
            switching = count_arr[0] -1;
            writeToFile <<"Case #"<<i<<": "<<switching<<endl;
        }
        
    }
           
    writeToFile.close();    
    return 0;
}
    
        
         

    
    
