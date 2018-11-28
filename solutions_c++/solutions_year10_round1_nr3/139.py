#include<iostream>
#include<string>
using namespace std;

int tx,a1,a2,b1,b2;
long long ans;
int x[1000001],y[1000001];

int main()
{
	string s="0",t="1",l="";
	while(l.length()<1000005){
		l=s+t;s=t;t=l;
	}
	x[0]=0;
	for(int i=1;i<=1000005;i++)
		y[i]=1000005;
	for(int i=1;i<=1000005;i++){
		x[i]=x[i-1]+l[i]-'0';
		y[x[i]]=i;
	}
	cin>>tx;
	for(int q=1;q<=tx;q++){
	ans=0;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for(int i=a1;i<=a2;i++){
			int c=x[i];
			if(c<b1)c=b1;
			int d=y[i];
			if(d>b2)d=b2;
			int e=d-c+1;
			if(e<0)e=0;
			ans+=(long long)(b2-b1+1-e);
		}
		cout<<"Case #"<<q<<": "<<ans<<endl;
	}

	return 0;
}
