#include<iostream>
#include<conio.h>
using namespace std;
 main()
{
       
     int n;
     
     cin>>n;
     char S[n+1][1000];
     int G[26]={24,6,2,15,10,-3,15,16,-5,11,-2,-5,-1,-12,-4,2,9,2,-5,3,-11,-6,-17,-11,-24,-9};
cin.ignore(1000,'\n');
 
   for (int i=0;i<n;i++)
        cin.getline(S[i],1000);

   
     
    for(int i=0;i<n;i++)
        {cout<<"Case #"<<i+1<<": ";
        for(int j=0;S[i][j]!='\0';j++)
        { 
       if(S[i][j]==' '){
        cout<<" ";
        continue;}
       S[i][j]+=G[S[i][j]-97];
        cout<<S[i][j];
        }
        cout<<endl;
        }
        
   getchar();
     }
