#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>

int pb=1,po=1;
int bval,oval;
char prev;
int pval=0;
int sec;
int osec,bsec;

int calculate(char r,int p)
{
	if(r=='O')
	{ 
		if(p>po)
			oval=p-po+1;
		else
			oval=po-p+1;
		po=p;
		return oval;
	}
	else
	{
		if(p>pb)
			bval=p-pb+1;
		else
			bval=pb-p+1;
		pb=p;
		return bval;
	}
}
void main()

{	
	int n,no,val,count=1;
	//char s[50];
	char r;
	int p;
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++)
	{	pb=po=1;
		pval=0;
		osec=bsec=0;
		cin>>no;
		for(int j=0;j<no;j++)
		{
			cin>>r>>p;
		//	cout<<s<<" "<<p<<" ";
			val=calculate(r,p);
			//cout<<val<<" ";
			if(pval!=0)
			{
				if(prev==r)
				{
					sec=sec+val;
					pval=pval+val;
					if(r=='O')
						osec=sec;
					else
						bsec=sec;
				}
				else if(prev!=r)
				{
					if(val-1<=pval)
					{
						sec++;
						pval=1;
						if(r=='O')
							osec=sec;
						else
							bsec=sec;
					}
					else
					{
						//sec=sec+val-1;	
						//pval=val-1+pval;
						if(r=='O')
							osec=sec=val+osec;
						else
							bsec=sec=val+bsec;
						pval=val-1-pval;
					}
					prev=r;
				}
			}
			else
			{
				sec=val;
				pval=val;
				prev=r;
				if(r=='O')
					osec=sec;
				else
					bsec=sec;
			}
		}
		cout<<"Case #"<<count++<<": "<<sec<<endl;
	}
}