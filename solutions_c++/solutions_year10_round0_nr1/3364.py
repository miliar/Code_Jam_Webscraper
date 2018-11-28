//A
#include<iostream>

#define MAX 2000

using namespace std;

typedef struct tagBulb
{
    int left;
    int state;
    int right;
}Bulb;

Bulb* b;

int main(int argc,char** argv)
{
    int runs;
    int n,k;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    
    cin>>runs;
    for(int i=0;i<runs;i++)
    {
        cin>>n>>k;
        b = new Bulb[n];
        for(int j=0;j<n;j++)
        {
            b[j].left=0;
            b[j].state=0;
            b[j].right=0;
        }
        b[0].left=1;
        
        for(int j=0;j<k;j++)
        {
            for(int index=0;index<n;index++)
            {
                if(b[index].left==1)
                    b[index].state=1-b[index].state;
            }
            for(int index=0;index<n;index++)
            {
                b[index].right=b[index].left*b[index].state;
                if(index<n-1)
                    b[index+1].left=b[index].right;
            }            
        }
        
        bool flag=true;
        for(int j=0;j<n;j++)
            if(b[j].left*b[j].state*b[j].right==0)
            {
                flag=false;
                break;
            }
        
        
        cout<<"Case #"<<i+1<<": ";
        if(flag)
            cout<<"ON";
        else
            cout<<"OFF";
        
        if(i!=runs-1)
            cout<<"\n";
    }
    
    return 0;
}
