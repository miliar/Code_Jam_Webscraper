#include <iostream>
using namespace std;
int main()
{
    FILE *fin;
    FILE *fout;
    fin=fopen("C-large.in","r");
    fout=fopen("C-large.out","w");
    int t,n,qua[1001],temp,smallest,pos,sum;
    fscanf(fin,"%d",&t);
    //cin>>t;
    for (int i=1;i<=t;++i)
    {
        temp=0;
        sum=0;
        pos=0;
        smallest=1000001;
        fscanf(fin,"%d",&n);
        //cin>>n;
        for(int j=1;j<=n;++j)
        {
            fscanf(fin,"%d",&qua[j]);
            //cin>>qua[j];
            temp=qua[j]^temp;
            if(qua[j]<smallest)
            {
                smallest=qua[j];
                pos=j;
            }
        }
        if(temp!=0)
            fprintf(fout,"Case #%d: NO\n",i);
            //cout<<"NO"<<endl;
        else
        {
            qua[pos]=0;
            for(int j=1;j<=n;++j)
            sum=sum+qua[j];
            fprintf(fout,"Case #%d: %d\n",i,sum);
            //cout<<sum<<endl;
        }
    }
}
