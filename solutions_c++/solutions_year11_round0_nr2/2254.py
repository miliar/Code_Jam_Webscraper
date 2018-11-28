#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
int n;
char a[123],mat1[212][212],mat2[212][212];
void cl()
{
	if(n<2)return ;
	if(mat1[a[n-2]][a[n-1]])
	{
		a[n-2]=mat1[a[n-2]][a[n-1]];
		n--;
	}
	for(int i=0;i<n-1;i++)
	{
		if(mat2[a[i]][a[n-1]])
		{
			n=0;
			return ;
		}
	}

}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ts;
	cin>>ts;
	for(int cas=1;cas<=ts;cas++)
	{
		memset(mat1,0,sizeof(mat1));
		memset(mat2,0,sizeof(mat2));
		cin>>n;
		while(n--)
		{
			char a,b,c;
			cin>>a>>b>>c;
			mat1[a][b]=mat1[b][a]=c;
		}
		cin>>n;
		while(n--)
		{
			char a,b;
			cin>>a>>b;
			mat2[a][b]=mat2[b][a]=1;
		}
		n=0;
		int m;
		cin>>m;
		while(m--)
		{
			cin>>a[n++];
			cl();
		//	for(int i=0;i<n;i++)cout<<a[i];cout<<endl;
		}
		printf("Case #%d: [",cas);
		for(int i=0;i<n;i++)
		{
			if(i)cout<<", ";
			cout<<a[i];
		}
		cout<<"]\n";
	}
}