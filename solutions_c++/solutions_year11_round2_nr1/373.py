#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

char inp[100][100];
int n;

struct s{
    int w,p;
    double wp[100],owp,oowp,rpi;
}a[100];

int main()
{
    int i,j,k,t,T;
    string str;
    double q,r;

    freopen("a.in","r",stdin);
    freopen("aout.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);

        for(i=0;i<n;i++)
        {
            cin>>str;

            for(j=0;j<n;j++)
            {
                inp[i][j]=str[j];
            }
        }

        for(i=0;i<n;i++)
        {

            a[i].w=a[i].p=0;

            for(j=0;j<n;j++)
            {
                if(inp[i][j]!='.')
                {
                    a[i].p++;

                    if(inp[i][j]=='1') a[i].w++;
                }
            }

            a[i].wp[i]=a[i].w/(double)a[i].p;
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(inp[j][i]=='1')
                {
                    if(a[j].p!=1) a[i].wp[j]=(a[j].w-1)/((double)(a[j].p-1));
                    else a[i].wp[j]=0.0;
                }

                else if(inp[j][i]=='0')
                {
                    if(a[j].p!=-1) a[i].wp[j]=(a[j].w)/((double)(a[j].p-1));
                    else a[i].wp[j]=0.0;
                }

            }
        }

        for(i=0;i<n;i++)
        {
            q=r=0.0;

            for(j=0;j<n;j++)
            {
                if(inp[i][j]!='.')
                {
                    q+=a[i].wp[j];
                    r+=1.0;
                }
            }

            a[i].owp=q/r;
        }

        for(i=0;i<n;i++)
        {
            q=r=0.0;

            for(j=0;j<n;j++)
            {
                if(inp[i][j]!='.')
                {
                    q+=a[j].owp;
                    r+=1.0;
                }
            }

            a[i].oowp=q/r;
        }

        for(i=0;i<n;i++)
        {
            a[i].rpi=(0.25 * a[i].wp[i]) + (0.50 * a[i].owp) + (0.25 * a[i].oowp);
        }

        printf("Case #%d:\n",t);

        /*for(i=0;i<n;i++)
        {
            cout<<a[i].wp[i]<<endl;

            for(j=0;j<n;j++)
            {
                if(inp[i][j]!='.')
                {
                    cout<<"with "<<j<<" "<<a[i].wp[j]<<endl;
                }
            }

            cout<<a[i].owp<<" "<<a[i].oowp<<endl;

            cout<<a[i].rpi<<endl;
        }*/

        for(i=0;i<n;i++) printf("%.10lf\n",a[i].rpi);
    }

    return 0;
}







