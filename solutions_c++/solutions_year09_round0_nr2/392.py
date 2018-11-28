#include<iostream>
#include<queue>
using namespace std;
struct po
{
	int x,y;
};
int pi[]={-1,0,0,1};
int pj[]={0,-1,1,0};
int mp[101][101];
char ta[101][101];
int h,w;
po mi(int i,int j)
{
	int min =100001;
	int x=-1,y=-1;
	for(int k = 0 ; k < 4 ; k ++)
	{
		int i1 = i + pi[k];int j1 = j +pj[k];
			if(i1>=0&&i1<h&&j1>=0&&j1<w)
			{
				if(min>mp[i1][j1])
				{
					min=mp[i1][j1];
					x = i1;
					y = j1;
				}
			}

	}
	po an;
	an.x =x;an.y = y;
	return an;

}


int main()
{
	
	
	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);
	queue<po> q;
	int n;
	cin>>n;
	int ca=1;
	
	while(ca<=n)
	{
		
		cin>>h>>w;
		int i,j;
		for( i = 0 ; i < h; i++)
			for(j = 0 ; j < w; j++)
			{
				cin>>mp[i][j];
				ta[i][j] = 'A';
			}
			//ta[f.x ][f.y] = 'a';
			char ch = 'a';
			int k;
		for( i = 0 ; i < h; i++)
			for(j = 0 ; j < w; j++)
			{
				if(ta[i][j]=='A')
				{
					ta[i][j]=ch;
					po f;
					f.x = i; f.y = j;
					q.push(f);
					while(!q.empty())
					{
					   po fi = q.front();q.pop();
					   for(k = 0 ; k < 4 ; k ++)
					   {
							int i1 = fi.x + pi[k];int j1 = fi.y +pj[k];
							if(i1>=0&&i1<h&&j1>=0&&j1<w)
							{
								if(ta[i1][j1]=='A')
								{
									po m = mi(i1,j1);
									if(m.x!=-1&&m.x==fi.x&&m.y ==fi.y&&mp[i1][j1]>mp[fi.x][fi.y])
									{
										ta[i1][j1]=ch;
										m.x=i1;m.y =j1;
										q.push(m);
										//cout<<q.size()<<endl;
									}
								}
							}
						}
					   po lit=mi(fi.x,fi.y);
					   if(lit.x!=-1&&ta[lit.x][lit.y]=='A'&&mp[lit.x][lit.y]<mp[fi.x][fi.y])
					   {
							ta[lit.x][lit.y]=ch;
							q.push(lit);
					   }
					   

					}
					ch++;
				}
			}
			printf("Case #%d:\n",ca);
			ca++;
			for( i = 0 ; i < h; i++)
			{
				for(j = 0 ; j < w-1; j++)
				{
				printf("%c " ,ta[i][j]);
				}
				printf("%c\n",ta[i][w-1]);
			}
	}

return 0;
}