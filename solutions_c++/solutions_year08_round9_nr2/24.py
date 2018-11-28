#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;


int zhan[2000000][2];
set<pair<int,int> > st;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j,l,t,x,y,x1,y1,x2,y2,w,h,top,bottom,xx,yy,num;
	_int64 ans;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&w,&h);
		scanf("%d%d",&x1,&y1);
		scanf("%d%d",&x2,&y2);
		scanf("%d%d",&x,&y);
		if (x1*y2==x2*y1)
		{
			st.clear();
			st.insert(make_pair(x,y));
			zhan[0][0]=x;
			zhan[0][1]=y;
			top=0;bottom=1;
			while (top<bottom)
			{
				xx=zhan[top][0]+x1;
				yy=zhan[top][1]+y1;
				if ((xx>=0)&&(xx<w)&&(yy>=0)&&(yy<h)&&(st.find(make_pair(xx,yy))==st.end()))
				{
					st.insert(make_pair(xx,yy));
					zhan[bottom][0]=xx;
					zhan[bottom][1]=yy;
					bottom++;
				}
				xx=zhan[top][0]+x2;
				yy=zhan[top][1]+y2;
				if ((xx>=0)&&(xx<w)&&(yy>=0)&&(yy<h)&&(st.find(make_pair(xx,yy))==st.end()))
				{
					st.insert(make_pair(xx,yy));
					zhan[bottom][0]=xx;
					zhan[bottom][1]=yy;
					bottom++;
				}
				top++;
			}
			ans=top;
		}
		else
		{
			xx=x;yy=y;
			num=0;
			while ((xx>=0)&&(xx<w)&&(yy>=0)&&(yy<h))
			{
				xx+=x1;yy+=y1;
				num++;
			}
			xx-=x1;yy-=y1;
			ans=0;
			while (num>0)
			{
				ans+=num;
				x+=x2;y+=y2;
				xx+=x2;yy+=y2;

				while ((xx>=0)&&(xx<w)&&(yy>=0)&&(yy<h))
				{
					xx+=x1;yy+=y1;
					num++;
				}
				xx-=x1;yy-=y1;
				num--;
				while (((xx<0)||(xx>=w)||(yy<0)||(yy>=h))&&(num>0))
				{
					xx-=x1;yy-=y1;
					num--;
				}
				while (((x<0)||(x>=w)||(y<0)||(y>=h))&&(num>0))
				{
					x+=x1;y+=y1;num--;
				}
			}
		}
		printf("Case #%d: %lld\n",l+1,ans);
	}
	return  0;
}

