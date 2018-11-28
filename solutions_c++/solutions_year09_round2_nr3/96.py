#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

#define valid(i,j) (i>=0 && i<W && j>=0 && j<W)

string Arr[25][25][1000];
int xx[]={0,0,-1,+1},yy[]={-1,+1,0,0};
int main(){
	int t;
	scanf("%d",&t);
	for (int kase = 1; kase <= t; ++ kase) {
		cout<<"Case #"<<kase<<":\n";
		set<pair<pair<int,string>,pair<int,pair<int,int> > > > S;
		int W,Q;
		cin>>W>>Q;
		char M[100][100];
		for(int i=0;i<W;i++)
			for(int j=0;j<W;j++)
				for(int k=0;k<1000;k++)
					Arr[i][j][k]="";
		for(int i=0;i<W;i++)
			for(int j=0;j<W;j++)
			{
				cin>>M[i][j];
				if(M[i][j]>='0' && M[i][j] <='9')
				{
					string tmp="";tmp+=(M[i][j]);
					S.insert(make_pair(make_pair(1,tmp),make_pair(M[i][j]-'0',make_pair(i,j))));
					Arr[i][j][M[i][j]-'0'+500]=M[i][j];
				}
			}
		while(!S.empty())
		{
			pair<pair<int,string>,pair<int,pair<int,int> > > tmp = *(S.begin());
			S.erase(S.begin());
			int sum=tmp.second.first;
			int x=tmp.second.second.first,y=tmp.second.second.second;
			string str=tmp.first.second;int len=tmp.first.first;
			for(int i=0;i<4;i++)
			{
				int nx=x+xx[i],ny=y+yy[i];
				int nsum;
				string nstring;
				if(valid(nx,ny))
				{
					char ch=str[str.size()-1];
					if(ch=='+'||ch=='-')
					{
						nsum=(ch=='+')?(sum+M[nx][ny]-'0'):(sum-(M[nx][ny]-'0'));
						if(nsum>300 || nsum<-300)
							continue;
						nstring=str+M[nx][ny];
						if(Arr[nx][ny][nsum+500]=="" || Arr[nx][ny][nsum+500].length()>=len+1)
						{
							if(Arr[nx][ny][nsum+500].length() == len+1 && Arr[nx][ny][nsum+500] < nstring)continue;
							if(Arr[nx][ny][nsum+500]!="")
								S.erase(S.find(make_pair(make_pair(Arr[nx][ny][nsum+500].length(),Arr[nx][ny][nsum+500]),make_pair(nsum,make_pair(nx,ny)))));
							Arr[nx][ny][nsum+500]=nstring;
							S.insert(make_pair(make_pair(len+1,nstring),make_pair(nsum,make_pair(nx,ny))));
						}
					}
					else
					{
						nsum=sum;
						nstring=str+M[nx][ny];
						if(Arr[nx][ny][nsum+500]=="" || Arr[nx][ny][nsum+500].length()>=len+1)
						{
							if(Arr[nx][ny][nsum+500].length() == len+1 && Arr[nx][ny][nsum+500] < nstring)continue;
							if(Arr[nx][ny][nsum+500]!="")
								S.erase(S.find(make_pair(make_pair(Arr[nx][ny][nsum+500].length(),Arr[nx][ny][nsum+500]),make_pair(nsum,make_pair(nx,ny)))));
							Arr[nx][ny][nsum+500]=nstring;
							S.insert(make_pair(make_pair(len+1,nstring),make_pair(nsum,make_pair(nx,ny))));
						}
					}
				}
			}

		}
		int query;
		for(int i=0;i<Q;i++)
		{
			cin>>query;
			string ans="";
			for(int j=0;j<W;j++)
				for(int k=0;k<W;k++)
					if(Arr[j][k][query+500]!="")
					{
						if(ans==""||(ans.length()>Arr[j][k][query+500].length()||(ans.length()==Arr[j][k][query+500].length() && ans>Arr[j][k][query+500])))
							ans=Arr[j][k][query+500];
					}
			cout<<ans<<endl;
		}
	}
	return 0;
}

