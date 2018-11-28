#include<iostream>
using namespace std;

char ans[105];
char arr[105];
char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    int i, j, t, k;
    int cse=0;
    
    scanf("%d", &t);
    getchar();
    while(t--)
    {
       for(i=0;i<105;i++)
        {
           scanf("%c", &arr[i]);
           if(arr[i] == '\n')
            {
             arr[i] = ' ';
             break;
            }
        }
        
        
        for(j=0;j<i;j++)
        {
           if(arr[j] != ' ')
           {
             k = arr[j];
             k = k - 97;
             ans[j] = map[k];
           }
           else if(arr[j] == ' ')
           ans[j] = ' ';
        }
        
        cse++;
        printf("Case #%d: ", cse);
        for(j=0;j<i;j++)
         printf("%c", ans[j]);
    printf("\n");
     }
}
           
