#include<iostream>
using namespace std;
char mat[110][110];

int bx[5]={1,0,-1,0,1};
int by[5]={0,1,0,-1,0};
int ax[4]={-1,-1,1,1};
int ay[4]={1,-1,-1,1};
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int CaSe = 1 ;CaSe<=zu;CaSe++)
	{
		printf("Case #%d: ",CaSe);

		int m;
		scanf("%d",&m);
		gets(mat[1]);
		memset(mat,0,sizeof(mat));
		for(int i=1;i<2*m;i++)
		{
			gets(mat[i]);
		}

		int z = 10000;

		int cx[5]={0};
		int cy[5]={0};
		for(int juli  = 0;juli<=z;juli++){

			int shangxian = 4;
			if(juli == 0)shangxian =1;
			for(int dir= 0;dir<shangxian;dir++){
				int jieshu = cx[dir+1];
				if(juli ==0 )jieshu= cx[dir+1]+ax[dir];
				for(int iii = cx[dir],jjj=cy[dir];iii!=jieshu;iii+=ax[dir],jjj+=ay[dir])
				{
						int ii = iii+m;
						int jj=jjj+m-1;


						bool flag  = 1;
						for(int i=0;i<m &&flag ;i++)
						{
							int xa = i+1;
							int ya=m-i-1;
							for(int j=0;j<m &&flag;j++)
							{
								int x = xa+j;
								int y = ya+j;
								//a[i][j]=mat[x+j][y+j]-'0';
								int x1 = 2 * ii- x;
								int y1= y;
								if(x1>=2*m||x1<1)continue;
								if(mat[x1][y1]==' ' ||mat[x1][y1]==0)continue;
								if(mat[x1][y1]!=mat[x][y])
								{
									flag = 0;
									break;
								}
							}
							for(int j=0;j<m &&flag;j++)
							{
								int x = xa+j;
								int y = ya+j;
								int x2 = x;
								int y2 = 2*jj-y;
								if(y2>=2*m-1||y2<0)continue;
								if(mat[x2][y2]==' ' ||mat[x2][y2]==0)continue;
								if(mat[x2][y2]!=mat[x][y])
								{
									flag = 0;
									break;
								}
							}
						}
						if(flag)
						{
							//cout<<ii<<" "<<jj<<" "<<juli<<endl;
							z= min(z,juli);
						}
					}




			}



			for(int i=0;i<5;i++)
				cx[i]+=bx[i],cy[i]+=by[i];
		}
		long long r = z+m;
		//cout<<m<<" "<<z<<" ";
		cout<<r*r-m*m<<endl;
	}
}