#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
int main()
{
    string dict[6000],str;
    char arr[16][27];
    int l,d,n,j,k,i,len,flag,count;
    cin>>l>>d>>n;
    for(i=0;i<d;i++)
    cin>>dict[i];
    for(i=0;i<n;i++)
    {
      cin>>str;
      count=0;
      len=0;
      for(j=0;j<16;j++)
       for(k=0;k<27;k++)
        arr[j][k]=0;
      for(j=0;j<str.length();j++)
      { len++;
        if(str[j]=='(')
        {  
           j++;
           while(str[j]!=')')
           {arr[len][str[j]-96]=1;j++;}
        }
        else
         arr[len][str[j]-96]=1;
      } 
      for(j=0;j<d;j++)
      { flag=0;
        for(k=0;k<dict[j].length();k++)
          if(arr[k+1][dict[j][k]-96]!=1)
          {flag=1;break;}
        if(flag==0)
        count++;
      }
      cout<<"Case "<<"#"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
      
      
        
      
           
        
        
      
