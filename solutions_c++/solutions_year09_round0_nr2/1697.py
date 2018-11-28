#include <cstdio>

// North, West, East, South.
const int vec[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int R,C;
int set[111*111];
int h[111*111];
int mat[111][111];

inline void Union(int root1,int root2)  
{
    if(root1==root2)
       return;
    else if(set[root2]<=set[root1]){
       set[root2]+=set[root1];
       set[root1]=root2;
    }
    else{
       set[root1]+=set[root2];
       set[root2]=root1;
    }
}

inline int Find(int x)                 
{
    if(set[x]<=0)
       return x;
    else
       return set[x]=Find(set[x]);
}

inline int get_id(int r,int c)
{
	return r*C+c+1;	
}

inline bool valid(int r,int c)
{
	return 0<=r&&r<R && 0<=c&&c<C;
}

inline void go()
{
	for(int i=1;i<=R*C;++i){
		set[i]=-1;
		h[i]=-1;
	}
	
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			int r;
			int c;
			int rr;
			int cc;
			int height=mat[i][j];
			int direc=-1;
			for(int t=0;t<4;++t){
				r=i+vec[t][0];
				c=j+vec[t][1];
				if(valid(r,c)&&mat[r][c]<height){
					height=mat[r][c];
					direc=t;
					rr=r;
					cc=c;
				}
			}
			if(direc!=-1){
				Union(Find(get_id(i,j)),Find(get_id(rr,cc)));
			}
		}	
	}
	
	char cur='a';
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			if(j){
				putchar(' ');
			}
			int now=Find(get_id(i,j));
			if(h[now]==-1){
				h[now]=cur;
				++cur;
			}
			putchar(h[now]);	
		}
		printf("\n");
	}
}

int main()
{
	//freopen("B-small.in","r",stdin);
	//freopen("B-small.out","w",stdout);
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int re;
	int cas;
	for(cas=1,scanf("%d",&re);re--;++cas){
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;++i){
			for(int j=0;j<C;++j){
				scanf("%d",&mat[i][j]);
			}
		}
		printf("Case #%d:\n",cas);
		go();
	}
}
