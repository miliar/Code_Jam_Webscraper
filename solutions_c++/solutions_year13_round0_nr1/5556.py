#include<iostream>
using namespace std;
int main()
{
	int i,j,t;
	char a[4][4];
	float rcount=0,lcount=0,dcount=0,tot=0,d1count=0;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.in","w",stdout);
	cin>>t;
	int r=1;
	for(;t>0;t--,r++)
	{
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>a[i][j];
		}
	}
	dcount=0;d1count=0;
	for(i=0;i<4;i++)
	{	rcount=0;
		for(j=0;j<4;j++)
		{	
			if(a[i][j]=='X') rcount++;
			else if(a[i][j]=='T') rcount+=.5;
			else if(a[i][j]=='.') rcount-=20;
		}
		tot=tot+rcount;
		if(rcount>3||(rcount<1&&rcount>=0)) break;
		
	}
	for(j=0;j<4;j++)
	{	lcount=0;
		for(i=0;i<4;i++)
		{
			if(a[i][j]=='X') lcount++;
			else if(a[i][j]=='T') lcount+=.5;
			else if(a[i][j]=='.') lcount-=20;			
		}
		tot=tot+lcount;
		if(lcount>3||(lcount<1&&lcount>=0)) break;
		
	}
	for(i=0,j=0;i<4;i++,j++)
	{			
		if(a[i][j]=='X') dcount++;
		else if(a[i][j]=='T') dcount+=.5;
		else if(a[i][j]=='.') dcount-=20;
		tot=tot+dcount;
		
	}
	for(i=0,j=3;i<4;i++)
	{	if(a[i][j]=='X') d1count++;
		else if(a[i][j]=='T') d1count+=.5;
		else if(a[i][j]=='.') d1count-=20;
		tot=tot+d1count;j--;
		
	}
cout<<"Case #"<<r<<": ";
if(rcount>3||lcount>3||dcount>3||d1count>3)
	cout<<"X won";
else if((rcount<1&&rcount>=0)||(lcount<1&&lcount>=0)||(dcount<1&&dcount>=0)||(d1count<1&&d1count>=0))
	cout<<"O won";
else if(rcount<0||lcount<0||dcount<0||d1count<0)
	cout<<"Game has not completed";

else 
	cout<<"Draw";
cout<<endl;
}
return 0;
}

//freopen("jj.txt","r",stdin);
//freopen("jj.text","w",stdout);
