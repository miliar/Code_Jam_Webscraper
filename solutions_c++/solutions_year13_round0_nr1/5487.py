#include <cstdio>
using namespace std;
char graph[4][4];
int main()
{
    int t;
    scanf("%d",&t);
    //getchar();
    for (int c = 1;c <= t;c++)
    {
        char res = 'n';
        bool point = false;
        for(int i = 0;i <4;i++)
        {
            for(int j = 0;j < 4;j++)
                scanf("%c",&graph[i][j]);
            //getchar();
        }
        //getchar();
        for(int i = 0;i < 4;i++)
        {
            char temp;
            if(res == 'n')
            {
                if(graph[i][0] == '.')
                {
                    point = true;
                    continue;
                }
                else if(graph[i][0] =='T')
                    temp = graph[i][1];
                else
                    temp = graph[i][0];
                int count = 0;
                for (int j = 0;j < 4;j++)
                {
                    if(graph[i][j] == temp || graph[i][j] == 'T')
                        count++;
                    else if(graph[i][j] == '.')
                    {
                        point = true;
                        break;
                    }
                    else
                    break;
                }
                if(count == 4 && temp != '.')
                res = temp;
                //printf("3\n");}
            }
        }
        for(int i = 0;i < 4;i++)
        {
            if(res == 'n')
            {
                char temp;
                if(graph[0][i] == '.')
                {
                    continue;
                    point = true;
                }
                else if(graph[0][i] =='T')
                    temp = graph[1][i];
                else
                    temp = graph[0][i];
                int count = 0;
                for (int j = 0;j < 4;j++)
                {
                    if(graph[j][i] == temp || graph[j][i] == 'T')
                        count++;
                    else if(graph[i][j] == '.')
                    {
                        point = true;
                        break;
                    }
                    else
                    break;
                }
                if(count == 4&& temp != '.')

                    res = temp;
                    //printf("4\n");}
            }
        }
        int i = 0;
        int j = 0;
        char temp;
        if(graph[0][0]!= 'T')
        temp = graph[0][0];
        else
        temp = graph[1][1];
        int count = 0;
        while(res == 'n' && i < 4 && j < 4 && temp != '.')
        {
            if(graph[i][j] == temp || graph[i][j] == 'T')
            {
                count++;
                i++;
                j++;
            }
            else
            break;
            if(count == 4)

                res = temp;
                //printf("5\n");}
        }
        i = 0;
        j = 3;
        if(graph[0][3]!= 'T')
        temp = graph[0][3];
        else
        temp = graph[1][2];
        count = 0;
        while(res == 'n' && i < 4 && j >=0 && temp != '.')
        {
            if(graph[i][j] == temp || graph[i][j] == 'T')
            {
                count++;
                i++;
                j--;
            }
            else
            break;
            if(count == 4)
            {
                res = temp;
                //printf("6\n");
            }

        }
        if(res == 'n' && point)
            printf("Case #%d: Game has not completed\n",c);
        else if(res == 'n')
            printf("Case #%d: Draw\n",c);
        else
            printf("Case #%d: %c won\n",c,res);
    }
}
