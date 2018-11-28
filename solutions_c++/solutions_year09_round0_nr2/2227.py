#include<iostream>
#include<vector>
#include<stack>
#include<limits>
using namespace std;
const int INF=1000000;
int H,W,X=1;
void DFS(vector<vector<int> >&R,vector<vector<char> >&ans,int i,int j);
void print(vector<vector<char> >&a)
{
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
			cout<<a[i+1][j+1]<<' ';
		cout<<endl;
	}
}
stack<pair<int,int> >S;
char C;
int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		C='a';
		cin>>H>>W;
		vector<vector<int> > range(H+2,vector<int>(W+2,INF));
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				cin>>range[i+1][j+1];
		vector<vector<char> > ans(H+2,vector<char>(W+2,'#'));
		ans[0][0]='a';
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				DFS(range,ans,i+1,j+1);
		cout<<"Case #"<<X<<':'<<endl;
		print(ans);
		X++;
	}
	return 0;
}

void DFS(vector<vector<int> >&R,vector<vector<char> >&ans,int i,int j)
{
	if(i>H || i<0 || j<0 || j>W || ans[i][j]!='#')
		return;
	//is a sink
	if(R[i][j]<=R[i-1][j] && R[i][j]<=R[i][j-1] && R[i][j]<=R[i+1][j] && R[i][j]<=R[i][j+1])
	{
		if(ans[i][j]=='#')
		{
			ans[i][j]=C;
			C++;
		}
		return;
	}
	else
	{
		pair<int,int> at(i,j),n(i-1,j),w(i,j-1),e(i,j+1),s(i+1,j);
		S.push(at);
		if(R[at.first][at.second]>R[n.first][n.second])
			at=n;
		if(R[at.first][at.second]>R[w.first][w.second])
			at=w;
		if(R[at.first][at.second]>R[e.first][e.second])
			at=e;
		if(R[at.first][at.second]>R[s.first][s.second])
			at=s;
		DFS(R,ans,at.first,at.second);
		pair<int,int> T=S.top();
		S.pop();
		ans[T.first][T.second]=ans[at.first][at.second];
		return;
	}
}
