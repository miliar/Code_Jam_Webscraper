#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef pair<LL, LL> PL;

int N, M;
vector<PL> boxes;
vector<PL> toys;

LL DP[128][128];
LL cacheBox[128][128];
LL cacheToy[128][128];

LL interBox(int a, int b, int type)
{
   LL sub = a > 0 ? cacheBox[a - 1][type] : 0;
   return cacheBox[b][type] - sub;
}

LL interToy(int a, int b, int type)
{
   LL sub = a > 0 ? cacheToy[b - 1][type] : 0;                
   return cacheToy[b][type] - cacheToy[a - 1][type];                
}

LL rec(int box, int toy)
{
    if (box >= N || toy >= M) return 0;       
    if (DP[box][toy] != -1) return DP[box][toy];
    
    LL result = 0;
    if (boxes[box].second == toys[toy].second)
    {
        LL packed = min(boxes[box].first, toys[toy].first);   
        result = max(result, packed + rec(box + 1, toy + 1)); //???
                       
        if (boxes[box].first == toys[toy].first)
           result = max(result, packed + rec(box + 1, toy + 1));
        else
        {
            int type = boxes[box].second;
            for (int i = box + 1; i <= N; i++)
            {
                LL interBoxes = interBox(box, i - 1, type);
                for (int j = toy + 1; j <= M; j++)
                {
                    LL interToys = interToy(toy, j - 1, type);
                    
                    LL have = min(interBoxes, interToys);
                    result = max(result, have + rec(i, j)); 
                } 
            }  
        }   
    }
    else
    {
        result = max(result, rec(box + 1, toy));
        result = max(result, rec(box, toy + 1));
    }
    
    return DP[box][toy] = result;        
}

LL solve()
{
    memset(DP, -1, sizeof(DP));      
    memset(cacheBox, 0, sizeof(cacheBox));
    memset(cacheToy, 0, sizeof(cacheToy));
    
    for (int type = 1; type <= 100; type++)
    {
        LL sum = 0; 
        for (int i = 0; i < boxes.size(); i++)
        {            
            if (boxes[i].second == type) sum += boxes[i].first;
            cacheBox[i][type] = sum;
        }
    }
    
    for (int type = 1; type <= 100; type++)
    {
        LL sum = 0; 
        for (int i = 0; i < toys.size(); i++)
        {
            if (toys[i].second == type) sum += toys[i].first;            
            cacheToy[i][type] = sum;
        }
    }
    
    return rec(0, 0);      
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> M;
        boxes.clear();
        toys.clear();
        
        for (int i = 0; i < N; i++)
        {
            LL num, type;
            cin >> num >> type;
            boxes.push_back(make_pair(num, type));
        }
        
        for (int i = 0; i < M; i++)
        {
            LL num, type;
            cin >> num >> type;
            toys.push_back(make_pair(num, type));
        }
        
        cout << "Case #" << t << ": " << solve() << endl;
    }
    
    return 0;
}
