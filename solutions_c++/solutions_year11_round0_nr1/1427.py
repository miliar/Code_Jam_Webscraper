#include "iostream"
#include "string"

using namespace  std;

int n;
char color[200];
int id[200];
int cnt=0;
int oid,bid;
int odir,bdir;

void input()
{
	cin>>n;
	for(int i=0;i<n;++i)
	{
		cin>>color[i]>>id[i];
	}
}

void getDir(int start)
{
	odir=-2;
	bdir=-2;
	for(int i=start;i<n;++i)
	{
		if(color[i]=='O')
		{
			if(id[i]>oid)
				odir=1;
			else if(id[i]<oid)
				odir=-1;
			else
				odir=0;
			break;
		}
	}
	for(int i=start;i<n;++i)
	{
		if(color[i]=='B')
		{
			if(id[i]>bid)
				bdir=1;
			else if(id[i]<bid)
				bdir=-1;
			else
				bdir=0;
			break;
		}
	}
}
void work()
{
	input();

	cnt=0;
	oid=1;bid=1;

	getDir(0);

	int curId=0;
	while(curId<n)
	{
	//	cout<<cnt<<": "<<oid<<" "<<bid<<" "<<odir<<" "<<bdir<<endl;
		cnt++;
		if(color[curId]=='O')
		{
			if(odir==0)
			{
				curId++;
				if(bdir==1)
					bid++;
				else if(bdir==-1)
					bid--;
			}
			else if(odir==-1)
			{
				oid--;
				if(bdir==1)
					bid++;
				else if(bdir==-1)
					bid--;
			}
			else if(odir==1)
			{
				oid++;
				if(bdir==1)
					bid++;
				else if(bdir==-1)
					bid--;
			}
		}
		else if(color[curId]=='B')
		{
			if(bdir==0)
			{
				curId++;
				if(odir==1)
					oid++;
				else if(odir==-1)
					oid--;
			}
			else if(bdir==-1)
			{
				bid--;
				if(odir==1)
					oid++;
				else if(odir==-1)
					oid--;
			}
			else if(bdir==1)
			{
				bid++;
				if(odir==1)
					oid++;
				else if(odir==-1)
					oid--;
			}
		}
		getDir(curId);
	}
	cout<<cnt<<endl;
}


int main()
{
	freopen("a.txt","r",stdin);
	freopen("a.out.txt","w",stdout);

	int cs;
	cin>>cs;
	for(int i=1;i<=cs;++i)
	{
		cout<<"Case #"<<i<<": ";
		work();
	}
}