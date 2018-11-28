#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
int cc=1,t,h1,h2,n,nm[101];
char m1[101][101];
double wpm[101],owpm[101],oowpm[101];
int main(){
	freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(h1=0;h1<n;h1++)
			for(h2=0;h2<n;h2++)
				cin>>m1[h1][h2];
		for(h1=0;h1<n;h1++)
		{
			wpm[h1]=0;
			nm[h1]=0;
			for(h2=0;h2<n;h2++)
				if(m1[h1][h2]=='0')
				{
					nm[h1]++;
				}
				else if(m1[h1][h2]=='1')
				{
					wpm[h1]++;
					nm[h1]++;
				}
			wpm[h1]/=nm[h1];
		}
		for(h1=0;h1<n;h1++)
		{
			owpm[h1]=0;
			for(h2=0;h2<n;h2++)
				if(m1[h1][h2]=='0')
				{
					owpm[h1]+=(wpm[h2]*nm[h2]-1)/(nm[h2]-1);
				}
				else if(m1[h1][h2]=='1')
				{
					owpm[h1]+=(wpm[h2]*nm[h2])/(nm[h2]-1);
				}
			owpm[h1]/=nm[h1];
		}
		printf("Case #%d:\n",cc++);
		for(h1=0;h1<n;h1++)
		{
			oowpm[h1]=0;
			for(h2=0;h2<n;h2++)
				if(m1[h1][h2]!='.')
					oowpm[h1]+=owpm[h2];
			oowpm[h1]/=nm[h1];
			printf("%.10lf\n",0.25*wpm[h1]+0.5*owpm[h1]+0.25*oowpm[h1]);
		}
	}
}
