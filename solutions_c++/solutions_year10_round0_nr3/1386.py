#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);

    int t,tt=1;
    cin>>t;
    while(t-- > 0)
    {
        int R,k,i,temp=0,start=0,end,N;
        vector <int> g;
        cin>>R>>k>>N;
        long long sum=0,temp_sum=0;
        for(i=0;i<N;i++)
        {
            cin>>temp;
            g.push_back(temp);
        }
        start=0;
        end=g.size();
        i=0;
        while(R--)
        {
                i=start;
                while((temp_sum+g[i])<=k )
                {
                    temp_sum+=g[i];
                    i++;
                    if(i==g.size())
                    i=0;
                    if(i==start)
                    break;
                }
                start=i;
                sum+=temp_sum;
                temp_sum=0;
                //R--;
        }
        cout<<"Case #"<<tt++<<": "<<sum<<endl;
    }
    return 0;
}
                
                     
