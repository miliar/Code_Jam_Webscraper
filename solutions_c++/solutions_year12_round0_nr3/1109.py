#include <iostream>
#include <string.h>
#include <cstring>
#include <stdio.h>

using namespace std;



int main()
{
    freopen("C-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,a,b,ans,n,tmp,index;
    int cmp[10];
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        ans=0;
        scanf("%d%d",&a,&b);
        for(int m=b;m>a;m--)
        {
            int dig=1;
            int k=0;
            tmp=m;
            while(tmp>=10)
            {
                dig*=10;
                tmp=tmp/10;
                k++;
            }
            cmp[0]=m;
            for(int j=1;j<=k;j++)
            {
                int mod=cmp[j-1]%10;
                //cout<<"mod:"<< mod<<endl;
                cmp[j]=mod*dig+cmp[j-1]/10;
                if(mod>0&&cmp[j]<m&&cmp[j]>=a)
                {
                    for(index=1;index<j;index++)
                    {
                        if(cmp[j]==cmp[index])break;
                    }
                    if(index==j)
                    {
                        //cout << m << ' '<< cmp[j] << endl;
                        ans++;
                    }
                    //ans++;
                }
            }

        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
