#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

    int t, n, s, p, ni, ans;
    vector<int> vi;

    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n>>s>>p;
        vi.clear();
        while(n--)
        {
            cin>>ni;
            vi.push_back(ni);
        }

        int p3=p*3;

        ans=0;
        for(vector<int>::iterator it=vi.begin();it!=vi.end();it++)
        {
            if(p3 - *it <= 0)ans++;
            else if(p3 - *it > 0 && p3 - *it <= 2 && p-1>=0)ans++;
            else if(p3 - *it > 2 && p3 - *it <= 4 && p-2>=0 && s>0){ans++; s--;}
        }

        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }

    return 0;
}
