#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{   
    freopen("out.txt", "w", stdout); 
    int T;
    cin>>T;
    
    for(int t = 1; T--; ++t)
    {
        int ans = 0, rpos[2] = {1, 1}, N, pp[2] = {0,0};
        vector <int> pts[2], rn;
        cin>>N;
        
        for(int i = 0; i < N; i++)
        {
            int temp;
            char ch;
            cin>>ch>>temp;
            pts[ch=='O'].push_back(temp);
            rn.push_back(ch=='O');
        }
        
        for(int i = 0; i < N; i++)
        {
            int now = rn[i], cp = !now;
            while(rpos[now] != pts[now][ pp[now] ])
            {
                ++ans;
                if(pts[now][ pp[now] ] < rpos[now])
                    --rpos[now];
                else
                    ++rpos[now];
                //other robot
                if(pp[cp] < pts[cp].size() && pts[cp][ pp[cp] ] < rpos[cp])
                    --rpos[cp];
                else if(pp[cp] < pts[cp].size() && pts[cp][ pp[cp] ] > rpos[cp])
                    ++rpos[cp];          
            }
            
            //push
            ++ans;
            ++pp[now];
            if(pp[cp] < pts[cp].size() && pts[cp][ pp[cp] ] < rpos[cp])
                --rpos[cp];
            else if(pp[cp] < pts[cp].size() && pts[cp][ pp[cp] ] > rpos[cp])
                ++rpos[cp];
        }
                
        printf("Case #%d: %d\n", t, ans);
    }
    
    return 0;
}
