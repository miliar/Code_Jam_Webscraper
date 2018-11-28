#include<iostream>

using namespace std;
    int N,P,S,T,total[100];
    
int getLolos()
{
    int result=0;
            for(int j=0;j<T;j++)
            {
                    if(total[j]!=0)
                    {
                    if((total[j]/3)>=P||((total[j]/3)==P-1 && total[j]%3!=0))result++;
                    else if((total[j]/3)==P-1 && total[j]%3==0 && S>0)
                    {
                        S--;
                        result++;
                    }
                    else if((total[j]/3)==P-2 &&(total[j]%3>1) && S>0)
                    {
                        S--;
                        result++;
                    }
                    }
             }
             return result;
}
int main()
{
    cin>>N;
    for(int i=1;i<=N;i++)
    {
            cin>>T;
            cin>>S;
            cin>>P;
            for(int j=0;j<T;j++)
            {
                    cin>>total[j];
            }
            if(P!=0)
            cout<<"Case #"<<i<<": "<<getLolos()<<endl;
            else
            cout<<"Case #"<<i<<": "<<T<<endl;
    }
    return 0;
}
