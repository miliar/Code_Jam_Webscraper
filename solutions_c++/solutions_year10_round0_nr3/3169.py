//Bismillahir Rahmanir Rahim
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.txt","w",stdout);
    int R,kas,K,P,i,cas;
    cin>>kas;
    for(cas=1;cas<=kas;cas++){

        queue<int>Q;
        vector<int>vec;
        cin>>R>>K>>P;
        for(i=0;i<P;i++)
        {
            int t;
            cin>>t;
            Q.push(t);
        }
        printf("Case #%d: ",cas);
        long long res=0;
        for(i=0;i<R;i++){
            int t=K;
            while(t>=Q.front()&&Q.size()>0)
            {
                int p=Q.front();
                Q.pop();
                vec.push_back(p);
                t-=p;
                res+=p;
            }
            int j;
            for(j=0;j<vec.size();j++)
            Q.push(vec[j]);
            vec.clear();
        }
        cout<<res<<endl;
    }
    return 0;
}
