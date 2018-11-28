#include<iostream>
#include<fstream>
#include<cstring>
#include<map>
using namespace std;
#define N 100000
struct node
{
	char name[101];
	int child[1000];
	int counts;
}dirs[N];
int top=0;
int counts=0;
int new_node(char name[101],int ne)
{
	int re=top;
	memcpy( dirs[re].name , name,100*sizeof(char));
	memset(dirs[re].child,0,sizeof(dirs[re].child));
	dirs[re].counts=0;
	top++;
	if(ne)counts++;
	return re;
}
void init()
{
	memcpy(dirs[0].name,"root",sizeof("root"));
	memset(dirs[0].child,0,sizeof(dirs[0].child));
	counts=0;
	top=1;
}
void add_aline(char *name,int ne)
{
	int i=0;
	int l=strlen(name);
	char tem[101];
	int root=0;
	while(i<l)
	{
		if(name[i]=='/')
		{
			i++;
			int s=0;
			while(name[i]!='/')
			{
				tem[s++]=name[i++];
				if(name[i]==0)
					break;
			}
			tem[s]=0;
			bool f=false;
			for(int j=0;j<dirs[root].counts;j++)
			{
				int p=dirs[root].child[j];
				if(strcmp(tem,dirs[p].name)==0)
				{
					root=p;
					f=true;
					break;
				}
			}
			if(!f)
			{
				int r=new_node(tem,ne);
				dirs[root].child[dirs[root].counts++]=r;
				root=r;
			}
		}
	}


}


int main()
{
    freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A.txt","w",stdout);
   int cases=0;
   int T,n,m;
   cin>>T;
   while(T-->0)
   {
	   cases++;
	   memset(dirs,0,sizeof(dirs));
	   init();
	   cin>>n>>m;
	   for(int i=0;i<n;i++)
	   {	
		   char tem[102];
		   cin>>tem;
		   add_aline(tem,0);
	   }
	   for(int i=0;i<m;i++)
	   {
		   char tem[102];
		   cin>>tem;
		   add_aline(tem,1);
	   }
	   printf("Case #%d: %d\n",cases,counts);
	   
   }




	return 0;
}