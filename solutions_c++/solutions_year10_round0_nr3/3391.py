#include<iostream>
#include<fstream>
using namespace std;
int main(void)
{
    FILE *fin = fopen("C-small-attempt0.in","r");
    FILE *fout = fopen("C-small-attempt0.out","w");
    int t,r,k,n,a[2000],sum[2000],e[2000],s0;
    long long ans;
    fscanf(fin,"%d",&t);
    for(int cas=1;cas<=t;cas++){
        fscanf(fin,"%d%d%d",&r,&k,&n);
        s0=0;
        for(int i=0;i<n;i++){
            fscanf(fin,"%d",&a[i]);
            s0+=a[i];
        }
        sum[0]=0;
        for(e[0]=0;e[0]<n;){
            if(sum[0]+a[e[0]]>k || sum[0]+a[e[0]]>s0)
                break;
            sum[0]+=a[e[0]];
            e[0]=(e[0]+1)%n;
        }
        //cout<<sum[0]<<" "<<e[0]<<endl;
        for(int i=1;i<n;i++){
            sum[i]=sum[i-1]-a[i-1];
            e[i]=e[i-1];
            while(1){
                if(sum[i]+a[e[i]]>k || sum[i]+a[e[i]]>s0)
                    break;
                sum[i]+=a[e[i]];
                e[i]=(e[i]+1)%n;
            }
            //cout<<sum[i]<<" "<<e[i]<<endl;
        }
        ans=0;
        for(int i=0,j=0;i<r;i++){
            ans+=sum[j];
            j=e[j];
        }
        fprintf(fout,"Case #%d: %I64d\n",cas,ans);
        //cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    fclose(fin);
    fclose(fout);
    //system("pause");
    return 0;
}
