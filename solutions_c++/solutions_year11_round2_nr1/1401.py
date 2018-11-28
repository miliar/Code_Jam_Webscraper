#include<cstdio>
int main()
{
	int test,t;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		int num,total[1000]={0},played[1000]={0};
		char ch[110][110]={'\0'};
		long double wp[110]={0},op[110]={0},oop[110]={0};
		scanf("%d",&num);
		for(int i=0;i<num;i++)
			scanf("%s",ch[i]);
		for(int i=0;i<num;i++)
		{
			int val=0,c=0;
			for(int j=0;j<num;j++)
			{
				if(ch[i][j]=='1')
				{
					val++;
					c++;
				}
				else if(ch[i][j]=='0')
					c++;
			}
			wp[i]=(long double)val/c;
			total[i]=val;
			played[i]=c;
		}
		for(int i=0;i<num;i++)
		{
			int val=0;
			long double avg=0;
			for(int j=0;j<num;j++)
			{
				if(ch[i][j]!='.')
				{	
					val++;
					if(ch[i][j]=='1')
						avg=avg+((long double)(total[j])/(long double)(played[j]-1));
					else
						avg=avg+((long double)(total[j]-1)/(long double)(played[j]-1));
				}
			}
			op[i]=avg/val;
		}
		for(int i=0;i<num;i++)
		{
			int count=0;
			long double avg=0;
			for(int j=0;j<num;j++)
			{
				if(ch[i][j]!='.')
				{
					count++;
					avg+=op[j];
				}
			}
			oop[i]=avg/count;
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<num;i++)
		{
			printf("%.12Lf\n",.25*wp[i]+.5*op[i]+.25*oop[i]);
		}
	}
	return 0;
}
