#include <fstream>
#include <stdlib.h>
#define SIZE 6001
using namespace std;
bool hor[SIZE][SIZE]={0,},ver[SIZE][SIZE]={0,};
bool visit[SIZE][SIZE]={0,};
void main()
{
	int n,CASE;
	const int dir[4][2]={-1,0,0,1,1,0,0,-1};
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int ans=0;
		int l; char str[33]={0,};
		int i,j,k; int x=SIZE/2,y=SIZE/2,di=0;
		memset(hor,0,sizeof(hor)); memset(ver,0,sizeof(ver));
		memset(visit,0,sizeof(visit));
		in >> l;
		for(i=0;i<l;i++)
		{
			in >> str >> j;
			for(;j>0;j--)
			{
				for(k=0;k<strlen(str);k++)
				{
					switch(str[k])
					{
					case 'L':
						di--; if(di<0) di=3; break;
					case 'R':
						di++; if(di>3) di=0; break;
					case 'F':
						switch(di)
						{
						case 0:
							ver[x-1][y]=true; break;
						case 1:
							hor[x][y]=true; break;
						case 2:
							ver[x][y]=true; break;
						case 3: 
							hor[x][y-1]=true; break;
						}
						x+=dir[di][0]; y+=dir[di][1];
						break;
					}
				}
			}
		}
		int hcnt=0,vcnt=0,hmax,vmax;
		for(i=0;i<SIZE;i++)
		{
			hcnt=vcnt=0;
			hmax=vmax=0;
			for(j=0;j<SIZE;j++)
			{
				if(hor[j][i]) hmax=j;
				if(ver[i][j]) vmax=j;
			}
			for(j=0;j<SIZE;j++)
			{
				if(hor[j][i]) hcnt++;
				if(ver[i][j]) vcnt++;
				if(hcnt>0 && hcnt%2==0 && j<hmax && visit[j][i]!=true)
				{
					visit[j][i]=true;
					ans++;
				}
				if(vcnt>0 && vcnt%2==0 && j<vmax && visit[i][j]!=true)
				{
					visit[i][j]=true;
					ans++;
				}
			}
		}
		out << "Case #" << CASE+1 << ": " << ans << endl;
	}
	out.close();
	in.close();
}