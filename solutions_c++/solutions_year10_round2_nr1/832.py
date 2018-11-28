#include<iostream>
#include<algorithm>
using namespace std;

char p[205][105];
char q[205];

char q1[205];

int main()
{
	int t,n,m,i,j,num,k,len1,len2,s,sum,mm=1,kk,ll;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		sum=0;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",&p[i]);
			len1=strlen(p[i]);
			p[i][len1++]='/';
			p[i][len1]='\0';
		}
	//	cout<<p[0][0]<<"ccc"<<endl;
	
		for(kk=0;kk<n;kk++)
			for(ll=kk+1;ll<n;ll++)
			{
				if(strcmp(p[kk],p[ll])>0)
				{
					strcpy(q1,p[kk]);
					strcpy(p[kk],p[ll]);
					strcpy(p[ll],q1);
				}
			}
		//cout<<p[0]<<endl;
		for(i=0;i<m;i++)
		{
			scanf("%s",&q);
			num=20000;
			len2=strlen(q);
			q[len2++]='/';
			q[len2]='\0';
			for(j=n-1;j>=0;j--)	
			{
				s=0;
				len1=strlen(p[j]);
			//	cout<<p[j]<<"qwqw  ";
				len2=strlen(q);
				for(k=0;k<len2;k++)
				{
					if(p[j][k]!=q[k])break;
				}
				//cout<<p[j]<<"qwqw  "<<q[0]<<endl;
			//	cout<<k<<endl;
				for(;k<len2;k++)
				{
					if(q[k]=='/')s++;
				}
			//	cout<<s<<endl;
				//cout<<s<<endl;
				if(s<num)num=s;
			}
			if(n==0)
			{
				s=0;
				len2=strlen(q);
				for(k=1;k<len2;k++)
				{
					if(q[k]=='/')s++;
				}
				if(s<num)num=s;
			}
			if(num!=0)
			{
				sum+=num;
				//cout<<num<<"aaaa"<<endl;
				strcpy(p[n++],q);
				for(kk=0;kk<n;kk++)
			for(ll=kk+1;ll<n;ll++)
			{
				if(strcmp(p[kk],p[ll])>0)
				{
					strcpy(q1,p[kk]);
					strcpy(p[kk],p[ll]);
					strcpy(p[ll],q1);
				}
			}
			//	for(k=0;k<n;k++)
				//	cout<<p[k]<<endl;
			}
		}
		printf("Case #%d: %d\n",mm++,sum);
	}
	return 0;
}
