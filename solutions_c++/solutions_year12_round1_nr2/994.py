#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int A[1002],B[1002];
        int starsob[1002];
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d%d",&A[i],&B[i]);
        }
        int answer=10000000;
        for(int mask=0;mask<(1<<N);mask++)
        {
            vector<pair<int,int> > down,up;
            
            for(int i=0;i<N;i++)
            {
                starsob[i]=0;
                if((mask>>i)&1)
                {
                    down.push_back(make_pair(A[i],i));
                }
                up.push_back(make_pair(B[i],i));
            }
            sort(down.begin(),down.end());
            sort(up.begin(),up.end());
            int posup=0;
            int posdown=0;
            int numstars=0;
            bool activity=true;
            while(activity && posup<up.size())
            {
                activity=false;
                if(posdown<down.size() && numstars>=down[posdown].first)
                {
                    numstars+=max(0,1-starsob[down[posdown].second]);
                    starsob[down[posdown].second]=max(1, starsob[down[posdown].second]);     
                    activity=true;
                    posdown++;
                }
                if(posup<up.size() && numstars>=up[posup].first)
                {
                    numstars+=2-starsob[up[posup].second];
                    starsob[up[posup].second]=2;             
                    activity=true;
                    posup++;
                }
            }
            
            if(posup>=up.size())
            {
                answer=min(answer, (int)down.size()+(int)up.size());
            }
          
            
        }
        if(answer==10000000)
            printf("Case #%d: Too Bad\n",t);
        else
            printf("Case #%d: %d\n",t,answer);
        
    
    
    }
}