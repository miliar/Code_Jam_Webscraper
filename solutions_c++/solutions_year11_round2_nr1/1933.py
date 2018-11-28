#include<iostream>
#include<cstring>
using namespace std;
double howmany(char*ch,char c)
{
	int n=0;
	int l=strlen(ch);
	int i;
	for(i=0;i<l;i++)
	{
		if(ch[i]==c) n++;
	}
	return (double)n;
}
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);

	int T;
	scanf("%d",&T);
	int i;
	double time=0.0;
	for(i=1;i<=T;i++)
	{
		int n;
		char ch[105][105];
		scanf("%d",&n);
		int j,k;
		for(j=0;j<n;j++)
		{
			scanf("%s",ch[j]);
		}
		double wp[105],owp[105],oowp[105];
		for(j=0;j<n;j++)
		{
			wp[j]=howmany(ch[j],'1')/(n-howmany(ch[j],'.'));
			//cout<<wp[j]<<endl;
		}
		for(j=0;j<n;j++)
		{
			int duishou=n-howmany(ch[j],'.');
			double po=0;
			for(k=0;k<n;k++)
			{
				if(k==j || ch[j][k]=='.') continue;
				int t,value=0,nn=0;
				for(t=0;t<n;t++)
				{
					if(ch[t][k]=='0' && t!=j) {value+=1;nn++;}
					else if(ch[t][k]=='1'&& t!=j){nn++;}
				}
				po+=(double)value/nn;
			}
			
			owp[j]=po/duishou;
			//cout<<owp[j]<<endl;
		}
		for(j=0;j<n;j++)
		{
			int duishou=n-howmany(ch[j],'.');
			double po=0;
			for(k=0;k<n;k++)
			{
				if(k==j || ch[j][k]=='.') continue;
				po+=owp[k];
			}
			
			oowp[j]=po/duishou;
			//cout<<oowp[j]<<endl;
		}















		cout<<"Case #"<<i<<":"<<endl;
		for(j=0;j<k;j++)
		{
			char buf[32] = "";
			sprintf(buf, "%.12f", 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
			while (buf[strlen(buf) - 1] == '0')
				buf[strlen(buf) - 1] = '\0';
			if	(buf[strlen(buf) - 1] == '.') buf[strlen(buf) - 1] = '\0';
			printf("%s\n", buf);
		}
			

	}

		
	
return 0;
}