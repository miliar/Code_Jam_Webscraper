# include <iostream>

using namespace std;
int r,c;
char ch[64][64];

bool solve()
{
	cin>>r>>c;
	for(int i=0;i<r;++i)
		cin>>ch[i];

	int num=0;
	for(int i=0;i<r;++i)
		for(int j=0;j<c;++j)
			if(ch[i][j]=='#')
				++num;

	if(num%4 != 0)
		return false;

	for(int i=0;i<r;++i)
		for(int j=0;j<c;++j)
		{
			if(j<c-1 && i<r-1 && ch[i][j]=='#' && ch[i][j+1] =='#' && ch[i+1][j]=='#' && ch[i+1][j+1]=='#')
			{
				ch[i][j]='/';
				ch[i][j+1]='\\';
				ch[i+1][j]='\\';
				ch[i+1][j+1]='/';
				num-=4;
			}
		}

	if(num==0)
		return true;
	return false;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<":"<<endl;
		if(solve())
		{	
			for(int j=0;j<r;++j)
				cout<<ch[j]<<endl;
		}
		else
		{
			cout<<"Impossible\n";
		}
	}
	return 0;
}
