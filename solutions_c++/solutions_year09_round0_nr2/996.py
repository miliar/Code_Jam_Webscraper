#include<iostream>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
int a[101][101];
char b[101][101];
pair <int,int> loc[101][101];
pair <int , int> neighbor(int x, int y, int h, int w)
{
	int i=x,j=y,mn=a[x][y];
	
	if(x-1 >= 0 && a[x-1][y]<a[x][y])
	{	mn=a[x-1][y];i=x-1;j=y;}
	if(y-1 >= 0 && a[x][y-1]<mn)
	{	mn=a[x][y-1];i=x;j=y-1;}
	if(y+1 < w && a[x][y+1]<mn)
	{	mn=a[x][y+1];i=x;j=y+1;}
	if(x+1 < h && a[x+1][y]<mn)
	{	mn=a[x+1][y];i=x+1;j=y;}
	
	
		return make_pair(i,j);
}
int main()
{
     int cases,cas;
     cin>>cases;
     int h,w,i,j;
     //cout<<"hi";
     for(cas=1;cas<=cases;cas++)
     {
     	cin>>h>>w;
     	for(i=0;i<h;i++)
     		for(j=0;j<w;j++)	
     			cin>>a[i][j];
     	//cout<<"hi";
     	memset(b,'.',sizeof(b));
     	b[0][0]='.';
     	char cur='a';
     	
     	for(i=0;i<h;i++)
     		for(j=0;j<w;j++)
     		{
     				pair <int,int> neig=neighbor(i,j,h,w);
     				loc[i][j]=neig;
     		}
     		
     	/*for(i=0;i<h;i++)
     	{
     		for(j=0;j<w;j++)
     		{
     				cout<<"("<<loc[i][j].first<<","<<loc[i][j].second<<") ";
     		}
     		cout<<endl;
     	}*/
     		//cout<<"hi2";
     	i=0;j=0;char now;int m,n;
     	while(1)
     	{
     		m=i;n=j;
     		if(b[i][j]=='.')
     		{
    	 		while(loc[i][j]!=make_pair(i,j))
     			{
     				i=loc[i][j].first;
     				j=loc[i][j].second;
     				if(b[i][j]!='.')break;
     				//cout<<"hi3";
     			}
     		
     		
     			if(b[i][j]!='.')
     			{
	     			now=b[i][j];
    	 			//while()	
     			}
     			else
     			{
     				b[i][j]=cur++;
     				now=b[i][j];	
     			}
     			//cout<<"hi";
     			i=m;j=n;
     			while(loc[i][j]!=make_pair(i,j))
     			{
	     			b[i][j]=now;
    	 			i=loc[i][j].first;
     				j=loc[i][j].second;
     				if(b[i][j]!='.')break;
     			}
     		}
     		i=m;j=n;
     		j++;
     		if(j>=w){j=0;i++;}
     		if(i>=h)break;
     		//cout<<endl<<m<<" "<<n<<endl;
      	
     	}
     	cout<<"Case #"<<cas<<": "<<endl;
     	for(i=0;i<h;i++)
     	{
     		for(j=0;j<w;j++)
     			cout<<b[i][j]<<" ";
     		cout<<endl;
     	}
     }
     return 0;
}
