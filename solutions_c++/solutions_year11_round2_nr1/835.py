#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,inp,cs,n;
    cin>>cases;
    string temp;
    int arr[110][110],i,j;
    double wp[110],owt[110][110], owp[110], oowp[110];
    for(cs=1;cs<=cases;cs++)
    {
        memset(arr,-1,sizeof(arr));
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>temp;
            for(j=0;j<temp.length();j++)
            {
                if(temp[j]!='.')
                    arr[i][j]=temp[j]-'0';
            }

        }
        for(i=0;i<n;i++)
        {
            int sum=0, count=0;
            for(j=0;j<n;j++)
            {
                if(arr[i][j]!=-1)
                    sum+=arr[i][j], count++;
            }
            wp[i]=(double)sum/count;
            //cout<<wp[i]<<endl;
            for(j=0;j<n;j++)
            {
                //cout<<j<<"how ";
                if(i==j)
                {
                    owt[i][j]=-1;
                    continue;
                }
                if(arr[i][j]==-1)
                    owt[i][j]=-1;
                else if(arr[i][j]==1)
                {
                    if(count-1>0)
                        owt[i][j]=(double)(sum-1)/(count-1);
                    else owt[i][j]=0;
                }

                else
                {
                    if(count-1>0)
                        owt[i][j]=(double)(sum)/(count-1);
                    else owt[i][j]=0;
                }
                //cout<<owt[i][j]<<" is it";
            }
            //cout<<endl;
        }
        for(i=0;i<n;i++)
        {
            double t=0;
            int count=0;
            for(j=0;j<n;j++)
            {
                if(i==j)
                    continue;
                if(owt[j][i]!=-1)
                t+=owt[j][i], count++;
            }
            owp[i]=t/count;
            //cout<<owp[i]<<" ";
        }
        //cout<<endl;
        for(i=0;i<n;i++)
        {
            double t=0;
            int count=0;
            for(j=0;j<n;j++)
            {
                if(i==j)
                    continue;
                if(arr[i][j]!=-1)
                     count++,t+=owp[j];
            }
            oowp[i]=t/count;
            //cout<<oowp[i]<<" ";
        }
        //cout<<endl;
        cout<<"Case #"<<cs<<":\n";
        for(i=0;i<n;i++)
        {
            double ans=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
            printf("%0.8lf\n",ans);
        }
    }
    return 0;
}
