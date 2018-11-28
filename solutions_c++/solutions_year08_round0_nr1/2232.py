#include<iostream>
using namespace std;
int main(void)
{
    int arr[1020][120];
    int n,iq,ans,mini;
    string s[120],q[1020];
    int t,i,j,k;
    cin>>t;
    int cas=1;
    while(t--)
    {
	cin>>n;
	getline(cin,s[0]);
	for(i=0;i<n;i++)
	    getline(cin,s[i]);
	cin>>iq;
	getline(cin,q[0]);
	for(i=0;i<iq;i++)
	    getline(cin,q[i]);
	for(i=0;i<iq;i++) for(j=0;j<n;j++) arr[i][j]=-1;
	ans=-1;
	if(iq==0){ cout<<"Case #"<<cas++<<": "<<0<<endl; continue; }
	for(i=0;i<n;i++)
	    if(s[i]!=q[0]) arr[0][i]=0;
	for(i=1;i<iq;i++)
	{
	    for(j=0;j<n;j++)
	    {
		if(s[j]==q[i])
		    continue;
		mini=1020;
		for(k=0;k<n;k++)
		    if(arr[i-1][k]>=0)
		    {
			if(k!=j) mini=min(mini,arr[i-1][k]+1);
			else mini=min(mini,arr[i-1][k]);
		    }
		arr[i][j]=mini;
	    }
	}
	for(i=0;i<n;i++)
	    if(ans==-1) ans=arr[iq-1][i];
	    else if(arr[iq-1][i]>=0) ans=min(ans,arr[iq-1][i]);
	cout<<"Case #"<<cas++<<": "<<ans<<endl; 
    }
    return 0;
}
