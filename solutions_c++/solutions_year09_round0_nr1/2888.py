#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int l , d , n;
    int i , j , k , t ,blog , i1 , j1 ,sum;
    string test;
    char aa[5001][15];
    int temp1, tlong[15];
    int bb[5001];
    freopen("d:\\A-large.in", "r", stdin);
    freopen("d:\\A-large.out", "w", stdout);
    cin>>l>>d>>n;
    for(i=0;i<d;i++)
        for(j=0;j<l;j++)
        {
            cin>>aa[i][j];
        }
    for(i=0;i<n;i++)
    {
        char temp[15][26];
        temp1=0;t=0;
        cin>>test;
        memset(bb,0,sizeof(bb));
        memset(tlong,0,sizeof(tlong));
        k=test.length();
        blog=0;
        for(j=0;j<k;j++)
        {   
            if(test[j]=='('){blog=1;continue;}
            else if(test[j]==')'){blog=0;tlong[temp1]=t;temp1++;t=0;}
            else if(blog==1){temp[temp1][t]=test[j];t++;}
            else if(blog==0){temp[temp1][t]=test[j];tlong[temp1]=1;temp1++;}
            
        }       
        sum=0;
        for(i1=0;i1<l;i1++)
        {           
           for(j1=0;j1<d;j1++)
           { blog=0;
             if(1==bb[j1]||0==i1)
             {
             for(t=0;t<tlong[i1];t++)
             {
                 if(aa[j1][i1]==temp[i1][t]){bb[j1]=1;blog=1;continue;}
                 
             }
             if(0==blog)bb[j1]=-1;
             } 
            
           }
             // for(j1=0;j1<d;j1++)cout<<bb[j1];     
                           
          }    
         for(j1=0;j1<d;j1++)if(1==bb[j1])sum++;
         cout<<"Case #"<<i+1<<": "<<sum<<endl; 
    }  cin>>l;      
}    
