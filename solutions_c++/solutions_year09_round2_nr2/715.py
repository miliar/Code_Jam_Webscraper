#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    int i,j,T;
    vector<int> c,A;
    string N;
    cin>>T;
    for(i=0;i<T;++i)
    {
        cin>>N;
        printf("Case #%d: ",i+1);
        c.clear();
        for(j=0;j<N.size();++j)c.push_back(N[j]-'0');
        int fdif,cr;
        vector<int> v,ans;
        for(fdif=0;fdif<c.size()-1;++fdif)
        {
            cr=10;v=c;
            int pos;
            for(j=fdif+1;j<c.size();++j)
                if(v[j]>c[fdif]&&v[j]<cr)
                {
                    cr=v[j];
                    pos=j;
                }
            if(cr==10)continue;
            swap(v[pos],v[fdif]);
            sort(v.begin()+fdif+1,v.end());
            if(v>c)
            {
                if(ans.empty()||v<ans)ans=v;
            }
        }
        if(!ans.empty())
        {
            for(j=0;j<ans.size();++j)printf("%d",ans[j]);
            printf("\n");
        }
        else
        {
            sort(c.begin(),c.end());
            for(j=0;j<c.size();++j)
                if(c[j]!=0)
                {
                    swap(c[j],c[0]);
                    break;
                }
            printf("%d0",c[0]);
            for(j=1;j<c.size();++j)printf("%d",c[j]);printf("\n");
        }
    }
    return 0;
}
