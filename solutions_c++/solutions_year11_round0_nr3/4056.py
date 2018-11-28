#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<fstream>
#include<limits.h>
using namespace std;

int main()
{
       
       int t;
       scanf("%d",&t);
       int max=t;
       ofstream f1 ("new.txt");
       
       do
       {
                      long low=LONG_MAX;
                      long sum=0;
                      long arr[100];
            long n;
            cin>>n;
            long ub=0;
            long suma=0;
            for(int i=0;i<n;i++)
            {
                    cin>>arr[ub++];
                    if(arr[ub-1]<low)
                                     low=arr[ub-1];
                    sum=sum^arr[ub-1];
                    suma=suma+arr[ub-1];
            }   
            //cout<<sum;
            if(sum==0)
            {
              //cout<<suma-low;
              f1<<"Case #"<<max-t+1<<": "<<(suma-low)<<endl;
            }
            else
                f1<<"Case #"<<max-t+1<<": NO"<<endl;
            
            
            
            
            
            
            //getch();   
            t--;
            }while(t!=0);
            
            }
