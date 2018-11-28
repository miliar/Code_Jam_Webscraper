#include <iostream>
using namespace std;

long casen,k,i,j,n,m;
long cs[120][1200];
long minn;
long ind[120];
bool suc;
long maxi,now;
char w[120][5000];
char v[1200][5000];
char s[1000];
int main()
{
	freopen("a2.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>casen;
	for (k=1;k<=casen;k++)
	{
		cin>>n;
		cin.getline(s,100);
		for (i=0;i<n;i++) cin.getline(w[i],4000);
		cin>>m;
		cin.getline(s,100);
		for (i=0;i<n;i++) cs[i][0]=0;
		for (j=0;j<m;j++) 
		{
			cin.getline(v[j],4000);
			for (i=0;i<n;i++) if (strcmp(w[i],v[j])==0) 
			{
				cs[i][0]++;
				cs[i][cs[i][0]]=j;
			}
		}
		minn=0;
		for (i=0;i<n;i++) ind[i]=1;
		suc=false;
		while (suc==false)
		{
			maxi=-1;now=-1;
			for (i=0;i<n && suc==false;i++)
			{
				if (ind[i]>cs[i][0]) suc=true;
				else
				{
					if (cs[i][ind[i]]>maxi)
					{
						maxi=cs[i][ind[i]];
						now=i;
					}
				}
			}
			if (suc==false)
			{
				//cout<<maxi<<' '<<w[now]<<endl;
				for (i=0;i<n;i++) while (cs[i][ind[i]]<maxi && ind[i]<=cs[i][0]) ind[i]++;
				minn=minn+1;
			}
		}
		cout<<"Case #"<<k<<": "<<minn<<endl;
	}
	return 0;
}
