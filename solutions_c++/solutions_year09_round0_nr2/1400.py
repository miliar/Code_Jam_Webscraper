#include<iostream>
#define Max 101
using namespace std;

int map[Max][Max], djs[Max*Max], h, w, dis[4][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
char table[Max*Max];

int tn(int a, int b)
{
	return a*w+b;
}

int find(int n)
{
	return (djs[n]==n ? n : djs[n]=find(djs[n]));
}

void dfs(int a, int b)
{
	int ta, tb, i, min, tt, t1, t2;
	for(i=0, min=map[a][b], tt=-1;i<4;i++)
	{
		ta=a+dis[i][0];
		tb=b+dis[i][1];
		if(ta>=0 && ta<h && tb>=0 && tb<w && map[ta][tb]<min)
		{
			min=map[ta][tb];
			tt=i;
		}
	}
	if(tt==-1)
	    return ;
	ta=a+dis[tt][0];
	tb=b+dis[tt][1];
	
	t1=tn(ta, tb), t2=tn(a, b);
	
	t1=find(t1), t2=find(t2);
	if(t1==t2)
	    return ;
	djs[t2]=t1;
	dfs( ta, tb );
}


int main()
{
	int z, zi, i, j, t;
	char now;
	scanf("%d", &z);
	for(zi=1;zi<=z;zi++)
	{
		scanf("%d %d", &h, &w);
		for(i=0;i<h;i++)
		{
		    for(j=0;j<w;j++)
		    {
		        scanf("%d", &map[i][j]);
		        djs[i*w+j]=i*w+j;
			}
		}

		for(i=0;i<h;i++)
		    for(j=0;j<w;j++)
		        dfs(i, j);

  		for(i=0;i<h;i++)
		    for(j=0;j<w;j++)
                djs[i*w+j]=find(djs[i*w+j]);
        
        memset(table, 0, sizeof(table));
        now='a';
        
        printf("Case #%d:\n", zi);
        for(i=0;i<h;i++)
        {
            t=djs[i*w];
			if(!table[t])
			    table[t]=now++;
			printf("%c",table[t]);
			
		    for(j=1;j<w;j++)
		    {
				t=djs[i*w+j];
				if(!table[t])
				    table[t]=now++;
    			printf(" %c",table[t]);
				
			}
			printf("\n");
		}

	}
}
