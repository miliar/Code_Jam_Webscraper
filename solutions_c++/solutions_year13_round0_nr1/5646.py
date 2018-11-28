#include "iostream"
using namespace std;
string a,b,c,d;
bool kropka,tak;
int n,poz;
char pozz;
int main()
{
	ios_base::sync_with_stdio(0);
	cin>>n;
	
	for (int i=0; i<n; i++)
	{
		cin>>a>>b>>c>>d;
		kropka=false;
		pozz='e';
		poz=5;
		cout<<"Case #"<<i+1<<": ";
		
		
		for (int u=0; u<4; u++)
		{
			if (a[u]=='T')
			{
				pozz='a';
				poz=u;
				break;
			}
			else if (b[u]=='T')
			{
				pozz='b';
				poz=u;
				break;
			}
			else if (c[u]=='T')
			{
				pozz='c';
				poz=u;
				break;
			}
			else if (d[u]=='T')
			{
				pozz='d';
				poz=u;
				break;
			}
			if (a[u]=='.' || b[u]=='.' || c[u]=='.' || d[u]=='.') kropka=true;
		}
		
		tak=true;
		
		if (pozz=='a') a[poz]='X';
		else if (pozz=='b') b[poz]='X';
		else if (pozz=='c') c[poz]='X';
		else if (pozz=='d') d[poz]='X';
		
		//cout<<poz<<" "<<pozz<<"\n";
		
		//cout<<a[0]<<" "<<a[1]<<" "<<a[2]<<" "<<a[3]<<"\n";
		
		if (tak && a[0]=='X' && a[1]=='X' && a[2]=='X' && a[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		if (tak && b[0]=='X' && b[1]=='X' && b[2]=='X' && b[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		if (tak && c[0]=='X' && c[1]=='X' && c[2]=='X' && c[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		if (tak && d[0]=='X' && d[1]=='X' && d[2]=='X' && d[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[0]=='X' && b[0]=='X' && c[0]=='X' && d[0]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[1]=='X' && b[1]=='X' && c[1]=='X' && d[1]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[2]=='X' && b[2]=='X' && c[2]=='X' && d[2]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[3]=='X' && b[3]=='X' && c[3]=='X' && d[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[0]=='X' && b[1]=='X' && c[2]=='X' && d[3]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak && a[3]=='X' && b[2]=='X' && c[1]=='X' && d[0]=='X')
		{
			cout<<"X won\n";
			tak=false;
		}
		
		if (tak)
		{
			if (pozz=='a') a[poz]='O';
			else if (pozz=='b') b[poz]='O';
			else if (pozz=='c') c[poz]='O';
			else if (pozz=='d') d[poz]='O';
			
			if (tak && a[0]=='O' && a[1]=='O' && a[2]=='O' && a[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			if (tak && b[0]=='O' && b[1]=='O' && b[2]=='O' && b[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			if (tak && c[0]=='O' && c[1]=='O' && c[2]=='O' && c[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			if (tak && d[0]=='O' && d[1]=='O' && d[2]=='O' && d[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[0]=='O' && b[0]=='O' && c[0]=='O' && d[0]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[1]=='O' && b[1]=='O' && c[1]=='O' && d[1]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[2]=='O' && b[2]=='O' && c[2]=='O' && d[2]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[3]=='O' && b[3]=='O' && c[3]=='O' && d[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[0]=='O' && b[1]=='O' && c[2]=='O' && d[3]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
			
			if (tak && a[3]=='O' && b[2]=='O' && c[1]=='O' && d[0]=='O')
			{
				cout<<"O won\n";
				tak=false;
			}
		}
		if (kropka && tak) cout<<"Game has not completed\n";
		else if (tak) cout<<"Draw\n";
	}
	
	return 0;
}