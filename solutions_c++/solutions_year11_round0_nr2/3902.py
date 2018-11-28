#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<math.h>


void main()


{	int flag=0,jf=0;
	int n,c,d,no;
	int count,f,coun=1;
	char cs[3],ds[2],str[50];
	char res[50],tgt;
	freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++)
	{
	
		count=0;
		f=0;
		cin>>c;
		if(c)
			cin>>cs;
		cin>>d;
		if(d)
			cin>>ds;
		cin>>no;
		cin>>str;

		for(int j=0;j<no-1;j++)
		{  
			if(jf==1)
		{	
			if(str[j]==ds[0])
				{
					tgt=ds[1];
					flag=1;
				}
				else if(str[j]==ds[1])
				{
					tgt=ds[0];
					flag=1;
				}
				else 
					flag=0;
				if(flag)
				{	
					flag=0;
					for(int k=0;k<count;k++)
					if(tgt==res[k])
					{
						res[0]='\0';
						count=0;
						flag=1;
					}
				}
					if(flag==1)
					{	j++;jf=1;}
				flag=0;
		}
			jf=0;
	//	if(jf==1)
	//	{j++;jf=1;}
			if(c && d)
			{

			if((str[j]==cs[0]&&str[j+1]==cs[1])||(str[j]==cs[1]&&str[j+1]==cs[0]))
			{
				res[count]=cs[2];
				count++;
				f=1;
				
			}
			else
			{
				res[count]=str[j];
				count++;
				f=0;
				
			}

			
			if(f==0)
			{
				if(str[j+1]==ds[0])
				{
					tgt=ds[1];
					flag=1;
				}
				else if(str[j+1]==ds[1])
				{
					tgt=ds[0];
					flag=1;
				}
				else 
					flag=0;
				if(flag)
				{	
					flag=0;
					for(int k=0;k<count;k++)
					if(tgt==res[k])
					{
						res[0]='\0';
						count=0;
						flag=1;
					}
				}
					if(flag==1)
					{	j++;jf=1;}
				flag=0;
				
				
			}

			}
			
			else if(c)
			{
				
				if((str[j]==cs[0]&&str[j+1]==cs[1])||(str[j]==cs[1]&&str[j+1]==cs[0]))
			{
				res[count]=cs[2];
				f=1;
				count++;
			
			}
			else
			{
				res[count]=str[j];
				f=0;
				count++;
				
			}

			}

			else if(d)
			{		flag=0;
					if(str[j+1]==ds[0])
					{	tgt=ds[1];flag=1;}
					else if(str[j+1]==ds[1])
					{	tgt=ds[0];flag=1;}
					res[count]=str[j];
					count++;
					if(flag)
					{flag=0;
					for(int k=0;k<count;k++)
					if(tgt==res[k])
					{
						res[0]='\0';
						count=0;
						flag=1;
						j++;jf=1;
					}
					}
					


			}
			else
			{	
				strcpy(res,str);
				count=strlen(str);
				
			}


			if(f==1)
			{
				j++;jf=1;	
				
			}
				if((j==no-2)&&(c||d))
				{	
					res[count]=str[j+1];
					count++;
				}

		}
		
		if(no==1)
			res[count++]=str[0];
		//if(f==1)
		//	res[count++]=str[j];
		cout<<"Case #"<<coun++<<": [";
		for(int r=0;r<count;r++)
		{	cout<<res[r];
			if(r!=count-1)
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
}