#include<iostream>
using namespace std;
int main()
{
    
    int t,n,order,disorder;
    FILE *fin;
    FILE *fout;
    fin=fopen("D-large.in","r");
    fout=fopen("D-large.out","w");
    fscanf(fin,"%d",&t);
    //cin>>t;
    for(int i=1;i<=t;++i)
    {
        disorder=0;
        fscanf(fin,"%d",&n);
        //cin>>n;
        for(int j=1;j<=n;++j)
        {
            fscanf(fin,"%d",&order);
            //cin>>order;
            if(order!=j)
                disorder++;
        }
    fprintf(fout,"Case #%d: %d.000000\n",i,disorder);
    //cout<<disorder;
    }
}
