#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        int n,A,B,C,D,X,Y,M;
        long long x[101]={0},y[101]={0},asw=0;
        cin>>n>>A>>B>>C>>D>>X>>Y>>M;
        x[0]=X;y[0]=Y;
        for(int jj=1;jj<n;jj++)
        {
            x[jj]=(A*x[jj-1]+B)%M;
            y[jj]=(C*y[jj-1]+D)%M;
        }
        asw=0;
        for(int j=0;j<n;j++)
        {
            for(int k=j+1;k<n;k++)
            {
                for(int l=k+1;l<n;l++)
                {
                    long long temp1=(x[j]+x[k]+x[l]),temp2=(y[j]+y[k]+y[l]);
                    if(((temp1/3)==double(temp1)/double(3))&&((temp2/3)==double(temp2)/double(3)))
                        asw++;
                }
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<asw<<endl;
    }
    return 0;
}
