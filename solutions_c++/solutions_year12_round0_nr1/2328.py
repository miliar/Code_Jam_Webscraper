#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;



char trans[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k',
	      'r','z','t','n','w','j','p','f','m','a','q'};



int main()
{

  int n;
  cin>>n;
  string trash;
  getline(cin,trash);
  string* str=new string[n];
  for(int i=0; i<n; i++)
    {
      getline(cin,str[i]);

    }

  for(int i=0;i<n;i++)
    {
      string s=str[i];
      cout<<"Case #"<<i+1<<": ";
      for(int j=0;j<s.length();j++)
	{
	  if(s[j]==' ')
	    cout<<" ";
	  else
	    printf("%c",trans[(int)s[j]-97]);
	}
      cout<<endl;
    }





}
