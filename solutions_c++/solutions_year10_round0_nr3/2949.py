#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
    FILE *fp, *fp_write;
    fp = fopen("data.in","r");
    fp_write = fopen("data.out","w");
    int T;
    fscanf(fp, "%d", &T);
    
   
    for(int i = 1; i <= T; ++i)
    {
        queue<int> q;
        int r, k, n;
        fscanf(fp, "%d %d %d", &r, &k, &n);
        //poopulate the queue
        while(n-- > 0)
        {
           int mem;
           fscanf(fp, "%d", &mem);
           q.push(mem);
        } 
        //printf("%d\n", q.size());
        int earn = 0;
        while(r-- > 0)
        {
             int fill = 0;
             int c =0;
             while(1)
             {
                 int f = q.front();
                 int size = q.size();
                 if( (fill + f) <= k && c < size)
                 {
                     fill += f;
                     q.pop();
                     q.push(f);
                     c++;
  //                   printf("%d\t", f);
                 }
                 else
                   break;
             }
//             printf("earn round : %d\n", fill);
             earn += fill;
        }
        fprintf(fp_write, "Case #%d: %d\n", i,earn);
    }
    fclose(fp_write);
    fclose(fp);
    return 0;
}
