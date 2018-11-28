#include<iostream>
#include<conio.h>
using namespace std;

int *N;
int final[50];
int main()
{
    int no_test_cases;
    cin>>no_test_cases;
    for (int i=0;i<no_test_cases;i++)
    {
        int R,k,nogrp;
        cin>>R>>k>>nogrp;
        N = new int[nogrp]; 
        
        for(int j=0;j<nogrp;j++)  //reading no of groups
            cin>>N[j];
            
        int money = 0;
        int counter=0;
        for(int j=0;j<R;j++)    //calculation
        {
                int lsum = k;
                int scount=0;
                while(lsum>0)
                {
                           
                           lsum-=N[counter];
                           if(lsum>=0)
                             {
                                     money+=N[counter];
                                     counter = (counter+1)%nogrp;
                                     scount++;
                                     if(scount>=nogrp)
                                        break;
                             }
                }
        }
        final[i]=money;
     }    
     for(int i = 0;i<no_test_cases;i++)
     cout<<"Case #"<<i+1<<": "<<final[i]<<"\n";

    
}
