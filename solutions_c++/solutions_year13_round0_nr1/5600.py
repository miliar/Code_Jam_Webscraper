#include<iostream>
using namespace std;
int main()
{int t,dt,fl,i,j,m;
char ar[5][5],tp;
cin>>t;
for(m=0;m<t;m++)
	{cin>>ar[0];
	cin>>ar[1];
	cin>>ar[2];
	cin>>ar[3];
	
	dt=0;
	for(i=0;i<4;i++)
	{fl=0;
	if(ar[i][0]=='.')
		{dt=1;}
		for(j=0;j<3;j++)
		{if(ar[i][j]!='T')
			{tp=ar[i][j];}
		else if(j>0)
			{tp=ar[i][j-1];}
		else {tp=ar[i][j+1];}
		if((tp==ar[i][j+1] && ar[i][j+1]!='.')||ar[i][j+1]=='T')
			{}		
		else {fl=1;}		
		if(ar[i][j+1]=='.')		
			{fl=1;dt=1;break;}		
				
		}	
	if(fl==0) break;}
	if(fl==0)
		{cout<<"Case #"<<m+1<<": "<<tp<<" won"<<endl;
		}
	
	else
		{
			for(j=0;j<4;j++)
				{fl=0;
					for(i=0;i<3;i++)
					{if(ar[i][j]!='T')
					{tp=ar[i][j];}
					else if(i>0)
			{tp=ar[i-1][j];}
		else {tp=ar[i+1][j];}

					if((tp==ar[i+1][j]&&ar[i+1][j]!='.')||ar[i+1][j]=='T')
						{}		
						else
						{fl=1;break;}
					}
				if(fl==0) break;}		
		
	if(fl==0)
		{cout<<"Case #"<<m+1<<": "<<tp<<" won"<<endl;
		}

else 
		{fl=0;
		for(i=0;i<3;i++)
			{if(ar[i][i]!='T')
			{tp=ar[i][i];}
		else if(i>0)
			{tp=ar[i][i-1];}
		else {tp=ar[i][i+1];}
			if((tp==ar[i+1][i+1]&&ar[i+1][i+1]!='.')||ar[i+1][i+1]=='T')
				{}
			else {fl=1;break;}
			}
		if(fl==0) 
			{cout<<"Case #"<<m+1<<": "<<tp<<" won"<<endl;}			
					
			else
				{fl=0;
				for(i=0;i<3;i++)
			{if(ar[i][3-i]!='T')
			{tp=ar[i][3-i];}
		else if(i>0)
			{tp=ar[i-1][4-i];}
		else {tp=ar[i+1][2-i];}
			if((tp==ar[i+1][3-(i+1)]&&ar[i+1][3-(i+1)]!='.')||ar[i+1][3-(i+1)]=='T')
				{}
			else {fl=1;break;}
			}				
		

		
				

if(fl==0) {cout<<"Case #"<<m+1<<": "<<tp<<" won"<<endl;}
else if(dt==1) {cout<<"Case #"<<m+1<<": "<<"Game has not completed"<<endl;}
else {cout<<"Case #"<<m+1<<": "<<"Draw"<<endl;}
}}
}
}




}
