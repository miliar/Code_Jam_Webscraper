#include<iostream>
#include<string>
#include<fstream>
using namespace std;

string form_list(char [38][40],char [30][32],string,int,int,int);
int checkd(string ,char [30][32],int,int);
char checkc(char,char,char [38][40],int);
void main()
{
	int t,c,d,n;
	char cn[38][40],dn[30][32];
	string s,s3="";
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("final.txt");
	fin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		
    fin>>c;
	for(int i=0;i<c;i++)
		fin>>cn[i];
	fin>>d;
	for(int i=0;i<d;i++)
		fin>>dn[i];
	fin>>n;

	fin>>s;
	s3=form_list(cn,dn,s,c,n,d);
	int l=s3.length();
	if(l==0) fout<<"Case #"<<tt<<": "<<"[]\n";
	else
	{
	fout<<"Case #"<<tt<<": "<<"["<<s3[0];
	for(int j=1;j<l;j++)
	{ 
		fout<<", "<<s3[j];
       
	}
	fout<<"]\n";
	}
	}
 fin.close();
 fout.close();

	}


string form_list(char cn[38][40],char dn[30][32],string s,int c,int n,int d)
{
	

	char *s2=new char [n];
	int i2=0,t2=0;;
	char t=0;
	for(int i=0;i<n;i++)
	{

		if(i2)
		{
		  t=checkc(s[i],s2[i2-1],cn,c);
          if(!t)
		  {
			s2[i2]=s[i];
			i2++;
   		  }
  		  else
		  {
			s2[i2-1]=t;
			
		  }
		}
		else
		{
			s2[i2]=s[i];
			i2++;
		}

		t2=checkd(s2,dn,d,i2-1);
		if(t2>=0)
		{
		  i2=0;	
		}
		
	
	
	}
	s2[i2]='\0';
	return s2;
	
}
char checkc(char c1,char c2,char cn[38][40],int c)
{
	
	for(int i=0;i<c;i++)
	{
		if(c2==cn[i][0])
		{
			if(c1==cn[i][1])
				return cn[i][2];
		}
		if(c1==cn[i][0])
		{
			if(c2==cn[i][1])
				return cn[i][2];

		}

	}
	return 0;
}
int checkd(string s2,char dn[30][32],int d,int i2)
{
	for(int i=0;i<d;i++)
	{
		for(int j=0;j<2;j++)
		{
        	if(s2[i2]==dn[i][j])
			{
				if(j==0)
				{
					for(int k=i2-1;k>=0;k--)
				    {
					   if(s2[k]==dn[i][1])
					   {  
						   return k;
						  
					   }
					}
				}
				else if(j==1)
				{
					for(int k=i2-1;k>=0;k--)
				    {
					   if(s2[k]==dn[i][0])
					   {  
						   return k;
					   }
					}
				}
			}
		}
	}
	return -1;
}

