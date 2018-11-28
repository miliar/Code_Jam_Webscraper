//Code Jam 2012 C 
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int digits(int n)
{
	int ret=1;
	while(n/10>0)
	{
		n/=10;
		ret++;
	}
	return ret;	
}

int gen_new_num(int n,int l,int k)
{
	int head,tail,tmp,s;
	tmp=s=1;
	for(int i=0;i<k;i++) tmp*=10;
	head=n%tmp;
	tail=n/tmp;
	for(int i=0;i<l;i++) s*=10;
	tmp=s/tmp;
	return head*tmp+tail;
}

int main(){
	int T,A,B,n,l,ans;
	int m[10];
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>A>>B;
		ans=0;
		for(int i=A;i<=B;i++)
		{
			l=digits(i);
			for(int j=0;j<l-1;j++)
				m[j]=gen_new_num(i,l,j+1);
			sort(m,m+l-1);
			for(int j=0;j<l-1;j++)
			{
				if(m[j]>i && m[j]<=B)
				{
					ans++;
					if(j>0 && m[j]==m[j-1]) ans--;
				}
			}
			
		}
		cout<<"Case #"<<cnt<<": "<<ans<<endl;
	}
	return 0;
}
 
