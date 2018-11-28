#include <iostream>
#include <stdio.h>

char replace[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main ()
{
    FILE *fp, *ft;
    int t, i, c=1;
    char s[200], x;
    
    fp = freopen("input.txt", "r", stdin);
    ft = fopen("output.txt", "w");
    
    fscanf (fp, "%d", &t);
    fscanf (fp, "%c", &x);
    
    while (c <= t)
    {
          std::cin.getline(s, 200);
          
          i = 0;
          
          fprintf (ft, "Case #%d: ", c);
          c++;
          
          while (s[i])
          {
                if (s[i] == ' ')
                   fprintf (ft, " ");
                else
                    fprintf (ft, "%c", replace[s[i] - 'a']);
                i++;
          }
          fprintf (ft, "\n");
    }
    
    return 0;
}
