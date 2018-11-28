#include<stdio.h>  
#include<string.h>

// Max Clique algorith from:
// http://blog.csdn.net/xiaojun_wu/archive/2004/07/28/53952.aspx

int joint[100][100];
int price[100][100];
int Size;
int MAX;
int kk;
int DP[100];
bool find;

int reachEnd(int start,int sets[])
{  
int lp;
for(lp=start ; lp<Size ; lp++)
    if(sets[lp])
       return lp;
return -1;
}
void DFS(int Visit[], int start ,int depth )
{
    int loop;
int first;
int sets[100],SET[100];
memcpy(sets,Visit,Size*4);
memcpy(SET,Visit,Size*4);
if((first=reachEnd(start,sets))==-1)
 {
     if(depth > MAX){
        MAX=depth;
        find=true;
        }
     return ;
 }
while( first != -1){
 
     if(depth+Size-start <= MAX)
       return ;
     if(depth+DP[first] <=MAX)
     return;
 
 sets[first]=0;
     SET[first]=0;
 for(loop=first+1;loop<Size;loop++)
     if(SET[loop]==1 && joint[first][loop]==1)
        sets[loop]=1;
     else
       sets[loop]=0;
 DFS(sets,first,depth+1);
 if(find)
     return ;
 first=reachEnd(first,SET);
 }
}

bool harmony(int i, int j)
{
    bool org = false;
    for (int k = 0; k < kk; k++)
    {
        if (price[i][k] == price[j][k]) return false;
        bool b = price[i][k] > price[j][k];
        if ((k > 0) && (b != org)) return false;
        org = b;
    }
    return true;
}

int main()
{
int loop,lp;
int Visit[100];
int cases;
scanf("%d", &cases);

for (int ri = 0; ri < cases; ri++)
{

scanf("%d %d",&Size, &kk);
/*
    for(loop=0;loop<Size;loop++)
       for(lp=0;lp<Size;lp++)
         scanf("%d",joint[loop]+lp);
*/
memset(joint, 0, sizeof(joint));
for (int i = 0; i < Size; i++)
{
    for (int z = 0; z < kk; z++)
    {
        scanf("%d", &price[i][z]);
    }
    for (int j = 0; j < i; j++)
    {
        if (!harmony(i, j))
        {
                        joint[i][j] = joint[j][i] = 1;
        }
    }
}
    MAX=0;
    for(loop=Size-1 ; loop>=0 ; loop--){
       find=false;
        memcpy(Visit,joint[loop],Size*4);
       DFS(Visit,loop,1);
       DP[loop]=MAX;
    }
    printf("Case #%d: %d\n", ri + 1, DP[0]);
}
return 0;
}
