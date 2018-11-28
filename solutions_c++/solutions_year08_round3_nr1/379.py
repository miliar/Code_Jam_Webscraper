#include <iostream>
using namespace std;
int comp(const void* ap,const void* bp)
{
        int a=*(int*)ap;
        int b=*(int*)bp;
        if(a>b)
                return -1;
        else if(a==b)
                return 0;
        return 1;
}
int main()
{
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
                int p,k,l;
                int arr[1001];
                long long int fs=0;
                cin>>p>>k>>l;
                for(int j=0;j<l;j++)
                        cin>>arr[j];   
                qsort(arr,l,sizeof(int),comp);
                for(int j=0;j<l;j++)
                        fs+=arr[j]*(j/k+1);
                cout<<"Case #"<<i+1<<": "<<fs<<endl;
        }
        return 0;
}
