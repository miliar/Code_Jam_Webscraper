#include<iostream>
#include<string>
using namespace std;
string a[200];
int n;
double v_wp[200],v_owp[200],v_oowp[200];
double wp(int i)
{
	int j;
	if (v_wp[i]>-1) return v_wp[i];
	double tot=0,win=0;
	for(j=0;j<n;j++)
    {
		if (a[i][j]!='.') tot+=1;
		if (a[i][j]=='1') win+=1;
	}
	v_wp[i]=win/tot;
	return win/tot;
}
double to_wp(int i,int ii)
{
	int j;
	
	double tot=0,win=0;
	for(j=0;j<n;j++)
		if (j!=ii)
    {
		if (a[i][j]!='.') tot+=1;
		if (a[i][j]=='1') win+=1;
	}
    
	return win/tot;
}
double owp(int i)
{
  int j,jj,tot=0;
  double ans=0;
  	if (v_owp[i]>-1) return v_owp[i];
  for(j=0;j<n;j++)
  {
	  if (a[i][j]!='.')
	  {
		  tot++;
		  ans+=to_wp(j,i);
	  }
  }
  	v_owp[i]=ans/tot;
  return ans/tot;
}
double oowp(int i)
{
    int j,jj,tot=0;
  double ans=0;
  for(j=0;j<n;j++)
  {
	  if (a[i][j]!='.')
	  {
		  tot++;
		  ans+=owp(j);
	  }
  }
  return ans/tot;
}
double rpi(int i)
{
	return 0.25*wp(i)+0.50*owp(i)+0.25*oowp(i);
}
int main()
{
	int tcase,cas,i;
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	scanf("%d",&tcase);
	for(cas=1;cas<=tcase;cas++)
	{
		scanf("%d",&n);
		for(i=0;i<=n;i++)
		{
			v_wp[i]=-2;v_owp[i]=-2;v_oowp[i]=-2;
		}
		for(i=0;i<n;i++)
			cin>>a[i];
		printf("Case #%d:\n",cas);
		for(i=0;i<n;i++)
			printf("%.9lf\n",rpi(i));
	}
}