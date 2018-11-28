#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<queue>
using namespace std;
struct node
{
	int x,y;
	int z;
};
bool operator<(const node&a,const node&b)
{
	if(a.x!=b.x)
		return a.x<b.x;
	if(a.y!=b.y)
		return a.y<b.y;
	return a.z<b.z;
}
struct node1
{
	int x;
	int c;//a->b
	int d;//arrive
};
bool operator<(const node1&a,const node1&b)
{
	if(a.x!=b.x)
		return a.x<b.x;
	return a.d>b.d;
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	//const int inf=1000000000;
	int zu;
	cin>>zu;
	int g=1;
	string s,t;
	while(zu--)
	{
		int m,n,k;
		cin>>k>>m>>n;
		vector<node>a(m+n);//,b(n);
		for(int i=0;i<m;i++)
		{
			cin>>s;
			a[i].x=((s[0]-'0')*10+s[1]-'0')*60+((s[3]-'0')*10+s[4]-'0');
			cin>>s;
			a[i].y=((s[0]-'0')*10+s[1]-'0')*60+((s[3]-'0')*10+s[4]-'0')+k;
			a[i].z=0;
		}
		for(int i=0;i<n;i++)
		{
			cin>>s;
			a[i+m].x=((s[0]-'0')*10+s[1]-'0')*60+((s[3]-'0')*10+s[4]-'0');
			cin>>s;
			a[i+m].y=((s[0]-'0')*10+s[1]-'0')*60+((s[3]-'0')*10+s[4]-'0')+k;
			a[i+m].z=1;
		}
		//sort(a.begin(),a.end());
		vector<node1> b(2*(m+n));
		for(int i=0;i<m+n;i++)
		{
			b[i].d=0;
			b[i+m+n].d=1;
			b[i].x=a[i].x;
			b[i+m+n].x=a[i].y;
			if(i<m)
				b[i].c='a',b[i+m+n].c='b';
			else
				b[i].c='b',b[i+m+n].c='a';

		}
		sort(b.begin(),b.end());
	//	for(int i=0;i<b.size();i++)cout<<b[i].x<<" "<<(char)b[i].c<<" "<<b[i].d<<endl;
		int x=0,y=0;
		int p=0,q=0;
		for(int i=0;i<b.size();i++)
		{
			if(b[i].d)
			{
				if(b[i].c=='a')
					x++;
				else
					y++;
			}
			else
			{
				if(b[i].c=='a')
				{
					if(x>0)
						x--;
					else
						p++;
				}
				else
				{
					if(y>0)
						y--;
					else
						q++;
				}
			}
		}
		cout<<"Case #"<<g++<<": "<<p<<" "<<q<<endl;
	}
}