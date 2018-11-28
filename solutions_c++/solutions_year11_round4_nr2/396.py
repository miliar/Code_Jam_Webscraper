#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
using namespace std;
int mat[1123][1231];
int n,d,m;
int yz(int i,int q,int d)
{
	double  x=0,y=0;
	for(int ii=0;ii<d;ii++)
		for(int qq=0;qq<d;qq++)
		{
			if((ii==0&&qq==0)||(ii==0&&qq==d-1)||(ii==d-1&&qq==d-1)||(ii==d-1&&qq==0))continue;
			x+=mat[ii+i][qq+q]*(ii-(d-1)/2.0);
			y+=mat[ii+i][qq+q]*(qq-(d-1)/2.0);
			//cout<<mat[i+ii][q+qq]<<"   "<<ii<<"   "<<qq<<"  "<<ii-(d-1)/2.0<<"  "<<qq-(d-1)/2.0<<endl;
		}
		//cout<<x<<"  "<<y<<endl;
		return x==0&&y==0;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		cin>>n>>m>>d;
		for(int i=0;i<n;i++)
			for(int q=0;q<m;q++)
			{
				char z;
				cin>>z;
				mat[i][q]=z-'0';//+d;
			}
			int da=-1;
			//cout<<yz(1,1,5)<<endl;;
			//continue;
			for(int i=0;i<n;i++)
				for(int q=0;q<m;q++)
				{
					for(int d=3;i+d-1<n&&q+d-1<m;d++)
					{
						if(yz(i,q,d))
						{
							//cout<<d<<endl;
							da=max(da,d);
						}
					}
				}
		printf("Case #%d: ",cas++);
		if(da+1)
			cout<<da<<endl;
		else puts("IMPOSSIBLE");
	}
}