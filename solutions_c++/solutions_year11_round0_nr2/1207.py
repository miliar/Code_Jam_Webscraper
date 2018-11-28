//In the name of Allah
//
//
#include <iostream>
#include <cstring>
using namespace std;
#define val(a) (((a))-'A')
const int MN=1000;
char list[MN];
int p=0;
int n,t;
bool con[30][30];
char cr[30][30];
bool op[30][30];
int cunt[30];
int main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int c=0;c<t;c++)
	{
		memset(con,0,sizeof(con));
		memset(op,0,sizeof(op));
		memset(cunt,0,sizeof(cunt));
		p=0;
		int a;
		cin>>a;
		for (int i=0;i<a;i++)
		{
			char f,s,r;
			cin>>f>>s>>r;
			con[val(f)][val(s)]=con[val(s)][val(f)]=1;
			cr[val(f)][val(s)]=cr[val(s)][val(f)]=r;
		}
		cin>>a;
		for (int i=0;i<a;i++)
		{
			char f,s;
			cin>>f>>s;
			op[val(f)][val(s)]=op[val(s)][val(f)]=1;
		}
		cin>>a;
		for (int i=0;i<a;i++)
		{
			char f;
			cin>>f;
			list[p]=f;
			cunt[val(f)]++;
			p++;
			if (p>=2 && con[val(f)][val(list[p-2])])
			{
				cunt[val(list[p-1])]--;
				cunt[val(list[p-2])]--;
				list[p-2]=cr[val(f)][val(list[p-2])];
				cunt[val(list[p-2])]++;
				p--;
			}
			else
			{
				for (int j=0;j<30;j++) if (op[val(f)][j] && cunt[j])
				{
					p=0;
					memset(cunt,0,sizeof(cunt));
					break;
				}
			}
		}
		cout<<"Case #"<<c+1<<": [";
		for (int i=0;i<p;i++)
		{
			if (i!=0)
				cout<<", ";
			cout<<list[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
