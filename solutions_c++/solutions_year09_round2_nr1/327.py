#include <stdio.h>
#include <string.h>

struct featrue
{
    double weight;
    char name[20];
    featrue* ok;
    featrue* no;
};

char InputData[200][20];
int N;
int L, A, n;

void InputDataFun(featrue* in)
{
     char t;
     double ind;
     bool isNo = true;
     int idx;
     char name[20] = {0,};
     in->ok = NULL;
     in->no = NULL;
     while(scanf("%c", &t))
     {
         if(t == '(')
         {
              scanf("%lf", &ind);
              in->weight = ind;
              break;
         }
     }
     idx = 0;
     while(scanf("%c", &t))
     {
         if(t == ')')
         {
              break;
         }
         if(t >= 'a' && t <= 'z')
         {
              name[idx] = t;
              idx++;
         }
         if(isNo && (t == '\n' || t == '('))
         {
              isNo = false;
              name[idx] = 0;
              featrue* newOk = new featrue;
              featrue* newNo = new featrue;
              in->ok = newOk;
              in->no = newNo;
              InputDataFun(newOk);
              InputDataFun(newNo);              
         }
     }
     strcpy(in->name, name);
}
          
          
int main()
{
    char temps[30];
    double result = 0;
    int count = 1;
    bool find;
    featrue start;
    featrue* now;
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &L);
        InputDataFun(&start); 
        
        scanf("%d", &A);
        printf("Case #%d:\n", count);
        count++;
        for(int j = 0; j < A; j++)
        {
            scanf("%s", temps);
            scanf("%d", &n);
            for(int k = 0; k < n; k++)
            {
                scanf("%s", InputData[k]);                    
            }
            now = &start;
            result = 1;
            while(now)
            {
                result *= now->weight;
                find = false;
                for(int k = 0; k < n; k++)
                {
                    if(strcmp(now->name, InputData[k])==0)
                    {
                        find = true;
                        break;
                    }
                }
                if(find) now = now->ok;
                else     now = now->no;
            }
            printf("%.7lf\n", result);
        }
    }    
    
    return 0;
}
