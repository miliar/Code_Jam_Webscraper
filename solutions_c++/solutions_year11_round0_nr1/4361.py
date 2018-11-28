#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	
	long long t,k,n,c,bmove[110],omove[110],b,o,bdone,odone,bpos,opos,done,pushed;
	char ch,q[110];
	
	cin>>t;
	
	for(k=1;k<=t;k++)
	{
		cin>>n;
		
		//getchar();
		
		b=0;
		o=0;
		
		for(c=0;c<n;c++)
		{
			cin>>ch;
			q[c]=ch;
			if(ch=='B')
			{
				cin>>bmove[b];
				b++;
			}
			else
			{
				cin>>omove[o];
				o++;
			}
			
			//cout<<q[c]<<endl;
		}
		
		bdone=0;
		odone=0;
		
		done=0;
		
		bpos=1;
		opos=1;
		
		for(c=0;;c++)
		{
			//cout<<c<<" "<<opos<<" "<<bpos<<endl;
			
			pushed=0;
			
			if(bdone==b && odone==o && done==n) break;
			
			if(bdone<b)
			{
				if(bpos==bmove[bdone]) 
				{
					if(q[done]=='B') 
					{
						pushed=1;
						bdone++;
						done++;
					}
				}
				else if(bpos>bmove[bdone]) bpos--;
				else bpos++;
			}
			
			if(odone<o)
			{
				if(opos==omove[odone]) 
				{
					if(q[done]=='O' && pushed==0) 
					{
						odone++;
						done++;
					}
				}
				else if(opos>omove[odone]) opos--;
				else opos++;
			}
			
			
			
		}
		
		cout<<"Case #"<<k<<": "<<c<<endl;
	}
	return 0;
}
