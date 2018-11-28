#include<iostream>
using namespace std;
int main()
{
    int T,N,L,H,freq[105],flag,final;
    cin>>T;
    for(int i=0;i<T;i++)
    {
            cin>>N>>L>>H;
            for(int j=0;j<N;j++)
                    cin>>freq[j];
            for(int k=L;k<=H;k++)
            {
                    flag=0;
                    for(int j=0;j<N;j++)
                    {
                            if(k%freq[j]!=0&&freq[j]%k!=0)
                            {
                                 flag=-1;
                                 break;
                            }
                    }
                    if(flag==0)
                    {
                               final=k;
                               break;
                    }
            }
            cout<<"Case #"<<i+1<<": ";
            if(flag==-1)
                        cout<<"NO\n";
            else
                cout<<final<<"\n";
  }
  return 0;
}
