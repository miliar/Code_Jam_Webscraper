#include <stdio.h>
int a[105],b[105],an,bn;
bool sx[105];//˳��
char str[10];
int main ()
{
	int cas,ca,n,i,x,ans,s1,s2,t1,t2,n1,n2;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		an=bn=ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",&str,&x);
			if(str[0]=='O')
			{
				sx[i]=0;
				a[an++]=x;
			}
			else
			{
				sx[i]=1;
				b[bn++]=x;
			}
		}
		s1=s2=1;//���Ƕ���1
		n1=n2=0;//���Ƕ�Ŀ�������±�
		t1=a[n1];
		t2=b[n2];
		for(i=0;i<n;i++)
		{
			if(sx[i]==0)//a��
			{
				while(s1!=t1)//�ƶ�
				{
					ans++;
					if(s1<t1)
						s1++;
					if(s1>t1)
						s1--;
					if(s2<t2)
						s2++;
					if(s2>t2)
						s2--;
				}
				//վ����
				ans++;//��ť
				n1++;
				t1=a[n1];
				if(s2<t2)
					s2++;
				if(s2>t2)
					s2--;
			}
			else//b��
			{
				while(s2!=t2)//�ƶ�
				{
					ans++;
					if(s1<t1)
						s1++;
					if(s1>t1)
						s1--;
					if(s2<t2)
						s2++;
					if(s2>t2)
						s2--;
				}
				//վ����
				ans++;//��ť
				n2++;
				t2=b[n2];
				if(s1<t1)
					s1++;
				if(s1>t1)
					s1--;	
			}
			
		}
		printf("Case #%d: %d\n",ca,ans);
		
		
		
	}
}