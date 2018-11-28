#include <iostream>
#include <cmath>
#include <string>
using namespace std;

string C[50];
string D[50];

int main()
{
	//freopen("F:\\DownLoad\\B-large.in","r",stdin);
	//freopen("F:\\B-large.out","w",stdout);
	int t;
	cin>>t;
	for ( int k = 1; k <= t; k++ )
	{
		int c,d,n;
		string ans="";
		char base[110];
		cin>>c;
		for ( int i = 0; i < c; i++ )
			cin>>C[i];
		cin>>d;
		for ( int i = 0; i < d; i++ )
			cin>>D[i];
		cin>>n;
		cin>>base;
		for ( int i = 0; i < n; i++ )
		{
			
			ans += base[i];
			if ( ans.length()==1 )
				continue;
			string CC = "";
			CC += ans[ans.length()-2];
			CC += ans[ans.length()-1];
			string rCC = "";
			rCC += ans[ans.length()-1];
			rCC += ans[ans.length()-2];
			int flag=0;
			for ( int j = 0; j < c; j++ )
			{
				if ( C[j].find(CC)==0 || C[j].find(rCC)==0 )
				{
					ans.erase(ans.length()-2,2);
					ans += C[j][2];
					flag = 1;
					break;
				}
			}
			if ( flag )
				continue;
			for ( int l = 0; l < ans.length()-1; l++ )
			{
				string DD="";
				string rDD="";
				DD += ans[ans.length()-1];
				DD += ans[l];
				rDD += ans[l];
				rDD += ans[ans.length()-1];
				int mark = 0;
				for ( int j = 0; j < d; j++ )
				{
					if ( DD==D[j] || rDD==D[j] )
					{
						ans = "";
						mark = 1;
						break;
					}
				}
				if ( mark )
					break;
			}
		}
		cout<<"Case #"<<k<<": [";
		for ( int i = 0; i < ans.length(); i++ )
		{
			if ( i==0 )
				cout<<ans[i];
			else
				cout<<", "<<ans[i];
		}
		cout<<"]\n";
	}
}