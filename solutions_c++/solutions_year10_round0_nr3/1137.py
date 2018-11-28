#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

#define SIZE 2000

int main()
{
    freopen("C2.in","r",stdin);
    freopen("C2.out","w",stdout);

    long long  i,j,k,l,n,test,Case=1,sum,total,r,m,cnt,c;
    map<vector<long long >,long long>mp;


    //scanf("%d",&test);
    cin>>test;
    while(test--)
    {
        //scanf("%d %d %d",&r,&c,&n);
        cin>>r>>c>>n;
        vector<long long>a(n),b(n);
        vector<long long>store;

        for(i=0;i<n;i++)
            //scanf("%d",&a[i]);
            cin>>a[i];

        mp.clear();

        total=0;
        for(i=0;i<r;i++)
        {
            if(mp[a]==0)
            {
                mp[a]=i+1;
                sum=0;
                for(j=0;j<n;j++)
                    if((sum+a[j])<=c)
                    {
                        sum+=a[j];
                    }
                    else break;
                store.push_back(sum);
                for(k=j,l=0;k<n;k++,l++)
                    b[l]=a[k];
                for(k=0;k<j;k++,l++)
                    b[l]=a[k];
                a=b;
                total+=sum;
            }
            else break;
        }
        k=i-1;
        j=mp[a]-1;
        r=r-i;
        m=k-j+1;

        //cout<<j<<" "<<k<<" "<<r<<endl;

        sum=0;
        for(i=j;i<=k;i++)
            sum+=store[i];
        total+=sum*(r/m);
        for(i=j,l=0;l<(r%m);l++,i++)
            total+=store[i];
        cout<<"Case #"<<Case++<<": "<<total<<endl;
    }

    return 0;
}
