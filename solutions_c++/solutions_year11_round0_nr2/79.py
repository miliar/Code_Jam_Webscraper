#include <iostream>
using namespace std;
int main()
{
	int t,c,n,i,j,ot,k,d;	
	char s[110];
	char b;
	bool cl;
	char cm[128][128],o[110];
	char op[128][128];
	int h[128];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		ot=0;
		cin>>c;
		memset(cm,0,sizeof(cm));
		memset(op,0,sizeof(op));
		memset(h,0,sizeof(h));
		for(i=0;i<c;i++)
		{
			cin>>s;
			cm[s[0]][s[1]]=s[2];
			cm[s[1]][s[0]]=s[2];
		}
		cin>>d;
		for(i=0;i<d;i++)
		{
			cin>>s;
			op[s[0]][++op[s[0]][0]]=s[1];
			op[s[1]][++op[s[1]][0]]=s[0];
		}
		cin>>n;
		cin>>s;
		for(i=0;i<n;i++)
		{
			if(ot>0 && cm[s[i]][o[ot-1]])
			{
				h[o[ot-1]]--;
				o[ot-1]=cm[s[i]][o[ot-1]];
				continue;
			}
			cl=0;
			for(k=1;k<=op[s[i]][0];k++)
				if(h[op[s[i]][k]])
				{
					memset(h,0,sizeof(h));
					ot=0;cl=1;
				}
			if(cl) continue;
			o[ot++]=s[i];
			h[s[i]]++;
		}
		cout<<"Case #"<<j<<": [";
		for(i=0;i<ot-1;i++)
			cout<<o[i]<<", ";
		if(ot>=1)
			cout<<o[ot-1]<<"]\n";
		else cout<<"]\n";
	}
}
