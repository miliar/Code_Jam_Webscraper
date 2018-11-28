#include<stdio.h>
#include<cstring>
#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include <fstream>
using namespace std;
int posa,posb;
char s[1305]; 
int pos[1305];
int movea[1305],moveb[1305];
int main() 
{
	ofstream outfile("C:\\test.txt"); 
	int t;
	cin>>t;
	int ca=0;
	while(t--)
	{
		ca++;
		int n;
		cin>>n;
		int la=0,lb=0;
		for(int i=1;i<=n;i++)cin>>s[i]>>pos[i];
		for(int i=1;i<=n;i++)
		{
			if(s[i]=='O')movea[la++]=pos[i];
			else moveb[lb++]=pos[i];
		}
		int ans=0;
		int l=1;
		int ta=0,tb=0;
		posa=posb=1;
		while(l<=n)
		{
			 
			if(s[l]=='O')
			{
				int t=abs(pos[l]-posa)+1;
				posa=pos[l];
				ans+=t; 
				ta++;
				if(tb<lb)
				{
					if(moveb[tb]>=posb){
						if(posb+t<=moveb[tb])posb+=t;
						else posb=moveb[tb];
					}
					else{
						if(posb-t>=moveb[tb])posb-=t;
						else posb=moveb[tb];
					
					}
				}
				l++;
			}
			else if(s[l]=='B')
			{
				int t=abs(pos[l]-posb)+1;
				posb=pos[l];
				ans+=t; 
				tb++;
				if(ta<la)
				{
					if(posa<=movea[ta])
					{
						if(posa+t<=movea[ta])posa+=t;
						else posa=movea[ta];
					}
					else{
						if(posa-t>=movea[ta])posa-=t;
						else posa=movea[ta];
					}
				}
				l++;
			}
			
		} 
		outfile<<"Case #"<<ca<<": "<<ans<<endl;
	}
	 outfile.close();
} 