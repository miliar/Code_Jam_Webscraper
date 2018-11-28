#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#pragma comment(linker, "/STACK:167772160")
typedef long long int64;
using namespace std;
bool z[200][200];
char com[200][200];
int tes,o,i,j,c,d,n,p;
string s;
char list[1001];
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>tes;
	for(o=0;o<tes;o++)
	{
		memset(com,' ',sizeof(com));
		memset(z,false,sizeof(z));

		cin>>c;
		for(i=1;i<=c;i++){cin>>s;com[int(s[0])][int(s[1])]=s[2];com[int(s[1])][int(s[0])]=s[2];}
		cin>>d;
		for(i=1;i<=d;i++){cin>>s;z[int(s[0])][int(s[1])]=true;z[int(s[1])][int(s[0])]=true;}

		cin>>n;
		getline(cin,s);
		p=0;
		for(i=1;i<s.length();i++)
		{
			char v=s[i];
			//cout<<v<<" ";

			bool is;
			is=false;

			if(p>0)
			if(com[int(v)][int(list[p])]!=' ')is=true;

			if(is)
			{
				list[p]=com[int(v)][int(list[p])];
				/*com[int(v)][int(list[p])]=' ';
				com[int(list[p])][int(v)]=' ';
				z[int(v)][int(list[p])]=true;
				z[int(v)][int(list[p])]=true;
				*/
			}else
			{
				int w=0;
				for(j=1;j<=p;j++)if(z[int(v)][int(list[j])]==true)w++;

				if(w>0)p=0;else
				{
					p++;list[p]=v;
				}
			}
		}

		cout<<"Case #"<<o+1<<": [";
		if(p==0)cout<<"]"<<endl;else
		{
			cout<<list[1];
			for(i=2;i<=p;i++)cout<<", "<<list[i];
			cout<<"]"<<endl;
		}
	}
}