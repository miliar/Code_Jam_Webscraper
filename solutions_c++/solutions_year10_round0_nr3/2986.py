#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAXSIZE_group = 1005;
struct
{
    int index;
    int size;
}next[MAXSIZE_group]; 
//next[i]表示的含义是若以第i组为队首,K值已定，那么下一轮队首是那一组?这一轮上了多少乘客 

void Init(int K, int N, int *g);

int main()
{
    int i, j;
    int T, casen = 1;

    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    
    scanf("%d", &T);
    while (T--)
    {    
        int R, K, N;
        int g[MAXSIZE_group]= {0};
        unsigned long long total, result;
        
        scanf("%d%d%d", &R, &K, &N);
        for(i=total=0; i<N; i++)
        {
            scanf("%d", &g[i]);
            total += g[i]; //最大可能为10^10,超过int型,所以用long long 
        }
        
        if (total <= K) //特殊情况,所有group都可以上车
          result = total*R;
        else
        {
            Init(K, N, g); //预处理，计算出next数组
            
            for (i=0,result=j=0; i<R; i++,j=next[j].index)
                result += next[j].size;
        }
        
        printf("Case #%d: %llu\n", casen++, result);
    }
    
   // system("pause");
    return 0;
}

void Init(int K, int N, int *g)
{
     int i, j;
     int total;
     
     memset(next, 0, sizeof(next));
     
     for (total=i=0; total+g[i]<=K;  total+=g[i],i=(i+1)%N) ;     
     next[0].index = i; next[0].size = total;
         
     for (i=1; i<N; i++) //O(N^2)
     {
         //第i组在上一组的基础上，尝试加下去. 
         for (total=next[i-1].size-g[i-1],j=next[i-1].index; total+g[j]<=K; j = (j+1)%N) 
             total += g[j]; 
             
         next[i].index = j;   
         next[i].size = total;
     }
}
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
