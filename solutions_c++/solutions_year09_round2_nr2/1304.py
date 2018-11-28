#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <cstring>

using namespace std;

char buffer[1000];
char buffer2[1000];

int len1;

int b1_start = 0;
bool count(int new_digit)
{
    int len2 = sprintf(buffer2, "%d", new_digit);
    sort(buffer2, buffer2+len2);
    
    int start = 0;
    
    while(buffer2[start] == '0')
        ++start;
    
//     printf("%s %s\n", buffer+b1_start, buffer2+start);
    return strcmp(buffer2+start, buffer+b1_start) == 0;
}

int main()
{
    int T;
    
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        b1_start = 0;
        
        scanf("%s", buffer);
        len1 = strlen(buffer);
        
        int start_num;
        sscanf(buffer, "%d", &start_num);
        
        sort(buffer, buffer+len1);
        
        while(buffer[b1_start] == '0')
        {
//             printf("%s\n", buffer);
            b1_start++;
        }
        
        while(!count(++start_num))
        {
//             printf("%s %d\n", start_num);
        }
        
        printf("Case #%d: %d\n", t, start_num);
        
    }
}