#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int T;
int N, M, n;
int ans;

typedef struct node
{
        int floor;
        int fa;
        char name[101];
}node;

int main()
{
	int i, j, k, l,pos,end,fl;
	bool flag;
	char temp[101];
    char getname[101];
	node v[10001];

    freopen("File.in", "r", stdin);
    freopen("File.out", "w", stdout);
    scanf("%d", &T);
    for(i = 1; i <= T; i++)
    {
        scanf("%d%d", &N, &M);
        n = 0;
        ans = 0;
        memset(v, 0, sizeof(v));
        for(j = 1; j <= N; j++)
        {
            k = 1;
            pos;
            end = 0;
            fl = 0;
            
            memset(temp, 0, sizeof(temp));
            scanf("%s", temp);
            while(1)
            {
                memset(getname, 0, sizeof(getname));
                pos = 0;
                for(; temp[k]!= '/' && temp[k] != '\0'; k++)
                {
                    getname[pos] = temp[k];
                    pos++;
                }
                flag = 1;
                for(int l = 1; l <= n; l++)
                {
                    if(!strcmp(getname, v[l].name) && v[l].floor == fl && v[l].fa == end)
                    {
                        end = l;
                        flag = 0;
                        break;
                    }
                }
                if(flag)
                {
                    n++;
                    strcpy(v[n].name, getname); 
                    v[n].floor = fl;
                    v[n].fa = end;
                    end = n;
                }
                if(temp[k] == '\0') break;
                k++;
                fl++;
            }
        }
        for(j = 1; j <= M; j++)
        {

            memset(temp, 0, sizeof(temp));
            scanf("%s", temp);
            while(1)
            {
                memset(getname, 0, sizeof(getname));
                pos = 0;
                for(; temp[k]!= '/' && temp[k] != '\0'; k++)
                {
                    getname[pos] = temp[k];
                    pos++;
                }
				flag = 1;
                for(l = 1; l <= n; l++)
                {
                    if(!strcmp(getname, v[l].name) && v[l].floor == fl && v[l].fa == end)
                    {
                        end = l;
                        flag = 0;
                        break;
                    }
                }
                if(flag)
                {
                    n++;
                    strcpy(v[n].name, getname); 
                    v[n].floor = fl;
                    v[n].fa = end;
                    end = n;
                    ans++;
                }
                if(temp[k] == '\0') break;
                k++;
                fl++;
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}