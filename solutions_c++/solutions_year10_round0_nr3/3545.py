#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

long int found(deque<long int> s,deque< deque<long int> > save)
{
    long int i,j;
    bool fl;
    for (i=0; i<save.size(); i++)
    {
        fl=1;
        for (j=0; j<save[i].size(); j++) if (save[i][j]!=s[j]) fl=0;
        if (fl) return i;
    }
    return -1;
}

deque<long int> change(deque<long int> s,long int k)
{
    long int c,sum=0,cnt=0;
    while (1)
    {
        c=s.front();
        sum+=c;
        if (sum>k)
        {
            sum-=c;
            break;
        }
        cnt++;
        if (cnt==s.size()) break;
        s.pop_front();
        s.push_back(c);
    }
    return s;
}

long int getcost(deque<long int> s,long int k)
{
    long int i=0,sum=0;
    for (i=0; sum+s[i]<=k && i<s.size(); i++) sum+=s[i];
    return sum;
}

int main()
{
    long int r,k,n,i,a,sum,c,ans,rest,fnd,j,t,cas=1;
    freopen("inc1","r",stdin);
    freopen("outc1","w",stdout);
    scanf("%ld",&t);
    while (t--)
    {
        deque<long int> s;
        deque< deque<long int> > save;
        deque<long int> sums;
        scanf("%ld%ld%ld",&r,&k,&n);
        for (i=0; i<n; i++)
        {
            scanf("%ld",&a);
            s.push_back(a);
        }
        ans=0;
        save.push_back(s);
        sums.push_back(getcost(s,k));
        ans=sums[0];
        for (i=1; i<r; i++)
        {
            s=change(s,k);
            sum=getcost(s,k);

            if (found(s,save)!=-1) break;
            else
            {
                save.push_back(s);
                sums.push_back(sum);
                ans+=sum;
            }
        }
        if (i<r)
        {
            rest=r-save.size();
            //printf("%d\n",rest);
            fnd=found(s,save);
            for (i=fnd; i<sums.size(); i++)
            {
                ans+=sums[i]*(rest/(save.size()-fnd));
                //prlong intf("1adding %ld\n",sums[i]*(rest/(save.size()-fnd)));
            }

            for (i=fnd,j=0; j<rest%(save.size()-fnd); j++,i++)
            {
                ans+=sums[i];
                //prlong intf("2adding %ld\n",sums[i]);
            }
        }
        printf("Case #%ld: %ld\n",cas,ans);
        cas++;
    }

	return 0;
}
