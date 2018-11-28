#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
//#include<pair>
using namespace std;
void doPaint(vector<vector<int> > map,int i,int j,vector<pair<int,int> > links,int w,int h,fstream &out)
{
	pair<int,int> p;
	int left,right,up,down;
	if(j==0)
		left=0;
	else 
		left=j-1;	
	if(j==w-1)
		right=w-1;
	else
		right=j+1;

	if(i==0)
		up=0;
	else
		up=i-1;

	if(i==h-1)
		down=h-1;
	else
		down=i+1;
	int min,min1,min2;
	min1=map[up][j]<map[down][j]?map[up][j]:map[down][j];
	min2=map[i][left]<map[i][right]?map[i][left]:map[i][right];
	min=min1<min2?min1:min2;
	if(map[i][j]<=map[up][j]&&map[i][j]<=map[down][j]&&map[i][j]<=map[i][left]&&map[i][j]<=map[i][right])
	{
		p.first=i;
		p.second=j;
		out<<(char)(('a')+(find(links.begin(),links.end(),p)-links.begin()))<<" ";
	}else if(min<map[i][j])
	{
		//xiayige
		if(min==map[up][j])
		{
			doPaint(map,up,j,links,w,h,out);return;
		}else if(min==map[i][left])
		{
			doPaint(map,i,left,links,w,h,out);return;
		}else if(min==map[i][right])
		{
			doPaint(map,i,right,links,w,h,out);return;
		}else
		{
			doPaint(map,down,j,links,w,h,out);return;
		}
	}

}
void doGetLinks(vector<vector<int> > map,int i,int j,vector<pair<int,int> > &links,int w,int h)
{
	pair<int,int> p;
	int left,right,up,down;
	if(j==0)
		left=0;
	else 
		left=j-1;	
	if(j==w-1)
		right=w-1;
	else
		right=j+1;

	if(i==0)
		up=0;
	else
		up=i-1;

	if(i==h-1)
		down=h-1;
	else
		down=i+1;
	int min,min1,min2;
	min1=map[up][j]<map[down][j]?map[up][j]:map[down][j];
	min2=map[i][left]<map[i][right]?map[i][left]:map[i][right];
	min=min1<min2?min1:min2;
	if(map[i][j]<=map[up][j]&&map[i][j]<=map[down][j]&&map[i][j]<=map[i][left]&&map[i][j]<=map[i][right])
	{
		p.first=i;
		p.second=j;
		if(find(links.begin(),links.end(),p)>=links.end())
			links.push_back(p);
		//cout<<(char)(('a')+(find(links.begin(),links.end(),p)-links.begin()))<<" ";
	}else if(min<map[i][j])
	{
		//xiayige
		if(min==map[up][j])
		{
			doGetLinks(map,up,j,links,w,h);return;
		}else if(min==map[i][left])
		{
			doGetLinks(map,i,left,links,w,h);return;
		}else if(min==map[i][right])
		{
			doGetLinks(map,i,right,links,w,h);return;
		}else
		{
			doGetLinks(map,down,j,links,w,h);return;
		}
	}

}
int main()
{
	int n,m;
	int h,w,t;
	vector<vector<int> > map;
	vector<int> temp;
	pair<int,int> p;
	vector<pair<int,int> > links;
	fstream in("B-small-attempt0.in",fstream::in),out("out.out",fstream::out);
	if(!in){
		cerr<<"read error"<<endl;return 1;
	}
	if(!out){
		cerr<<"write error"<<endl;return 1;
	}
	in>>n;
	m=n;
	while(n--)
	{
		in>>h>>w;		
		for(int i=0;i<h;i++)
		{
			temp.clear();
			for(int j=0;j<w;j++)
			{
				in>>t;
				temp.push_back(t);
			}
			map.push_back(temp);
		}
		/*for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
				cout<<map[i][j]<<" ";
			cout<<endl;
		}
		cout<<endl;*/
		
		//get links
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				doGetLinks(map,i,j,links,w,h);
				/*int left,right,up,down;
				if(j==0)
					left=0;
				else 
					left=j-1;
				
				if(j==w-1)
					right=w-1;
				else
					right=j+1;

				if(i==0)
					up=0;
				else
					up=i-1;

				if(i==h-1)
					down=h-1;
				else
					down=i+1;

				
				if(map[i][j]<=map[up][j]&&map[i][j]<=map[down][j]&&map[i][j]<=map[i][left]&&map[i][j]<=map[i][right])
				{
					p.first=i;
					p.second=j;
					links.push_back(p);
				}*/
			}
		}
		/*for(int i=0;i<links.size();i++)
			cout<<map[links[i].first][links[i].second]<<" ";*/
		out<<"Case #"<<m-n<<":"<<endl;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
				doPaint(map,i,j,links,w,h,out);
			out<<endl;
		}
		//cout<<endl;
		links.clear();
		temp.clear();
		map.clear();
		
	}
	in.close();
	out.close();
	return 0;
}