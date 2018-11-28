#include <cstdio>
#include <algorithm>
using namespace std;


struct Node
{
    int times;
    bool isEnd;
    int from;
    
    void init(int t, bool i, int f)
    {
        times = t;
        isEnd = i;
        from = f;
    }
    bool operator<(const Node& other)const
    {
        if(times != other.times)
            return times < other.times;
        else
            return isEnd;     
    }
};



int main()
{
    Node nodes[1024];
    
    int N;
    scanf("%d", &N);
    for(int times = 0; times < N; times++)
    {
        int T, Ns[2];
        scanf("%d%d%d", &T, Ns, Ns + 1);
        
        int total = 0;
        for(int i = 0; i < 2; i++)
            for(int j = 0; j < Ns[i]; j++)
                for(int k = 0; k < 2; k++)
                {

                    int H, M;
                    scanf("%d:%d", &H, &M);
                    nodes[total++].init(H * 60 + M + k * T, k, i);
                }
        
        sort(nodes, nodes + total);
        int remain[2] = {0};
        int ans[2] = {0};
        for(int i = 0; i < total; i++)
            if(nodes[i].isEnd)
                remain[!nodes[i].from]++;
            else if(remain[nodes[i].from])
                remain[nodes[i].from]--;
            else
                ans[nodes[i].from]++;
                
        printf("Case #%d: %d %d\n", times + 1, ans[0], ans[1]);
    }
    return 0;   
}
