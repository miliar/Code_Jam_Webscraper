#include <iostream>

using namespace std;

struct xyz{char q;char f;char t;}mc[50],md[50];
int sc,sd,se;

string st,tmxy,str;
int n,i,j,z,zb;
char klc;
int cas=1;

int cheakm(char q,char f,int m,char &t)
{

if(m==0)
{
for(int i=0;i<sc;i++)
	if((mc[i].q==q &&mc[i].f==f)||(mc[i].q==f &&mc[i].f==q))
	{t=mc[i].t;return 1;}
}
if(m==1)
{
for(int i=0;i<sd;i++)
	if((md[i].q==q &&md[i].f==f)||(md[i].q==f &&md[i].f==q))
	{t='a';return 1;}
}

return 0;
}

void casen(string str)
{
string rez;
for(int i=0;i<str.size();i++)
	{rez+=str[i];if(i!=str.size()-1)rez+=", ";}
cout<<"Case #"<<cas<<": ["<<rez<<"]"<<endl;
cas++;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>n;
	for(i=0;i<n;i++)
	{
		st="";
		cin>>sc;
		for(j=0;j<sc;j++)
		{
		cin>>tmxy;
		mc[j].q=tmxy[0];
		mc[j].f=tmxy[1];
		mc[j].t=tmxy[2];
		}
		cin>>sd;
		for(j=0;j<sd;j++)
		{
		cin>>tmxy;
		md[j].q=tmxy[0];
		md[j].f=tmxy[1];
		}
		cin>>se>>str;
			for(j=0;j<se;j++)
			{
				zb=0;
			if(st.size()>0)
			if(!cheakm(st[st.size()-1],str[j],0,klc))
			for(z=0;z<st.size();z++)
			{
				if(cheakm(st[z],str[j],1,klc))
				{zb=1;break;}
			}
				if(zb){st="";continue;}
			if(st.size()!=0){
				if(cheakm(st[st.size()-1],str[j],0,klc))st[st.size()-1]=klc;
			else  st+=str[j];}
			else st+=str[j];
			}
		casen(st);		
	}
	return 0;
}