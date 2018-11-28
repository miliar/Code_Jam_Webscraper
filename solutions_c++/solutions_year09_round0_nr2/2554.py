#include <cstdio>
#include <queue>
using namespace std;
//#define PI pair <int,int>
#define H 150
#define W 150
struct PI{
	int a,b;
	PI () {}
	PI(int x,int y) :a(x),b(y) {}
	bool operator==(const PI & o){
		return a==o.a && b==o.b;
	}
	bool operator != (const PI & o){
		return !(*this == o);
	}
};
int map[H][W];
int dep[H][W];
PI p[H][W];
bool use[H][W];
char color[H][W];
PI v,V;
int m;
char cur;
queue <PI> q;

PI get(PI u){
	if (p[u.a][u.b]==u){
		return u;
	}
	p[u.a][u.b]=get(p[u.a][u.b]);
	return p[u.a][u.b];
}
void join(PI a,PI b)
{
	a=get(a);
	b=get(b);
	if (dep[a.a][a.b] > dep[b.a][b.b])
		swap(a,b);
	p[a.a][a.b]=b;
	if (a != b)
	{
		if (dep[a.a][a.b]==dep[b.a][b.b])
			++dep[b.a][b.b];
	}
}
int main(){
	int h=150,w=150,t;
	PI mv[4]={PI(-1,0),PI(0,-1),PI(0,1),PI(1,0)};
	scanf("%d",&t);
	for (int iter=1; iter<=t; ++iter){
	//for (int iter =15;iter<16;++iter){
		scanf("%d %d",&h,&w);
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				scanf("%d",&map[i][j]);
		for (int i=1; i<=h; ++i)
			map[i][0]=map[i][1],map[i][w+1]=map[i][w];
		for (int i=1; i<=w; ++i)
			map[0][i]=map[1][i],map[h+1][i]=map[h][i];
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j){
				//use[i][j]=0;
				dep[i][j]=0;
				p[i][j]=PI(i,j);
				color[i][j]='1';
			}
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j){
				//v = p[i][j];
				m = map[i][j];
				for (int k=0; k<4; ++k)
					if (m > map[i+mv[k].a][j+mv[k].b]){
						m = map[i+mv[k].a][j+mv[k].b];
						V = PI(i+mv[k].a,j+mv[k].b);
					}
				if (m != map[i][j]){
					join(PI(i,j),V);
				}
				/*
				if (!use[i][j]){
					use[i][j]=1;
					q.push(p[i][j]);
					while(!q.empty()){
						v = q.front();
						m = map[v.a][v.b];
						for (int k=0; k<4; ++k)
							if (m > map[v.a+mv[k].a][v.b+mv[k].b]){
								m = map[v.a+mv[k].a][v.b+mv[k].b];
								V = PI(v.a+mv[k].a,v.b+mv[k].b);
							}
						if (m != map[v.a][v.b]){
							join(v,V);
							q.push(V);
						}
						q.pop();
					}
				}
				*/
			}
		cur='a';
		printf("Case #%d:\n",iter);
		for (int i=1; i<=h; ++i){
			for (int j=1; j<=w; ++j){
				v=get(PI(i,j));
				if (color[v.a][v.b] == '1'){
					color[v.a][v.b] = cur++; 
				}
				printf("%c ",color[v.a][v.b]);
			}
			printf("\n");
		}
/*
		if (iter == 15){
			printf("\n%d %d\n\n",h,w);
			for (int i=0; i<=h+1; ++i){
				for (int j=0; j<=w+1; ++j)	
					printf("%d ",map[i][j]);
				printf("\n");
			}
*/
		/*
			printf("\n\n");
			for (int i=1; i<=h; ++i)
				pritnfmap[i][0]=map[i][1],map[i][w+1]=map[i][w];
			for (int i=1; i<=w; ++i)
				map[0][i]=map[1][i],map[h+1][i]=map[h][i];

	
			return 0;
		}
*/

#ifdef DEBUG
		for (int i=0; i<=h+1; ++i){
			for (int j=0; j<=w+1; ++j)
				printf("%d ",map[i][j]);
			printf("\n");
		}
#endif
	}
		
	return 0;
}
