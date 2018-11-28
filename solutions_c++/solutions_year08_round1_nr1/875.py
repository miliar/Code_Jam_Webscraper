#include<iostream>
using namespace std;

int main(){
    int T;
    int v1[800];
    int v2[800];
    cin >>T;
    for(int k=0;k<T;k++)
    {
            int num;
            cin >> num;
            for(int j=0;j<num;j++)
            {
                    cin >> v1[j];
            }
            for(int j=0;j<num;j++)
            {
                    cin >> v2[j];
            }
       int pro=0;     
       for(int i=0;i<num;i++)
       {
               for(int j=i-1;j>=0;j--)
               {
                       if(v1[j+1]<v1[j])
                       {
                          int temp=v1[j+1];
                          v1[j+1]=v1[j];
                          v1[j]=temp;                           
                       }
                        if(v2[j+1]>v2[j])
                       {
                          int temp=v2[j+1];
                          v2[j+1]=v2[j];
                          v2[j]=temp;
                           
                       }
               }
       }
       for(int i=0;i<num;i++)
       {
               //cout << v1[i] <<" "<< v2[i] << endl; 
               pro+=v1[i]*v2[i];
       }
       cout <<"Case #"<<k+1<<": "<< pro<<endl;    
    }
    return 0;
}