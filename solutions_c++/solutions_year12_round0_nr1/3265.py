#include <cstdio>
#include <cstring>

int main()
{
    int n;
    char line[101];
    
    char* source = "abcdefghijklmnopqrstuvwxyz";
    char* target = "yhesocvxduiglbkrztnwjpfmaq";
    
    scanf("%d\n", &n);
    
    for (int i = 0; i < n; i++)
    {
        printf("Case #%d: ", i + 1);
        gets(line);
        
        for (int j = 0; j < strlen(line); j++)
        {
            if (line[j] == ' ')
            {
                printf(" ");
            }
            else
            {
                printf("%c", target[line[j] - 97]);
            }
        }
        
        printf("\n");
    }
    
    return 0;
}
