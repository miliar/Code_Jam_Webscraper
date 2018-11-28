#include <iostream>
#include<algorithm>
#define MAX 2000000000
using namespace std;
int main()
{
  int n,arr[6],arrinpt[6];;
  register int i=0,m,x,j,y,k,it;
  string v[120],str="ABCDE",temp,t;
 int ntc;
 cin>>ntc;
 int tc=0;
 while(ntc--)
	{
             tc++;
             cout<<"Case #"<<tc<<": ";
  cin>>str;
	
  //string str1=str[0]+"0";
  //str1=str1+str.substr(1);
  //char c[100][6]; 
  string str1=str;
  sort(str1.begin(),str1.end());
 string kk=str;

  string res,res1,k1=str;
  int c=0;
  	do{
	 
	  res1=kk;
	  //if(c==1)break;
	  //cout<<str; 
	  //c++;
	  }while(next_permutation (kk.begin(),kk.end()));
	
	do{
	 
	  res=str;
	  if(c==1)break;
	  //cout<<str; 
	  c++;
	  }while(next_permutation (str.begin(),str.end()));


	 if(res1==k1)
	{
		 int flag=0;
			for(int kv=0;kv<str1.length();kv++)
		{
			if(str1[kv]!='0')
			{
				flag=kv;
				break;
			}
		}
string tt="";
tt+=str1[flag];
for(int y=0;y<str1.length();y++)
		{
		if(y!=flag)
			{
				tt+=str1[y];
			}
		}
		  cout<<tt[0]<<"0"<<tt.substr(1)<<"\n";
	 //cout<<strn<<"\n";
	}
	else
	{
		//cout<<"IMH";
	cout<<res<<"\n";
	}
	}
	return 0;
  }
