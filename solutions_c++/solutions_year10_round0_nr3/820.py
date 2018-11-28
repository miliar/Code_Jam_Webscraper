#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#include<vector>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<stack>

using namespace std;

typedef pair<__int64,int> pii;

#define mp make_pair

bool seen[1005];

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        __int64 rounds, maxPeople, groups;
        scanf("%I64d%I64d%I64d",&rounds,&maxPeople,&groups);
        
        queue<pii> que;
        
        for(int i = 0; i < groups; ++i)
        {
            __int64 groupSize;
            scanf("%I64d",&groupSize);   
            que.push(mp(groupSize,i));           
        }    
        
        memset(seen,0,sizeof(seen));
                
        __int64 cycleStartsFrom = 0;
        
        vector<__int64> startingPeople, income;
        
        while(true)
        {
            __int64 total = 0, cntGroups = 0;
            __int64 next = que.front().second;
            
            if(seen[next]) 
            {
                cycleStartsFrom = next;
                break;
            }
            
            seen[next] = true;
            startingPeople.push_back(next);
            
            while(cntGroups < groups)
            {
                total += que.front().first;
                
                if(total > maxPeople)
                {
                    income.push_back(total - que.front().first);                    
                    break;
                }
                
                que.push(que.front());
                ++cntGroups;
                
                que.pop();
            }
            
            if(cntGroups == groups) 
            {
                income.push_back(total);
                break;
            }
            
            if(income.size() == rounds) break;
        }
            
        __int64 headIncome = 0;
        int indx = 0;
        
        while(indx < income.size() && startingPeople[indx] != cycleStartsFrom)
        {
            rounds--;
            headIncome += income[indx];   
            ++indx;
        }
        
        __int64 cycleLen = income.size() - indx;
        
        __int64 incomeInCycle = 0, tailIncome = 0;
        
        for(int i = indx; i < income.size(); ++i)
        {
            incomeInCycle += income[i];   
        }
        
        __int64 totalCycles = rounds / cycleLen;
        __int64 totalIncomeInCycle = incomeInCycle * totalCycles;
        __int64 tailLen = rounds % cycleLen;
        
        for(int i = indx; i < indx+tailLen; ++i)
        {
            tailIncome += income[i];
        }
                
        __int64 totalIncome = headIncome + totalIncomeInCycle + tailIncome;
        
        printf("Case #%d: %I64d\n",t,totalIncome);
    }
    
    return 0;
}
