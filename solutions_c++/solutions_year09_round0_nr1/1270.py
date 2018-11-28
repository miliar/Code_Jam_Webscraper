#include<iostream>
using namespace std;
int main()
{
  int l,d,n;
  cin>>l>>d>>n;
  char a[5001][16];
  for(int i=0;i<d;i++)
    scanf("%s",a[i]);
  

  for(int i=0;i<n;i++)
    {
      char a1[4300];int b[16][26];
      for(int j=0;j<16;j++) for(int lk=0;lk<26;lk++) b[j][lk]=0;
      scanf("%s",a1);
      int lm=0;int j=0;
      while(lm<l)
	{
	  
          if(a1[j]=='(')
               {
                 j++;
                 while(a1[j]!=')')
		   { b[lm][a1[j]-'a']=1;j++; }     
                 lm++;j++;
                 continue;
               }
          
            
               
	  b[lm][a1[j]-'a']=1;lm++;j++;
             
        }
  //for(int bb=0;bb<l;bb++)
  //{cout<<endl;for(int bc=0;bc<26;bc++)cout<<b[bb][bc];}
     // {int lm1=a[0][0]-'a';
       //   cout<<lm1<<" ";}
      /*for(int ik=0;ik<d;ik++)
       { for(j=0;j<l;j++)
          {int lm1=a[0][0]-'a';
          cout<<lm1<<" ";}
cout<<endl;
       }*/
      int flag,value=0;
      for(j=0;j<d;j++)
	{//cout<<a[j]<<"ghg"<<j<<endl;
         flag=0;
         for(int k=0;k<l;k++)
          if(b[k][a[j][k]-'a']==0)
            flag=1;
         if(flag==0)
         value++; 
	}
      //cout<<value;
      cout<<"Case #"<<i+1<<": "<<value<<endl;       
    }
  
  
  return 0;
}
