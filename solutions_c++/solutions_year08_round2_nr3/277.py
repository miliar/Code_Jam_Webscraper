#include <iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    for(int ii=0;ii<N;ii++)
    {
        int K,n,a[5001]={0},key[101]={0},b[5001]={0};
        scanf("%d%d",&K,&n);
        for(int i=0;i<n;i++){scanf("%d",&key[i]);}
        int q=1,p=1,temp=1;
        while(p<=K)
        {
            if(b[q]==0&&temp==p)
            {
                a[q]=p;b[q]=1;
                p++;temp=0;
            }
            q++;
            if(q>K)q=q%(K);temp+=(1-b[q]);
        }
        cout<<"Case #"<<(ii+1)<<":";
        for(int i=0;i<n;i++)
            printf(" %d",a[key[i]]);
        cout<<endl;
    }
    return 0;
}
