//A
#include<iostream>
using namespace std;
#define N 10005
int d[N],l[N],n,S;
int found;
void solve(int k,int pre)
{
	int range;
	if(pre==-1) range=d[k];
	else
		range=min(d[k]-d[pre],l[k]);
	if(d[k]+range>=S) found=1;
	for(int i=k+1;i<n;i++)
	{
		if(found) return;
		if(d[i]<=d[k]+range)
			solve(i,k);
	}
}
int main(){
	int T;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			scanf("%d%d",&d[i],&l[i]);
		cin>>S;
		cout<<"Case #"<<cnt<<": ";
		found=0;
		solve(0,-1);
		if(found)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
