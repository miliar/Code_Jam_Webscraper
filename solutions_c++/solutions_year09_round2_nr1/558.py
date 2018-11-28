#include <iostream>
#include <string>
#include <stack>
using namespace std;
struct Point
{
	int dire;
	char str[100];
	double value;
	int left,Right,parent;
};
Point head[1000000];
int p;
int len;
void Process(char str[])
{
	int i;
	p = 0;
	stack<Point> st;
	for (i=0;i<len;i++)
	{
		if (str[i]=='(');
		else if (str[i]==')')
		{
			if (st.size()==1) break;
			Point a,b;
			a = st.top();
			st.pop();
			b = st.top();
			st.pop();
			if (b.left==-1){ b.left = a.dire;head[b.dire].left = a.dire;}
			else {b.Right = a.dire;head[b.dire].Right=a.dire;}
			st.push(b);
		}
		else
		{
			double re = 0;
			double ttt = 1;
			bool flag = false;
			while (str[i]>='0'&&str[i]<='9'||str[i]=='.')
			{
				if (str[i]=='.') flag = true;
				else
				{
					if (!flag) re = re*10 + str[i]-'0';
					else
					{
						re = re + ttt/10*(str[i]-'0');
						ttt /= 10;
					}
				}
				i++;
			}
			
			char  ss[100];
			ss[0] = '\0';
			int k = 0;
			while(str[i]>='a'&&str[i]<='z')
			{
				ss[k++] = str[i];
				i++;
			}
			ss[k] = '\0';
			Point a;
			a.dire = p;a.left=-1,a.Right = a.parent = -1;
			strcpy(a.str , ss);
			a.value = re;
			head[p++] = a;
			st.push(a);
			i--;
		}
	}
}
int main()
{
	freopen("B_small.in","r",stdin);
	freopen("tt.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int w=1;w<=T;w++)
	{
		printf("Case #%d:\n",w);
		int n,i;
		scanf("%d",&n);
		getchar();
		char tt[8005] = "";
		char str[1000];
		len = 0;
		while (n--)
		{
			gets(str);
			for (i=0;i<strlen(str);i++)
			{
				if (str[i]!=' ') tt[len++] += str[i];
			}
		}
		Process(tt);
		scanf("%d",&n);
		int m;
		char ff[100][100];
		while (n--)
		{
			scanf("%s",&str);
			scanf("%d",&m);
			for (i=0;i<m;i++)
				scanf("%s",&ff[i]);

			double p = head[0].value;
			int result = 0;
			while (head[result].Right!=-1)
			{
				for (i=0;i<m;i++)
				{
					if (strcmp(head[result].str,ff[i])==0) break;
				}
				if (i!=m)
				{
					 p *= head[head[result].left].value;
					 result = head[result].left;
				}
				else
				{
					p *= head[head[result].Right].value;
					result = head[result].Right;
				}
			}
			printf("%0.7lf\n",p);
		}
	}
}
