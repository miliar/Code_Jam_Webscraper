#include <stdio.h>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int V = 1100;
struct circle
{
    int r;
    int id;
    int x, y;
    bool operator < (const circle &a) {
        return r > a.r;
    }
}c[V];
int n, W, L;

int main()
{
    int test;
    scanf("%d",&test);
    for (int cas=1;cas<=test;cas++)
    {
        scanf("%d%d%d",&n,&W,&L);
        for (int i=0;i<n;i++) 
        {
            scanf("%d",&c[i].r);
            c[i].id = i;
        }
        bool isSwap = false;
        if (W < L) { swap(W, L); isSwap = true; }
        //sort(c, c+n);
        
        vector<int> vec, vec1;
        
        vec1.push_back(0); c[0].x = 0; c[0].y = 0;
        int cx = c[0].r;
        int j = 0;
        //printf("cxxx = %d %d\n",c[0].r, c[1].r);
        for (int i=1;i<n;i++)
        {
            cx = cx + c[i].r;
            //printf("cx = %d %d\n",cx, W);
            if (cx > W)
            {
                j = 0;
                vec = vec1;
                vec1.clear();
                cx = 0;
                c[i].x = 0;
                c[i].y = c[vec[0]].y + c[vec[0]].r + c[i].r;
                cx += c[i].x;
            }
            while (j < vec.size() && cx > c[vec[j]].x + c[vec[j]].r) j++;
            //printf("c[%d] = cx = %d %d %d %d\n",i, cx, c[i].r, c[i].x, c[i].y);
            if (vec.empty()) {
                c[i].x = cx;
                c[i].y = 0;
            }
            else {
                c[i].x = cx;
                c[i].y = c[vec[j]].y + c[vec[j]].r + c[i].r;
            }
            cx += c[i].r;
            
            
            vec1.push_back(i);
        }
        
        printf("Case #%d:",cas);
        for (int i=0;i<n;i++)
        {
            if (isSwap) swap(c[i].x, c[i].y);
            printf(" %d %d",c[i].x, c[i].y);
        }
        printf("\n");
        
        if (isSwap) swap(W, L);
        
        for (int i=0;i<n;i++)
        {
            if (!(c[i].x >= 0 && c[i].x <= W && c[i].y >= 0 && c[i].y <= L)) {
                printf("error!\n");
                break;
            }
            
            for (int j=0;j<i;j++)
            if (abs(c[i].x - c[j].x) + abs(c[i].y - c[j].y) < c[i].r + c[j].r)
            {
                printf("error! %d %d %d %d\n",i, j, abs(c[i].x - c[j].x) + abs(c[i].y - c[j].y), c[i].r+c[j].r);
                break;
            }
        }
       
    }
}

