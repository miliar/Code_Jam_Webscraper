#include <stdio.h>
#include <stdlib.h>

#define MAX 1000000
struct node{
    int x;
    struct node *next;
}Node[10001];

int visit[10001];
int cycle[10001];
int al[102][102];

int h,w;
int size;
int c;
void init()
{
    int i;
    for(i=1; i<=size; i++)
    {
        Node[i].next =NULL;
        visit[i] = 0;
    }
}

void dfs(int v)
{
    struct node *temp = Node[v].next;
    visit[v] = 1;
    cycle[v] = c;
    while(temp != NULL)
    {
        if( !visit[temp->x])
            dfs(temp->x);
        temp = temp->next;
    }
}

int main()
{
    int t;
    int i, j, k;
    int x, y;
    char label;
    
    scanf("%d",&t);
    for( i=1; i<=t; i++ )
    {
        scanf("%d%d",&h,&w);
        size = h * w;
        c = 0;
        init();
        for(j=1; j<=h; j++)
            for(k=1; k<=w; k++)
                scanf("%d",&al[j][k]);
        for(j = 0; j<=w+1; j++)
            al[0][j] = al[h+1][j] = MAX;
        for(j = 0; j<=h+1; j++)
            al[j][0] = al[j][w+1] = MAX;              
        for( j=1; j <= h; j++)
            for(k=1; k <= w; k++)
            {
                x = j;
                y = k;
                //printf("%d %d\n",j,k);
                if( al[x][y] > al[j-1][k])
                {
                    x = j-1;
                    y = k;
                }
                if( al[x][y] > al[j][k-1]) 
                {
                    x = j;
                    y = k-1;
                }
                if( al[x][y] > al[j][k+1] )
                {  
                    x = j;
                    y = k + 1;
                }
                if( al[x][y] >al[j+1][k] )
                {      
                    x = j+1;
                    y = k;
                }
               
                if(x != j || y != k)
                {
                    struct node * a =(struct node *)malloc(sizeof(struct node));
                    struct node * b =(struct node *)malloc(sizeof(struct node));
                    a->x = (x-1)*w + y;
                    a->next = Node[(j-1)*w+k].next;
                    Node[(j-1)*w+k].next = a;
                    b->x = (j-1)*w + k;
                    b->next = Node[(x-1)*w+y].next;
                    Node[(x-1)*w+y].next = b;
                } 
            }
        #ifdef DEBUG
        for(j=1; j<=size; j++)
        {
            struct node *temp = Node[j].next;
            while(temp)
            {
                printf("%d ",temp->x);
                temp = temp->next;
            }
            printf("\n");
        }
        #endif
        for(j=1; j<=size; j++)
            if( !visit[j])
            {
                dfs(j);  
                c++;
            }         
        printf("Case #%d:\n",i);
        #ifdef DEBUG
        for(j=1; j<=size; j++)
            printf("%d ",cycle[j]);
        printf("\n");
        #endif
        for(j=1; j<=h; j++)
        {
            for(k=1; k<=w; k++)
            {
                printf("%c",'a'+cycle[(j-1)*w+k]);
                if(k!=w)
                    printf(" ");
            }
            printf("\n");
        }
    }
    //while(1);
    return 0;
}

