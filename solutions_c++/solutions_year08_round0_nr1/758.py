#include <iostream>
#include <string>
using namespace std;
int main()
{
    int N;
    cin>>N;
    for(int i=1;i<=N;i++)
    {
        int Q,S,j,k,m,n,res[100]={0},sum=0,asw=0;
        char strs[100][101],strq[1000][101];
        char temp[1000];
        scanf("%d\n",&S);
        for(j=0;j<S;j++)
        {
            cin.getline(strs[j],1000);
        }
        scanf("%d\n",&Q);
        for(k=0;k<Q;k++)
        {
            cin.getline(strq[k],1001);
            for(m=0;m<S;m++)
            {
                if(strcmp(strq[k],strs[m])==0){res[m]=1;break;}
            }
            sum=0;
            for(n=0;n<S;n++)sum+=res[n];
            if(sum==S){asw++;for(n=0;n<S;n++)res[n]=0;res[m]=1;}
        }
        cout<<"Case #"<<i<<": "<<asw<<endl;
    }
    return 0;
}