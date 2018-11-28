#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
 int l,d,n;
 vector<string> vst;
 vst.push_back("abc");
 vst.push_back("bca");
 vst.push_back("dac");
 vst.push_back("dbc");
 vst.push_back("cba");
 string str="(ab)(bc)(ca)";
 int cnt=0;
 for(int i=0;i<d;i++)
 {
 int j=0;    
 bool f1=false;    
   for(int k=0;k<str.size();k++)
   {
   if(j==l-1)
      {
      cnt++; 
      break;
      } 
   else if(str[k]=='(')
	f1=true;
   else if(str[k]>='a' && str[k]<='z')
     {
       if(str[k]==vst[i][j])
       {
	if(f1==true)
	    {
	    while(str[++k]!=')');
            f1=false;
	    } 
	 j++;
         }
        else
        break;
     }
   }
  }
cout<<cnt<<endl;
return 0;  
}
