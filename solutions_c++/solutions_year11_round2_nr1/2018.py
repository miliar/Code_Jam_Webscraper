#include <stdio.h>
double wp[105],owp[105],oowp[105];
char data[105][105];
double fz[105],fm[105];
double ofz[105][105],ofm[105],ooxx[105];
int main ()
{
	int cas,ca=1,n,i,j;
	double fenzi,fenmu;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",&data[i]);
		for(i=0;i<n;i++)
		{
			fenzi=fenmu=0;
			for(j=0;j<n;j++)
			{
				if(data[i][j]=='1')
				{
					fenzi+=1;
					fenmu+=1;
				}
				if(data[i][j]=='0')
					fenmu+=1;
			}
			fz[i]=fenzi;
			fm[i]=fenmu;
			wp[i]=fenzi/fenmu;
		}
		int num;
		double tot;
		for(i=0;i<n;i++)//计算第i个的owp
		{
			num=0;
			tot=0;
			for(j=0;j<n;j++)
			{
				if(data[i][j]=='1')//i个j比了,i赢了,j输了,剔除掉后，分母减1
				{
					tot+=(fz[j])/(fm[j]-1);
					ofz[i][j]=(fz[j]-1)/(fm[j]-1);//i的owp里的j的权重
					num++;
				}
				if(data[i][j]=='0')
				{
					tot+=(fz[j]-1)/(fm[j]-1);
					ofz[i][j]=(fz[j])/(fm[j]-1);
					num++;
				}
			}
			ofm[i]=num;
			ooxx[i]=tot;
			owp[i]=tot/num;
		}
		for(i=0;i<n;i++)//剔除i,计算第i个的oowp
		{
			num=0;
			tot=0;
			for(j=0;j<n;j++)
			{
				if(data[i][j]!='.')//i和j有比赛，
				{
					//tot+=(ooxx[j]-ofz[j][i])/(ofm[j]-1);
					tot+=owp[j];
					num++;
				}
			}
			oowp[i]=tot/num;
		}
		printf("Case #%d:\n",ca);
		for(i=0;i<n;i++)
		{
			printf("%.8lf\n",wp[i]/4+owp[i]/2+oowp[i]/4);
		}






	}
}