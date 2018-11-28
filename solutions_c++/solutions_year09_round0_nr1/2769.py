#include<iostream>
using namespace std;
int n,l,d;
int zhizhen;
struct node{
	char w[16];
	bool flag[16];
	bool pp;
}a[5005];
char p[999999];
int xx;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout); 
	cin>>l>>d>>n;
	int i,jishu,j,sum,len;
	for(i=0;i<d;i++)
	{
		cin>>a[i].w;
	}
	for(jishu=1;jishu<=n;jishu++)
	{
		cin>>p;
		xx=0;sum=0;
		len=strlen(p);
		for(i=0;i<d;i++) 
		{
			a[i].pp=1;
			for(j=0;j<l;j++)
				a[i].flag[j]=0;
		}
		zhizhen=0;
		for(i=0;i<len;i++)
		{
			if(xx==0&&p[i]=='(') {xx=1;continue;}
			else if(xx==0&&p[i]!='(') {
				for(j=0;j<d;j++) {
					if(a[j].pp==1){
						if(a[j].w[zhizhen]==p[i]) a[j].flag[zhizhen]=1;
						else a[j].pp=0;
					}
				}
				zhizhen++;
			}
			else if(xx==1&&p[i]==')') {
				for(j=0;j<d;j++)
				{
					if(a[j].flag[zhizhen]==0) a[j].pp=0;
				}
				zhizhen++;xx=0;
			}
			else if(xx==1&&p[i]!=')'){
				for(j=0;j<d;j++) {
					if(a[j].pp==1){
						if(a[j].w[zhizhen]==p[i]) a[j].flag[zhizhen]=1;
					}
				}
			}
		}
		for(i=0;i<d;i++)
		{
		if(a[i].pp==1) sum++;
		}
		cout<<"Case #"<<jishu<<": "<<sum<<endl;
	}
	return 0;
}