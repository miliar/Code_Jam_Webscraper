#include <stdio.h>

#define LEN 100
#define MAX 500

#define tt(x) (s[x]-'0')

int time(char *s)
{
	return (tt(0)*10+tt(1))*60+tt(3)*10+tt(4);
}

int sort(int a[], int n)
{
	int t;
	
	for(int i=0;i<n;i++)
		for(int j=0;j<i;j++)
			if(a[i]<a[j])
			{
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
}

int main()
{
	int n;
	scanf("%d ",&n);

	for(int i=1;i<=n;i++)
	{
		int tt,na,nb;
		scanf("%d %d %d ",&tt,&na,&nb);
		
		int a1[MAX],a2[MAX],b1[MAX],b2[MAX];

		for(int j=0;j<na;j++)
		{
			char s[LEN], t[LEN];
			scanf("%s %s ",s,t);
			a1[j]=time(s);
			a2[j]=time(t)+tt;
		}

		for(int j=0;j<nb;j++)
		{
			char s[LEN], t[LEN];
			scanf("%s %s ",s,t);
			b1[j]=time(s);
			b2[j]=time(t)+tt;	
		}
		
		int cc[MAX*4],c=0;
		for(int j=0;j<na;j++)	cc[c++]=a1[j];
		for(int j=0;j<na;j++)	cc[c++]=a2[j];
		for(int j=0;j<nb;j++)	cc[c++]=b1[j];
		for(int j=0;j<nb;j++)	cc[c++]=b2[j];
		
		sort(a1,na);
		sort(a2,na);
		sort(b1,nb);
		sort(b2,nb);
		sort(cc,c);
		
		int aa[MAX], bb[MAX];
		int ax=0,bx=0,ay=0,by=0;
		int a1i=0,a2i=0,b1i=0,b2i=0;
		

		for(int j=0;j<c;j++)
		{

			
			if(a2[a2i]==cc[j] && a2i<na)
			{
				bx++;
				a2i++;
			}
			
						
			if(b2[b2i]==cc[j] && b2i<nb)
			{
				ax++;
				b2i++;
			}

			if(a1[a1i]==cc[j] && a1i<na)
			{
				if(ax==0)
					ay++;
				else
					ax--;
				a1i++;
			}

			if(b1[b1i]==cc[j] && b1i<nb)
			{
				if(bx==0)
					by++;
				else
					bx--;
				b1i++;
			}
		}
		
		printf("Case #%d: %d %d\n",i,ay,by);
		
			
	}

	return 0;
}
