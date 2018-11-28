#include<iostream>
#include<math.h>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("agrahri.in","r",stdin);
    freopen("test-large.out","w",stdout);
	int t;
	cin>>t;
	int cn=0;
	while(t--)
	{
	    cn++;
	    cout<<"Case #"<<cn<<": ";
		int n;
		cin>>n;
		char *name=new char[n];
		int *v=new int[n];
		int o=-1,b=-1;
		for(int x=0;x<n;x++)
		{
			cin>>name[x]>>v[x];			if(o==-1&&name[x]=='O')o=x;	if(b==-1&&name[x]=='B')b=x;
		}
		if(o==-1)
		{
		    int tt=0;int lb=1;
		    for(int x=0;x<n;x++)
		    {
                tt+=abs(v[x]-lb)+1;
                lb=v[x];
		    }
		    cout<<tt<<"\n";
		}
		else if(b==-1)
		{
		    int tt=0;int lo=1;
		    for(int x=0;x<n;x++)
		    {
		        tt+=abs(v[x]-lo)+1;
		        lo=v[x];
		    }
		    cout<<tt<<"\n";
		}
		else
		{int lb=1,lo=1;
		int so=0,sb=0;
		int tt=0;
		int cn=0;
		while(1)
		{
		    //cout<<"o="<<o<<" b="<<b<<" sb="<<sb<<" so="<<so<<" tt="<<tt<<" lb="<<lb<<" lo="<<lo<<"\n";
		    if(so)
			{so=0;o++;while(o<n&&name[o]!='O')o++;}
			if(sb)
			{sb=0;b++;while(b<n&&name[b]!='B')b++;}
			if(o>=n)
			{
                if(b>=n)
                break;
                tt+=abs(v[b]-lb)+1;
                lb=v[b];
                sb=1;
			}
			else if(b>=n)
			{
			    tt+=abs(v[o]-lo)+1;
			    so=1;
			    lo=v[o];
			}
			else if(o<b)
			{
				so=1;
				tt+=abs(v[o]-lo)+1;
				int movo=abs(v[o]-lo)+1;lo=v[o];
				int movb=min(movo,abs(v[b]-lb));
				if(v[b]>lb)
				lb=lb+min(movo,abs(v[b]-lb));
				else 	lb=lb-min(movo,abs(v[b]-lb));
			}
			else
			{
              sb=1;
              tt+=abs(v[b]-lb)+1;
              int movb = abs(v[b]-lb)+1;lb=v[b];
              int movo = min(movb,abs(v[o]-lo));
              if(v[o]>lo)
              lo=lo+min(movb,abs(v[o]-lo));
              else
              lo=lo-min(movb,abs(v[o]-lo));
			}
		}
		cout<<tt<<"\n";
		}
	}
	return 0;
}
