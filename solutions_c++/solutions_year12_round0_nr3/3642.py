#include<iostream>
#include<cstdio>
#include<conio.h>
#include<string.h>
using namespace std;

int arr[20000001];

int main()
{
long i,c;
long a,b;
char num[10];
char temp[10];

//for(i=0;i<20000001;i++)
//arr[i]=0;
int t;

freopen("input.in","r",stdin);
freopen("output.out","w+",stdout);

cin>>t;

int i1;

for(i1=0;i1<t;i1++)
{
                   


cin>>a;
cin>>b;
int count=0;

for(i=a;i<b;i++)
{
                        int l;
                        sprintf(num,"%ld",i);
                        l=strlen(num);
                                                
                        int j;
                        for(j=l-1;j>0;j--)
                        {
                                        int p=l-j;
                                        int k;
                                        for(k=0;k<j;k++)
                                        {
                                                        temp[k+p]=num[k];
                                        }
                                        for(k=j;k<l;k++)
                                        {
                                                        temp[k-j]=num[k];
                                        }
                                        temp[l]='\0';
                                        c=atol(temp);
                        if((c>i)&&(c<=b))count++;
                       }
}   

    cout<<"Case #"<<(i1+1)<<": "<<count<<endl;
}                 
    
}                    
                                        

                       
