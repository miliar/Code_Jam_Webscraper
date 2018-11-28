#include <iostream>
#include <string>
using namespace std;

int di[]={-1,0,0,1,1,-1,1,-1};
int dj[]={0,-1,1,0,1,-1,-1,1};

string g[4];
bool check(int i, int j, int k)
{
		if (g[i][j]=='.'||g[i][j]=='T')
				return false;
		char c=g[i][j];
		bool T=false;
		for (int t=0;t<3;t++)
		{
				i+=di[k];
				j+=dj[k];
				if (i<0||j<0||i>3||j>3)
								return false;
				if (g[i][j]==c)
								continue;
				if (g[i][j]=='T'&&!T) {
								T=true;
								continue;
				}
				return false;
		}
		return true;
}

int main() {
	int n;
	cin>>n;
	for (int cas=1;cas<=n;cas++)
	{
		for (int i=0;i<4;i++)
			cin>>g[i];
		cout<<"Case #"<<cas<<": ";
		int cnt=0;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++) {
				if (g[i][j]!='.')
					cnt++;
				for (int k=0;k<8;k++)
				{
						if (check(i,j,k)) {
				//				cout<<i<<" "<<j<<endl;
								if (g[i][j]=='X')
										cout<<"X won";
								else if (g[i][j]=='O')
										cout<<"O won";
								goto lab;
						}
				}
			}
		if (cnt==16)
				cout<<"Draw";
		else
				cout<<"Game has not completed";
lab:
		cout<<endl;
	}
}
