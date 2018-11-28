#include<iostream>
using namespace std;

#include<algorithm>
int p,q;
int flag[1002],cell[100];

int fun(){
    int result=0;
    for(int i=0;i<q;i++){
            flag[cell[i]]=0;
            for(int j=cell[i]+1;j<p&&flag[j]==1;j++)
            result++;
            for(int j=cell[i]-1;j>=0&&flag[j]==1;j--)
            result++;
            }
            return result;
    }    
    
int main(){
    int cas;
    int out[100];
    
    cin>>cas;
    for(int j=1;j<=cas;j++){
        cin>>p>>q;
        int temp;
        for(int i=0;i<q;i++){
        cin>>temp;
        cell[i]=temp-1;
        }
        for(int i=0;i<p;i++)
        flag[i]=1;
        int min=-1;
        do{
                          
                    int l=fun();
                    //cout<<l<<endl;
                    if(min==-1)
                    min=l;
                    if(min>l)
                    min=l;
                    for(int i=0;i<p;i++)
                    flag[i]=1;
                    //cout<<"repeat"<<endl;
        }
                  
        while(next_permutation(cell,cell+q));
        out[j-1]=min;
        
        }
        for(int j=1;j<=cas;j++)
        cout<<"Case #"<<j<<": "<<out[j-1]<<endl;
       
        return 0;
}        
