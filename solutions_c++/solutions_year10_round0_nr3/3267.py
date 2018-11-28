//C
#include<iostream>

#define MAX 2000

using namespace std;

int a[MAX];
int g[MAX];
int next[MAX];

int main(int argc,char** argv)
{
    int r,k,n;
    int runs;
    unsigned long long money;
    int temp;
    
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    
    cin>>runs;
    for(int i=0;i<runs;i++)
    {
        cin>>r>>k>>n;
        
        for(int j=0;j<n;j++)
            cin>>a[j];
            
        for(int j=0;j<n;j++)
        {   
            temp=0;
            int last=0;
            int index=0;
            while(temp<=k && index<n)
            {
                temp+=a[(j+index)%n];
                last=a[(j+index)%n];
                index++;
            }
            if(temp>k)
            {
                temp-=last;
                index--;
            }
            index=(j+index)%n;
            
            g[j]=temp;
            next[j]=index;
        }
        
        money=0;
        temp=0;
        for(int j=0;j<r;j++)
        {
            money+=g[temp];
            temp=next[temp];
        }
        
        cout<<"Case #"<<i+1<<": "<<money;
        if(i!=runs-1)
            cout<<"\n";
    }
    
    return 0;
}
