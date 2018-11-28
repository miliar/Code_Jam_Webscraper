#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

int t,w,h;
char mas[102][102];
int val[102][102];
bool used[102][102];
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

void process(int x, int y, char ch)
	{
//	cout<<"In the function: "<<x<<" "<<y<<" "<<ch<<endl;
	used[x][y] = true;
	mas[x][y] = ch;	
	int minim = BIG, p = -1;
	fr(i,4)
		if(val[x+dx[i]][y+dy[i]]<minim&&val[x+dx[i]][y+dy[i]]<val[x][y])
			{
			minim = val[x+dx[i]][y+dy[i]];
			p = i;
			}
	if(p!=-1&&!used[x+dx[p]][y+dy[p]]) 
		{
//		cout<<"Get lower: "<<x+dx[p]<<" "<<y+dy[p]<<" "<<ch<<endl;
		process(x+dx[p],y+dy[p],ch);
		}
	fr(i,4)
		if(!used[x+dx[i]][y+dy[i]]&&val[x+dx[i]][y+dy[i]]>val[x][y])
			{
        		int xtemp = x+dx[i];
			int ytemp = y+dy[i];
//			cout<<"Higher candidate: "<<xtemp<<" "<<ytemp<<endl;
			minim = BIG;
			p = -1;
			fr(j,4)
				if(val[xtemp+dx[j]][ytemp+dy[j]]<minim&&val[xtemp+dx[j]][ytemp+dy[j]]<val[xtemp][ytemp])
					{
					minim = val[xtemp+dx[j]][ytemp+dy[j]];
					p = j;
					}
			if(p==-1) continue;
			if(xtemp+dx[p]==x&&ytemp+dy[p]==y)
				{
//				cout<<"Get higher: "<<xtemp<<" "<<ytemp<<endl;
				process(xtemp,ytemp,ch);
				}
			}
	}

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d",&t);
fr(i,t)
	{
	scanf("%d%d", &h, &w);
	memset(used, 0, sizeof(used));
	fw(ii,1,h)
	fw(jj,1,w)
		scanf("%d", &val[ii][jj]);
	int k = 0;
	fw(ii,0,h+1)
		val[ii][0] = val[ii][w+1] = BIG;
	fw(ii,0,w+1)
		val[0][ii] = val[h+1][ii] = BIG;

	fw(ii,1,h)
	fw(jj,1,w)
		if(!used[ii][jj])
			{
//			cout<<"\t\tFOUND: "<<ii<<" "<<jj<<endl;
			process(ii,jj,'a'+k);	
			k++;
			}
	printf("Case #%d:\n", i+1);
	fw(ii,1,h)
		{
		fw(jj,1,w)
			{
			printf("%c ", mas[ii][jj]);
//			if(jj!=w) printf(" ");
			}
		printf("\n");
		}
	}
return 0;
}
