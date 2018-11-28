#include<iostream>
#include<string>
using namespace std;
int main()
{
    long i,j,k ,t,cas=1;

	__int64 arr2[1000],l;
    char str[1000],ch;
    cin>> t;
 while(t>0)
 {
           bool arr[1000]={0};
    cin>>str;k=0;
    string str1="";
    for(i=0;i<strlen(str);i++)
    {
       if(str[i]>='a'&&str[i]<='z')
       { 
          if(arr[str[i]-'a'+10]==0){arr[str[i]-'a'+10]=1;k++;str1+=str[i];}
       }       
         if(str[i]>='0'&&str[i]<='9')
       { 
          if(arr[str[i]-'0']==0){arr[str[i]-'0']=1;k++;str1+=str[i];}
       }       
    
    
    }    
   // str[0]=1;
    ch=str1[0];
    for(i=0;i<strlen(str);i++)
    {
       if(ch==str[i])arr2[i]=1;
    }
    ch=str1[1];
    for(i=0;i<strlen(str);i++)
    {
       if(ch==str[i])arr2[i]=0;
    }
    for(i=2;i<str1.size();i++)
    {
       ch=str1[i];
      for(j=0;j<strlen(str);j++)
       {
          if(ch==str[j])arr2[j]=i;
       }
    
    }
    
    l=1;
__int64   sum=0;
    for(i=strlen(str)-1;i>=0;i--)
    {
       
       arr2[i]=l*arr2[i];
       sum+=arr2[i];
       l*=(k);                          
    }
    //cout<<sum<<endl;
	printf("Case #%ld: %I64d\n",cas++,sum);
     t--;   
}
    return 0;
}
