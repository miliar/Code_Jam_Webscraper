#include<iostream>
using namespace std;

struct node
{
	int x,y,z;	
}p[1010];

bool mark[110][110];
int a[110][110];
int fx[4]={-1,0,0,1};
int fy[4]={0,-1,1,0};
char colors,color[110][110];

int cmp(const void *xx,const void *yy)
{
	if(  ((node *)xx)->z == ((node*)yy)->z )
	{
		if( ((node*)xx)->x == ((node*)yy)->x ) {
			((node*)xx)->y - ((node *)yy)->y;
		}
		return ((node*)xx)->x - ((node *)yy)->x;
	}
	return ((node*)yy)->z - ((node *)xx)->z;
}

char f(int x,int y)
{
	char c;
	int xx,yy,i,dir=10,maxz=a[x][y];
	mark[x][y]=true;
//	cout<<" # "<<x<<" "<<y<<" "<<color[x][y]<<endl; ///
	if(color[x][y]<'z'+1) return color[x][y];
	for(i=0;i<4;++i)
	{
		xx=x+fx[i]; yy=y+fy[i];
		//cout<<" @@@ "<<xx<<" "<<yy<<" "<<a[xx][yy]<<endl; 
		if(a[xx][yy]!=-1) 
		{
			if(a[xx][yy]<maxz) 
			{
				maxz=a[xx][yy];
				dir = i;
			} else if(a[xx][yy]==maxz && i<dir) dir=i;
		}
	}
	if(maxz<a[x][y]) 
	{
		xx=x+fx[dir]; yy=y+fy[dir];	
	//	cout<<" x y c "<<x<<" "<<y<<" "<<c<<" maxz = "<<maxz<<" xx yy color "<<xx<<" "<<yy<<" "<<color[xx][yy]<<endl; ///
	//	if(color[xx][yy]<'z'+1) c=color[xx][yy];	
		//else 
		c = f(xx,yy);
	} else  {
		if(color[x][y]<='z') c=color[x][y];
		else {
			++colors;			
			c=colors;
		}
	}
	color[x][y]=c;
	//cout<<" x y c "<<x<<" "<<y<<" "<<c<<endl; ////
	return c;
}

int main()
{
	int t,h,w,s,i,j;
	int x,y;
	int cases=0;
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d:\n",++cases);
		scanf("%d%d",&h,&w);
		s = -1;
		for(i=1;i<=h;++i) for(j=1;j<=w;++j) {
			scanf("%d",&a[i][j]);
			++s;
			p[s].x=i;
			p[s].y=j;
			p[s].z=a[i][j];
		}
		for(i=0;i<=w+1;++i) { a[0][i]=-1; a[h+1][i]=-1; }
		for(i=0;i<=h+1;++i) { a[i][0]=-1; a[i][w+1]=-1; }
	//	qsort(p,s+1,sizeof(p[0]),cmp);
		
		//for(i=0;i<=s;++i) cout<<p[i].z<<" "<<p[i].x<<" "<<p[i].y<<endl; ///
		colors ='a'-1;
		for(i=1;i<=h;++i) for(j=1;j<=w;++j) { mark[i][j]=false; color[i][j]='z'+1; }
		/*
		for(i=0;i<=s;++i)
		{
			x=p[i].x; y=p[i].y;
			if(!mark[x][y]) {
				f(x,y);
			}
		}*/
		for(i=1;i<=h;++i)
		{
			for(j=1;j<=w;++j) 
			{
				if(!mark[i][j]) f(i,j);
			}
		}
		for(i=1;i<=h;++i) {
			 for(j=1;j<=w;++j) {
			 	printf("%c",color[i][j]);
			 	if(j!=w) printf(" ");
			 }
			 printf("\n");
		}
	}
	return 0;
}
