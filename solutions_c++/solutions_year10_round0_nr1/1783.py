#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;


int main()
{

	fstream input;
	string s;
	cin>>s;
    input.open(s.c_str(),ios::in);

	int cases;
	input>>cases;
	fstream output;
	output.open("output.txt",ios::out);
	for(int i=0;i<cases;i++)
	{
		
		int n,k;
		input>>n;
		input>>k;
	    char str[100];
	    int sz=0;
	    while(k!=0)
	    {
                   if(k%2==0)
                             str[sz]='0';
                   else
                       str[sz]='1';
                                 
                   k=k/2;
                   sz++;
                   
         }
       //  output<<str<<"   ";
         int flag=0;             //off
         if(n<=sz)
         {
                          int cnt=0;
                          for(int j=0;j<n;j++)
                          {
                                  if(str[j]=='1')
                                                 cnt++  ;      
                          }                 
                          if(cnt==n)
                                    flag=1;
         }
         if(flag==1)
                    output<<"Case #"<<i+1<<": ON"<<endl;
         else
                    output<<"Case #"<<i+1<<": OFF"<<endl;


         
	}
	input.close();
	output.close();
	system("pause");
	
	return 0;

}
