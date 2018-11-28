#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
class wNode
{
public:
	wNode *p[26];
	wNode()
	{
		int i;
		for(i=0;i<=25;i++)p[i]=NULL;
	}
};
class BNode
{
public:
	int a[26];
	int ei;
	BNode()
	{
		int i;
		for(i=0;i<=25;i++)a[i]=-1;
		ei=-1;
	}
};
wNode w;
BNode b[15];
int L,N,res;
void go(int k,wNode *p)
{
	int i,id;
	if(k==L)
	{
		res++;
	}
	else
	{
		for(i=0;i<=b[k].ei;i++)
		{
			id=b[k].a[i];
			if(p->p[id]!=NULL)
			go(k+1,p->p[id]);
		}
	}
}
int main()
{
	int i,j,k,id,ti,D;
	wNode *pw;
	char c;
	fin>>L>>D>>N;
	//读入字典树w
	for(i=1;i<=D;i++)
	{
		pw=&w;
		for(j=1;j<=L;j++)
		{
			fin>>c;
			id=c-'a';
			if(pw->p[id]!=NULL)
				pw=pw->p[id];
			else
			{
				pw->p[id]=new wNode;
				pw=pw->p[id];
			}
		}
	}





	//对给case处理:
	for(k=1;k<=N;k++)
	{

		res=0;


		for(i=0;i<=L-1;i++)b[i].ei=-1;

		for(i=0;i<=L-1;i++)
		{
			fin>>c;
			if(c=='(')
			{
				fin>>c;
				while(c!=')')
				{
					id=c-'a';
					b[i].ei++;
					ti=b[i].ei;
					b[i].a[ti]=id;
					fin>>c;
				}
			}
			else
			{
				id=c-'a';
				b[i].a[0]=id;
				b[i].ei=0;
			}
		}



		id=b[0].a[0];
		go(0,&w);
		fout<<"Case #"<<k<<": "<<res<<endl;
	}
	return 0;
}
