#include <iostream>
#include <string>

using namespace std;
int d,l,n,words;


int main(int argc,char *argv[])
{
string s;
cin>>l>>d>>n;
char pat[d][l];
//pat=new char

for(int i=0;i<d;i++)
	for(int j=0;j<l;j++)
		cin>>pat[i][j];
		
for(int i=0;i<n;i++)
{
cin>>s;
words=0;
	for(int j=0;j<d;j++)
	{
	for(int k=0,p=0;k<l;k++,p++)
	{
	if(s[p]=='(')
	 { p++;
	 while(s[p]!=')')
	  {
	  if(pat[j][k]==s[p])
	    {
		  if(k==(l-1))
		  {words++;}
		  while(s[p]!=')')
			  p++;
		
		k-=l;		  
		  break;
		}
      p++;
	  
	  }
	
    k+=l;	
	  
	  }
	else if(s[p]==pat[j][k])
	{
	  if(k==(l-1))
	  words++;
	
	
	}
	else 
	   break;
	
	
	}

	}
	
cout<<"Case #"<<i+1<<": "<<words<<endl;	

}



return 0;}