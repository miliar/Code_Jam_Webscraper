#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
struct node
{
	std::string str;
	node *nx[2];
	float p;
	node():str(std::string(""))
	{
		nx[0]=nx[1]=0;
	}
};
node *root;
std::string allowed_chars="1234567890()qwertyuiopasdfghjklzxcvbnm";
char gc()
{
	char c;
	do
	{
		c=getchar();
	}
	while(!std::binary_search(allowed_chars.begin(),allowed_chars.end(),c));
	return c;
}

void load(node *act)
{
	gc();
	scanf("%f",&act->p);
	char buff[64];
	buff[0]=gc();
	if(buff[0]==')')return;
	ungetc(buff[0],stdin);
	scanf("%s",&buff[0]);
	act->str=buff;
	act->nx[0]=new node;
	load(act->nx[0]);
	act->nx[1]=new node;
	load(act->nx[1]);
	gc();
}
std::vector<std::string> A;
float go(node *nd)
{
	if(nd==0)return 1;
	if(std::binary_search(A.begin(),A.end(),nd->str))
	{
		return nd->p*go(nd->nx[0]);
	}
	else
	{
		return nd->p*go(nd->nx[1]);
	}
}
int main()
{
	std::sort(allowed_chars.begin(),allowed_chars.end());
	int n,a,l,N;
	scanf("%d",&N);
	char buff[64];
	for(int i=1;i<=N;++i)
	{
		root=new node;
		scanf("%d",&l);
		load(root);
		scanf("%d",&a);
		printf("Case #%d:\n",i);
		while(a--)
		{
			A.clear();
			scanf("%s%d",buff,&n);
			A.resize(n);
			for(int j=0;j<n;++j)
			{
				scanf("%s",buff);
				A[j]=buff;
			}
			std::sort(A.begin(),A.end());
			printf("%.7f\n",go(root));
		}
	}
	return 0;
}

