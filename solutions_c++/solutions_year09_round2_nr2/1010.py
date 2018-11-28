#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("B-large(2).in",ios::in);
    out.open("ap.out",ios::out);
    int T,t,i,j,n;
	char temp;
    in >> T;
	string s,sp;
	bool occur[10];
    for (t=1;t<=T;t++)
    {
		for (i=0;i<10;i++) occur[i]=false;
		in>>s;
		for (i=0;i<s.size();i++) occur[s[i]-'0']=true;
		if (s.size()==1)
		{
			out<<"Case #"<<t<<": "<<s+'0'<<"\n";
			continue;
		};
		n=s.size()-1;
		while ((n>0)&&(s[n]<=s[n-1])) n--;
		if (n==0)
		{
						
			sp="";
			sp+=s[s.size()-1];
			sp+='0';
			for (i=s.size()-2;i>=0;i--)	sp+=s[i];
			j=0;
			while (sp[j]=='0') j++;
			temp=sp[j];
			sp[j]=sp[0];
			sp[0]=temp;
			out<<"Case #"<<t<<": "<<sp<<"\n";
			continue;	
		};
		n--;
		j=n;
		while ((j<s.size()-1)&&(s[j+1]>s[n])) j++;
		while ((j>0)&&(s[j-1]==s[j])) j--;
		temp=s[j];
		s[j]=s[n];
		s[n]=temp;
		for (i=n+1;i<s.size();i++) for (j=i+1;j<s.size();j++)
		{
			if (s[i]>s[j])
			{
				temp=s[i];
				s[i]=s[j];
				s[j]=temp;	
				
			};
			
		};
 		out<<"Case #"<<t<<": "<<s<<"\n";		

    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
