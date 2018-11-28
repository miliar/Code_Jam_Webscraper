#include<iostream>
using namespace std;
bool map1[10005][10005];
bool map2[10005][10005];
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out.txt","w",stdout);
	int c,ii;
	cin>>c;
	for(ii=1;ii<=c;ii++)
	{
		int r;
		cin>>r;
		int i,j;
		int max_x=1,max_y=1,choose=1,num=0;
		while(r--)
		{
			int x1,x2,y1,y2;
			cin>>x1>>y1>>x2>>y2;
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
				{
					if(x2>max_x) max_x=x2;
					if(y2>max_y) max_y=y2;
					map1[j][i]=true;
					num++;
				}
		}
		int count=0;
		while(num>0)
		{
		if(choose==1)
		{
			num=0;
			for(i=1;i<=max_x;i++)
				for(j=1;j<=max_y;j++)
				{
					if((map1[j][i]==true)&&(map1[j-1][i]==false)&&(map1[j][i-1]==false))
						map2[j][i]=false;
					else if((map1[j][i]==false)&&(map1[j-1][i]==true)&&(map1[j][i-1]==true))
					{
						map2[j][i]=true;
						num++;
					}
					else 
					{
						map2[j][i]=map1[j][i];
						if(map2[j][i]==true)
							num++;
					}

				}
			choose=2;
		}
		else
		{
			num=0;
			for(i=1;i<=max_x;i++)
				for(j=1;j<=max_y;j++)
				{
					if((map2[j][i]==true)&&(map2[j-1][i]==false)&&(map2[j][i-1]==false))
						map1[j][i]=false;
					else if((map2[j][i]==false)&&(map2[j-1][i]==true)&&(map2[j][i-1]==true))
					{
						map1[j][i]=true;
						num++;
					}
					else 
					{
						map1[j][i]=map2[j][i];
						if(map1[j][i]==true)
							num++;
					}

				}
			choose=1;
		}
		count++;
		}
		cout<<"Case #"<<ii<<": "<<count<<endl;
	}
	return 0;
}