#include <cstdio>
#include <cstring>
#define MAX 1101
char mat['Z'+3]['Z'+3],vec[MAX];
bool marca['Z'+3]['Z'+3];
bool eli['Z'+3]['Z'+3];//los que limpian la lista
int t,car,d,n,u,us['Z'+3];
void imprime()
{
    printf("[");
    if (u>=1)
        printf("%c",vec[1]);
    for (int i=2; i<=u; i++)
        printf(", %c",vec[i]);
    printf("]\n");
}
int main()
{
    scanf("%d",&t);
    char a,b,c;
    for(int g=1; g<=t; g++)
    {
        memset(mat,0,sizeof(mat));
        memset(us,0,sizeof(us));
        memset(eli,0,sizeof(eli));
        memset(marca,0,sizeof(marca));
        scanf("%d ",&car);
        for (int i=1; i<=car; i++)
        {
            scanf("%c%c%c",&a,&b,&c);
            mat[a][b]=c;
            mat[b][a]=c;
            marca[a][b]=true;
            marca[b][a]=true;
            scanf(" ");
        }
        scanf("%d ",&d);
        for (int i=1; i<=d; i++)
        {
            scanf("%c%c",&a,&b);
            eli[a][b]=true;
            eli[b][a]=true;
            scanf(" ");
        }
        scanf(" ");
        u=0;
        scanf("%d ",&n);
        for (int i=1; i<=n; i++)
        {
            scanf("%c",&a);//revisar si esta junto a alguno de los elementos que hacen que cambie
            if (u!=0)
            {
                if (marca[a][vec[u]])
                {
                    us[vec[u]]--;
                    char aux=vec[u];
                    vec[u]=mat[a][aux];
                    us[vec[u]]++;
                }
                else//ver si hay alguien opuesto a el en el vector
                {
                    for (int j='A'; j<='Z'; j++)
                    {
                        if (us[j]>0 && eli[a][j])
                        {
                            j='Z'+1;
                            memset(us,0,sizeof(us));
                            u=0;
                        }
                    }
                    if (u!=0)
                    {
                        vec[++u]=a;
                        us[a]++;
                    }
                }
            }
            else
            {
                vec[++u]=a;
                us[a]++;
            }
        }
        scanf("\n");
        printf("Case #%d: ",g);
        imprime();
    }
}
