#include <iostream>
#include <map>
#include <string>
using namespace std;

int n, x;
int X[800], Y[800];
int graph[800][800];
int m1[100], m2[800];

const long long inf = (long long) 100000 * (long long) 100000 * (long long) 800;
//const int inf = 1000000000;
#define MAXN 800
#define _clr(x) memset(x,0xff,sizeof(int)*n)

long long kuhn_munkras(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],q,i,j,k;
	long long ret = 0, l1[MAXN],l2[MAXN], p;
	for (i=0;i<m;i++)
		for (l1[i]=-inf,j=0;j<n;j++)
			l1[i]=mat[i][j]>l1[i]?mat[i][j]:l1[i];
	for (i=0;i<n;l2[i++]=0);
	for (_clr(match1),_clr(match2),i=0;i<m;i++){
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (l1[k]+l2[j]==mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
		if (match1[i]<0){
			for (i--,p=inf,k=0;k<=q;k++)
				for (j=0;j<n;j++)
					if (t[j]<0&&l1[s[k]]+l2[j]-mat[s[k]][j]<p)
						p=l1[s[k]]+l2[j]-mat[s[k]][j];
			for (j=0;j<n;l2[j]+=t[j]<0?0:p,j++);
			for (k=0;k<=q;l1[s[k++]]-=p);
		}
	}
	for (i=0;i<m;i++)
		ret+=mat[i][match1[i]];
	return ret;
}

void input()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &X[i]);
    }  
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &Y[i]);
        for (int j = 0; j < n; j++)
        {
            graph[i][j] = -Y[i] * X[j];
        }    
    }  
     
}  

void solve()
{
    printf("Case #%d: %d\n", ++x, -kuhn_munkras(n, n, graph, m1, m2));
}      

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    //cout << inf << endl;
    while (t--)
    {
        input();
        solve();
    }  
}    
