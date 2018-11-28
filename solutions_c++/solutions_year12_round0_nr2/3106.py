#include<iostream>
#include<cstdio>
#include<fstream>
#include<cmath>
#include<algorithm>

inline int min (int a, int b)
{
    if (a>b) return b;
    return a;
}

float array[110];int v[110]; int k[110],o[110];

using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int a,b,c,d,i,j,l,t,n,s,p,ans;
    fin>>t;
    for(i=1;i<=t;i++)
    {
        ans=0;
        fin>>n>>s>>p;
        cout<<n<<" ";
        for(j=0;j<n;j++)
        fin>>array[j];
        sort(array,array+n);
        for(j=0;j<n;j++)
        {
            v[j]=ceil(array[j]/3);
            if((int)array[j]==0)k[j]=0;
            else if((int)array[j]%3==2)
            {
                k[j]=(int) (array[j]/3+2);
            }
            else if ((int)array[j]%3==0)
            {
                k[j]=(int)(array[j]/3+1);
            }
            else k[j]=v[j];
        }
/*	for(j=0;j<n;j++)
		cout<<v[j]<<" ";cout<<"\n";
	for(j=0;j<n;j++)
		cout<<k[j]<<" ";cout<<"\n";*/
        if(s!=0)
        for(j=0;j<n;j++)
        {
            if(k[j]>=p)
            {
                ans++;
                k[j]=-1;
                v[j]=-1;
                s--;
            }
            if(s==0)break;
        }
        for(j=0;j<n;j++)
        {
            if(v[j]>=p)
                ans++;
        }
        fout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    return 0;
}
