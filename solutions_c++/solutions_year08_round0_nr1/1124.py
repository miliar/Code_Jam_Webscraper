#include <iostream>
#include <string>
#include <map>
using namespace std;

map<string, int> smap;

#define SMAX 100
#define QMAX 1000

int tbl[SMAX][QMAX+1];
int qlist[QMAX];

int main()
{
	int cc;
	cin>>cc;
	for(int ci=1;ci<=cc;ci++)
	{
		int s,q;
		int i,j,k;
		string str;
		cin>>s;
		cin.ignore();
		smap.clear();
		for(i=0;i<s;i++)
		{
			getline(cin,str);
			smap[str]=i;
		}

		cin>>q;
		cin.ignore();
		for(j=0;j<q;j++)
		{
			getline(cin,str);
			qlist[j]=smap[str];
		}

		for(i=0;i<s;i++) tbl[i][q]=0;

		int t;
		for(j=q-1;j>=0;j--)
			for(i=0;i<s;i++)
			{
				tbl[i][j]=q+1;
				for(k=0;k<s;k++)
				{
					if(qlist[j]==k) continue;
					t=tbl[k][j+1];
					if(k!=i) t++;
					if(t<tbl[i][j]) tbl[i][j]=t;
				}
			}

		t=q+1;
		for(i=0;i<s;i++)
		{
			if(tbl[i][0]<t) t=tbl[i][0];
		}

		cout<<"Case #"<<ci<<": "<<t<<endl;
	}

	return 0;
}
