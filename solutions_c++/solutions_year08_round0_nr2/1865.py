#include<cstdio>
#include<cstring>
int t,na,nb,ra,rb,i,j,k,aux,m;
int ua[101],ub[101],a[102][2],b[102][2];
char s[100];
void sort(int a[101][2],int n)
{
	int i,j,aux;
	for(i=1;i<n;i++)
		for(j=i+1;j<=n;j++)
			if(a[i][0]>a[j][0])
			{
				aux=a[i][0];
				a[i][0]=a[j][0];
				a[j][0]=aux;
				aux=a[i][1];
				a[i][1]=a[j][1];
				a[j][1]=aux;
			}
}
int wait(int x)
{
	x=x+m;
	if(x%100>=60)
	{
		x+=100;
		x-=60;
	}
	return x;
}

void goa(int t,int i,int j);
void gob(int t,int i,int j);

void goa(int t,int i,int j)
{
	for(int k=i;k<=na;k++)
		if(ua[k]==0 && t<=a[k][0])
		{
			ua[k]=1;
			t=wait(a[k][1]);
			gob(t,k+1,j);
			return;
		}	
}
void gob(int t,int i,int j)
{
	for(int k=j;k<=nb;k++)
		if(ub[k]==0 && t<=b[k][0])
		{
			ub[k]=1;
			t=wait(b[k][1]);
			goa(t,i,k+1);
			return;
		}	
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		memset(ua,0,sizeof(ua));
		memset(ub,0,sizeof(ub));
		scanf("%d",&m);
		scanf("%d %d ",&na,&nb);
		for(i=1;i<=na;i++)
		{
			gets(s);
			aux=(s[0]-'0')*1000+(s[1]-'0')*100+(s[3]-'0')*10+s[4]-'0';
			a[i][0]=aux;
			aux=(s[6]-'0')*1000+(s[7]-'0')*100+(s[9]-'0')*10+s[10]-'0';
			a[i][1]=aux;
		}
		for(i=1;i<=nb;i++)
		{
			gets(s);
			aux=(s[0]-'0')*1000+(s[1]-'0')*100+(s[3]-'0')*10+s[4]-'0';
			b[i][0]=aux;
			aux=(s[6]-'0')*1000+(s[7]-'0')*100+(s[9]-'0')*10+s[10]-'0';
			b[i][1]=aux;
		}
		sort(a,na);
		sort(b,nb);
		i=1;j=1;
		a[na+1][0]=2400;
		b[nb+1][0]=2400;
		ra=rb=0;
		while(i<=na || j<=nb)
		{
			while(ua[i])i++;
			while(ub[j])j++;
			if(i>na && j>nb) break;
			if(a[i][0]<=b[j][0])
			{
				ua[i]=1;
				ra++;
				i++;
				gob(wait(a[i-1][1]),i,j);
			}
			else
			{
				ub[j]=1;
				rb++;
				j++;
				goa(wait(b[j-1][1]),i,j);
			}
		}
		printf("Case #%d: %d %d\n",k,ra,rb);
	}
	fclose(stdout);
	return 0;
}
