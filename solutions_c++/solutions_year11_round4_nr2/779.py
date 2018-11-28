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
    //freopen("inp.txt","r",stdin);
    freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cs,k,i,j,a,b,arr[11][11],r,c,d,ans;
    cin>>cases;
    double sx, sy, sm, xx, yy;
    string str;
    for(cs=1;cs<=cases;cs++)
    {
        cin>>r>>c>>d;
        for(i=0;i<r;i++)
        {
            cin>>str;
            for(j=0;j<c;j++)
                arr[i][j]=(str[j]-'0');
        }



        k=min(r,c);
        //cout<<"k= "<<k<<endl;
        ans=-1;
        for(k=min(r,c);k>=3 && ans==-1;k--)
        {
            //cout<<k<<endl;
            for(i=0;i<=r-k && ans==-1;i++)
                for(j=0;j<=c-k && ans==-1;j++)
                {
                    sx=0, sy=0, sm=0;
                    for(a=0;a<k;a++)
                    {
                        for(b=0;b<k;b++)
                        {
                            if(a==0 || a==k-1)
                            {
                                if(b==0 || b==k-1)
                                    continue;
                            }
                            sx+=(double)(arr[a+i][b+j]+d)*(b+0.5);
                            sm+=(arr[a+i][b+j]+d);
                            sy+=(double)(arr[a+i][b+j]+d)*(k-1-a+0.5);
                        }
                    }

                    //cout<<sx<<" "<<sy<<" "<<sm<<endl;

                    xx=(sx)/(double)(sm);
                    yy=(sy)/(double)(sm);
                    if(xx==k/2.0 && yy==xx)
                    {
                        ans=k;
                        break;
                    }
                }
        }
        cout<<"Case #"<<cs<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;

    }
    return 0;
}
