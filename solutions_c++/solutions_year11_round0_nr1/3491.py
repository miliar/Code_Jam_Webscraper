#include<iostream>
#include<stdio.h>
int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
    {
            int n, q;
            char color;
            int j = 0, k = 0; 
            int o[100], b[100]; 
            int seq[100];
            scanf("%d", &n);
            for(q = 0; q < n; q++)
            {
                      scanf(" %c ", &color);
                      if(color == 'O')
                      {
                               seq[q] = 0;
                               scanf("%d", &o[j]);
                               j++;
                      }
                      else
                      {
                               seq[q] = 1;
                               scanf("%d", &b[k]);
                               k++;         
                      }
            }
            /*for(int u = 0; u < j; u++)
                    printf("%d||", o[u]);
            for(int v = 0; v < k; v++)
                    printf("%d..", b[v]);
            */
            int time = 0;
            j = 0;
            k = 0;
            int timeo = 0, timeb = 0;
            int poso = 1, posb = 1;
            for(q = 0; q < n; q++)
            {
                  if(seq[q] == 0)
                  {         
                            if(o[j] >= poso)
                            {
                                    if(time - timeo > o[j] - poso)
                                            time += 1;
                                    else
                                            time += (o[j] - poso - (time - timeo)) + 1;
                            }
                            else
                            {
                                    if(time - timeo > poso - o[j])
                                            time += 1;
                                    else
                                            time += (poso - o[j] - (time - timeo)) + 1;
                            }
                            poso = o[j];
                            timeo = time;
                            j++;
                  }     
                  else
                  {
                            if(b[k] >= posb)
                            {
                                    if(time - timeb > b[k] - posb)
                                            time += 1;
                                    else
                                            time += (b[k] - posb - (time - timeb)) + 1;
                            }
                            else
                            {
                                    if(time - timeb > posb - b[k])
                                            time += 1;
                                    else
                                            time += (posb - b[k] - (time - timeb)) + 1;
                            }
                            posb = b[k];
                            timeb = time;
                            k++;
                  }
            }
            printf("Case #%d: %d%s", i+1, time, i == t ? "" : "\n"); 
            fflush(stdin);
    }
    //system("pause");
    return 0;    
}
