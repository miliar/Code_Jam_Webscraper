#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

bool tab[512][512];
int val[512][512];
bool cut[512][512];
typedef pair<int,int> para;
typedef pair<int,para> para2;
para2 p(int a, int b, int c){
	return para2(a,para(b,c));
}


int sums[513];

void jeden(){
	int n, m; scanf("%d%d\n", &m, &n);
	//printf("!! %d %d\n", m, n);
	for(int i = 0; i<m; i++){
		for(int j = 0; j<n; j+=4){
			char k; scanf(" %c", &k);
			int v;
			if(k>='0' && k<='9') v = k-'0';
			else v=10+k-'A';
			for(int z = 3; z>=0; z--){
				tab[i][j+z] = v&1;
				v>>=1;
			}
		}
		
	}
		
	/*printf("!!\n");
	for(int i = 0; i<m; i++){
		for(int j = 0; j<n; j++)
			printf("%d", tab[i][j]);
		printf("\n");
		
	}
	printf("!!\n");//*/
	
	priority_queue<para2> Q;
	for(int i = m-1;i>=0; i--)
		for(int j = n-1;j>=0; j--)
		{
			cut[i][j]=0;
			if(i==m-1 || j==n-1) val[i][j]=1;
			else if(tab[i][j]==tab[i+1][j+1] && tab[i][j]!=tab[i+1][j] && tab[i][j]!=tab[i][j+1])
			{
				val[i][j] = 1+min(min(val[i+1][j], val[i][j+1]), val[i+1][j+1]);
			}
			else val[i][j]=1;
			Q.push(p(val[i][j],-i, -j));
		}
	//	printf("!!!\n");
	/*for(int i = 0; i<m; i++){
		for(int j = 0; j<n; j++)
			printf("%d", val[i][j]);
		printf("\n");
	}*/
	for(int i = 0; i<=n; i++) sums[i]=0;
	while(!Q.empty()){
		int v = Q.top().first;
		int i = -Q.top().second.first;
		int j = -Q.top().second.second;
		Q.pop();
		if(cut[i][j] || val[i][j]!=v){
		//	if(!cut[i][j]) printf("$$ throw %d %d, v=%d, real=%d\n", i,j,v, val[i][j]);
		//	else printf("$$ cut %d %d, v=%d\n", i,j,v);
			continue;
		}
		//printf("%d %d v=%d\n", i, j, v);
		sums[v]++;
		
		for(int i2 = i; i2<i+v; i2++)
			for(int j2 = j; j2<j+v; j2++)
				cut[i2][j2]=1;
		for(int i2 = i+v-1; i2>=0 && i2>i-v; i2--)
			for(int j2 = j+v-1; j2>=0 && j2>j-v; j2--)
				if(!cut[i2][j2])
				{
					int oldv = val[i2][j2];
					if(i2==m-1 || j2==n-1 || cut[i2+1][j2]
						|| cut[i2][j2+1] || cut[i2+1][j2+1]) val[i2][j2]=1;
					else if(tab[i2][j2]==tab[i2+1][j2+1] && tab[i2][j2]!=tab[i2+1][j2]
						&& tab[i2][j2]!=tab[i2][j2+1])
					{
						val[i2][j2] = 1+min(min(val[i2+1][j2], val[i2][j2+1]), val[i2+1][j2+1]);
					}
					else val[i2][j2]=1;
					if(val[i2][j2]!=oldv) Q.push(p(val[i2][j2],-i2, -j2));
				}
		/*for(int i1 = 0; i1<m; i1++){
		for(int j1 = 0; j1<n; j1++)
			if(i1>=i && i1<i+v && j1>=j && j1<j+v)
			printf("#");
			else
			printf("%c", cut[i1][j1]?'-':val[i1][j1]+'0');
		printf("\n");
		}
		printf("!!\n");//*/
		
		
	}
	int diffs =0;
	for(int i = 0;  i<=n; i++)
		if(sums[i]) diffs++;
	printf("%d\n", diffs);
	for(int i = n; i>=0; i--)
		if(sums[i]) printf("%d %d\n",i, sums[i]);
}

main(){
	int c; scanf("%d", &c);
	for(int i = 1; i<=c; i++){
		printf("Case #%d: ", i);
		jeden();
	}
}
