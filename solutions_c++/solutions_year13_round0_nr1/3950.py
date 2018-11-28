#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int n=0;
    while(t--)
    { n++;
        string str[4];
        int i,j,c=0,d=0,flag=0,dot=0;
       
      
        for(i=0;i<4;i++)
        {
        cin>>str[i];
    }    
         for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='.')
            dot++;
            }    
            
        }    
        for(i=0;i<4;i++)
        {
            if(str[i][i]=='X')
            c++;
            else if(str[i][i]=='O')
            d++;
            else if(str[i][i]=='T')
            {
                c++;d++;
            }    
            
        }
        if(c==4)
        flag=1;
        else if(d==4)
        flag=-1;
         if(flag==1)
   {
       cout<<"Case #"<<n<<": "<<"X won"<<endl;
       continue;
   }    
   else if(flag==-1)
    {
       cout<<"Case #"<<n<<": "<<"O won"<<endl;
       continue;
   }    
   
      
       
        c=d=0;
        for(i=0;i<4;i++)
        {
            if(str[i][3-i]=='X')
            c++;
            else if(str[i][3-i]=='O')
            d++;
            else if(str[i][3-i]=='T')
            {
                c++;d++;
            }    
        }
        if(c==4)
        flag=1;
        else if(d==4)
        flag=-1;
            if(flag==1)
   {
       cout<<"Case #"<<n<<": "<<"X won"<<endl;
       continue;
   }    
   else if(flag==-1)
    {
       cout<<"Case #"<<n<<": "<<"O won"<<endl;
       continue;
   }    
   
   //cout<<"Entered"<<endl;
  
        c=d=0;
        for(i=0;i<4;i++)
        {
            c=d=0;
            //cout<<i<<endl;
            for(j=0;j<4;j++)
            {
                //cout<<str[i][j]<<" ";
                
                if(str[i][j]=='X')
            c++;
            else if(str[i][j]=='O')
            d++;
            else if(str[i][j]=='T')
            {
                c++;d++;
            }    
        }    
        //cout<<c<<","<<d<<endl;
            if(c==4)
           flag=1;
           else if(d==4)
           flag=-1;
           c=d=0;
           
  
         if(flag==1)
   {
       cout<<"Case #"<<n<<": "<<"X won"<<endl;
       break;
   }    
   else if(flag==-1)
    {
       cout<<"Case #"<<n<<": "<<"O won"<<endl;
       break;
   }    
}    if(flag==1 || flag==-1)
        continue;
   
       for(j=0;j<4;j++)
        {c=d=0;
            for(i=0;i<4;i++)
            {
                if(str[i][j]=='X')
            c++;
            else if(str[i][j]=='O')
            d++;
            else if(str[i][j]=='T')
            {
                c++;d++;
            }    
        }    
            if(c==4)
           flag=1;
           else if(d==4)
           flag=-1;
           c=d=0;
       
    }        
             if(flag==1)
   {
       cout<<"Case #"<<n<<": "<<"X won"<<endl;
       continue;
   }    
   else if(flag==-1)
    {
       cout<<"Case #"<<n<<": "<<"O won"<<endl;
       continue;
   }    
   else if(flag==0 && dot==0)
   {
   cout<<"Case #"<<n<<": "<<"Draw"<<endl;
   continue;
   }    
   else if(flag==0&&dot>0)
   {
       cout<<"Case #"<<n<<": "<<"Game has not completed"<<endl;
      continue;
    }         
   }
   return 0;
}       
