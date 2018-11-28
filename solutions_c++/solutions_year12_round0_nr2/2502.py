#include<iostream>

using namespace std;

int main ()
{
    int t,n,s,p,i,j,ans=0,temp,tempi;
    cin>>t;
    for ( j = 0; j < t ; j++ )
    {
    	cin>>n;
    	cin>>s;
	cin>>p;
    	ans=0;
    	//cout<<len<<endl<<endl;
	for ( i=0 ; i<n ; i++)
    	{
		cin>>temp;
		tempi=temp;
		if(temp>=0)
		{
		temp=temp-((3*p)-2);
		//cout<<temp<<"\t";
		if(temp>=0)
		ans++;
		if(temp<0 && s>0)
		if((tempi>=1 && temp>=-1) || (tempi>=2 && temp>=-2))
		{
		s--;
		ans++;
		}
		}
	}
    	cout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
    	return 0;
}
