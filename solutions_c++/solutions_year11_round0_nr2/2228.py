#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>


using namespace std;

char search_complement(char str[3], char c)
{
    if(c == str[0])
        return str[1];
    if(c == str[1])
        return str[0];
    return '\0';
}

int search_vector(vector<char> elem,char c)
{
    int i,l;
    l = int(elem.size());
    for(i = 0; i < l; i++)
    {
        if(elem[i] == c)
            return 1;
    }
    return 0;
}

int main()
{
    char combine[100][4];
    char opossed[100][3];
 
    vector<char> elem;

    char line[101],op,c1,c2, invoke1[3],invoke2[3];

    int i,j,k,t,c,d,n,len,x;

    scanf("%d",&t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d",&c);
        for(j = 0; j < c; j++)
        {
            scanf("%s",combine[j]);
        }

        scanf("%d",&d);
        for(j = 0; j < d; j++)
        {
            scanf("%s",opossed[j]);
        }

        scanf("%d",&len);
        scanf("%s",line);

        for(j = 0; j < len; j++)
        {
            elem.push_back(line[j]);

            x = int(elem.size());
            if(x > 1)
            {
                c1 = elem[x-2];
                c2 = elem[x-1];
                if(strchr("QWERASDF",c1) != NULL && strchr("QWERASDF",c2) != NULL)
                {
                    invoke1[0] = c1;invoke1[1]=c2;invoke1[2] = '\0';
                    invoke2[0] = c2;invoke2[1]=c1;invoke2[2] = '\0';
   
                    for(k = 0; k < c; k++)
                    {
                        if(strstr(combine[k],invoke1) != NULL || strstr(combine[k],invoke2) != NULL)
                        {
                            op = combine[k][2];
                            elem.pop_back();
                            elem.pop_back();
                            elem.push_back(op);
                            break;
                        }
                    } 
                }
            }
            x = int(elem.size());
            if (x > 0 && strchr("QWERASDF",elem[x-1]) != NULL) 
            {
                for(k = 0; k < d; k++)
                {
                    op = search_complement(opossed[k],elem[x-1]);
                    if(op != '\0' && search_vector(elem,op))
                    {
                        elem.clear();
                        break;
                    }
                }
            }

        }

        if(elem.size())
        {
            printf("Case #%d: [",i);
            for(j = 0; j < int(elem.size()) - 1; j++)
            {
                printf("%c, ",elem[j]);
            }
            printf("%c]\n",elem[j]);
        }
        else
            printf("Case #%d: []\n",i);
        elem.clear();
    }

    return 0;
}