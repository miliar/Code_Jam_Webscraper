#include <iostream>
#include <vector>
using namespace std;
const int _MAX = 101;
int T,H,W;
int Arr[_MAX][_MAX];
char ChArr[_MAX][_MAX];
bool FArr[_MAX][_MAX];
int R[]={-1,0,0,1};
int C[]={0,-1,1,0};
bool InRange(int x,int y)
{
	if(x<0||x>=H||y<0||y>=W)return false;
	return true;
}

void func(int x,int y,vector<pair<int,int> >& pArr,char& ch)
{
	//for(int i=0;i<H;++i){			for(int j=0;j<W;++j)			{				cout<<ChArr[i][j]<<' ';			}			cout<<endl;		}	cout<<"------------------"<<endl;
	int s=x,e=y,v=Arr[x][y];
	bool f = false;
	for(int i=0;i<4;++i)
	{
		int ss = R[i]+x;
		int ee = C[i]+y;
		if(InRange(ss,ee))
		{
			if(v > Arr[ss][ee])
			{
				s = ss;
				e = ee;
				v = Arr[ss][ee];
				f=true;
			}
		}
	}
	if(f)
	{
		pArr.push_back(make_pair<int,int>(s,e));
		if(FArr[s][e] && ch > ChArr[s][e])
			ch = ChArr[s][e];
		func(s,e,pArr,ch);
	}
	else
	{
		if(FArr[s][e] && ch > ChArr[s][e])
			ch = ChArr[s][e];
		else
			ChArr[s][e] = ch;
		FArr[s][e]=true;
		for(int i=0;i<pArr.size();++i)
		{
			ChArr[pArr[i].first][pArr[i].second] = ch;
			FArr[pArr[i].first][pArr[i].second]=true;
		}
		//ch+=1;
	}
}

int main(int argc, char *argv[])
{
	//FILE* ifp = freopen("Watersheds.in","r",stdin);
	FILE* ifp = freopen("B-large.in","r",stdin);
	FILE* ofp = freopen("B-large.out","w",stdout);
	cin>>T;
	for(int TC=0;TC<T;++TC)
	{
		cin>>H>>W;
		memset(FArr,0,sizeof(FArr));
		for(int i=0;i<H;++i)
		for(int j=0;j<W;++j)
		{
			cin>>Arr[i][j];
		}
		char ch='a';
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				if(!FArr[i][j])
				{
					vector<pair<int,int> >pArr;
					char chT = ch;
					pArr.push_back(make_pair<int,int>(i,j));
					func(i,j,pArr,chT);
					if(chT==ch)
						ch = ch+1;
				}
			}
		cout<<"Case #"<<TC+1<<":"<<endl;
		for(int i=0;i<H;++i)
		{
			for(int j=0;j<W;++j)
			{
				cout<<ChArr[i][j]<<' ';
			}
			cout<<endl;
		}
	}
}
