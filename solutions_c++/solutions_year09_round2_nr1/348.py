#include<stdio.h>
#include<string.h>
struct node
{
    char feat[50];
    double p;
    int left;
    int right;
    int par;
}tree[50000];
char str[80000],temp[500],info[100][500];;
int stack[50000],rpl[50000],ti,tn,total,len,i,j,n,m;
void oper(int f,int t,int fa)
{
    int i,j,cur;
    double k;
    for (tree[total].p=0.0,i=f+1;str[i]!='.';i++)
        tree[total].p=tree[total].p*10.0+str[i]-'0';
    for (k=1.0,i++;str[i]>='0'&&str[i]<='9';i++)
    {
        k/=10.0;
        tree[total].p+=k*(str[i]-'0');
    }
    tree[total].par=fa;
    tree[total].left=tree[total].right=-1;
    if (fa!=-1)
    {
        if (tree[fa].left==-1) tree[fa].left=total;
        else tree[fa].right=total;
    }
    if (str[i]!=')')
    {
        for (j=0;str[i]>='a'&&str[i]<='z';j++,i++)
            tree[total].feat[j]=str[i];
        tree[total++].feat[j]=0;
		cur=total-1;
        oper(i,rpl[i],cur);
        oper(rpl[i]+1,t-1,cur);
    }
    else
    {
        tree[total++].feat[0]=0;
        return;
    }
}
double calc(int now)
{
	int i;
	if (tree[now].feat[0]==0) return tree[now].p;
	for (i=0;i<m;i++)
		if (!strcmp(info[i],tree[now].feat))
			break;
	if (i==m) return tree[now].p*calc(tree[now].right);
	else return tree[now].p*calc(tree[now].left);
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tn);
    for (ti=1;ti<=tn;ti++)
    {
        printf("Case #%d:\n",ti);
		scanf("%d\n",&n);
        len=0;
        stack[0]=0;
        for (i=0;i<n;i++)
        {
            gets(temp);
            for (j=0;temp[j];j++)
                if (temp[j]!=' ')
                {
                    str[len++]=temp[j];
                    if (temp[j]=='(') stack[++stack[0]]=len-1;
                    else if (temp[j]==')') rpl[stack[stack[0]--]]=len-1;
                }
        }
        str[len]=0;
        total=0;
        oper(0,len-1,-1);
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",temp);
			scanf("%d",&m);
			for (j=0;j<m;j++)
				scanf("%s",info[j]);
			printf("%lf\n",calc(0));
		}
    }
    return 0;
}
