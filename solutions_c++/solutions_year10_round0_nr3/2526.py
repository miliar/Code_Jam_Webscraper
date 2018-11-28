#include<iostream>
#include<vector>

using std::cout;
using std::cin;
using std::vector;

int main()
{
    int R, k, N;
    int T, casenum=1;
    int Money;
    vector<int> groups;
    vector<int>::iterator VIter,VBegin, VEnd;
    cin>>T;
    while(casenum<=T)
    {
        cin>>R>>k>>N;
        Money=0;
        int sum=0;
        for(int i=0;i<N;i++)
        {
            int temp;
            cin>>temp;
            groups.push_back(temp);
            sum+=temp;
        }
        if(sum<=k)
            Money = sum*R;

        if(!Money)
        {
            VBegin=groups.begin();
            VEnd=groups.end();
            VIter=VBegin;
            while(R--)
            {
                int total=0;
                while((total+*VIter)<=k)
                {
                    total+=*VIter;
                    VIter++;

                    if(VIter==VEnd)
                        VIter=VBegin;
                }
                if(VIter==VEnd)
                    VIter=VBegin;
                Money+=total;
            }
        }
        printf("Case #%d: %d\n",casenum,Money);
        casenum++;
        groups.clear();
    }
}
