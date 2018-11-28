#include<iostream>
#include<ostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<iomanip>
#include<map>
#include<math.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{

  freopen("input.txt","r",stdin);
 freopen("output.in","w",stdout);
    
    int t,index=1,i,j;
    cin>>t;
    while(index<=t)
    {
        string s[4],result,d1,d2;
        int f=0,z=0;
        for(i=0;i<4;i++)
            cin>>s[i];
        for(i=0;i<4;i++)
        { 
            d1.push_back(s[i][i]);
        }
        for(i=0;i<4;i++)
        {  d2.push_back(s[i][3-i]);
          
        }
        
        for(i=0;i<4;i++)
        {
            if(s[i]=="XXXX"||s[i]=="TXXX"||s[i]=="XTXX"||s[i]=="XXTX"||s[i]=="XXXT")
            {
                result="X won";
                f=1;
                break;
            }
        }
        if(f==0)
        {
            if(d1=="XXXX"||d1=="TXXX"||d1=="XTXX"||d1=="XXTX"||d1=="XXXT"||d2=="XXXX"||d2=="TXXX"||d2=="XTXX"||d2=="XXTX"||d2=="XXXT")
            {
                result="X won";
                f=1;
             
 
            }
        }
        if(f==0)
        {  
            for(i=0;i<4;i++)
            {
               
                if(s[i]=="OOOO"||s[i]=="TOOO"||s[i]=="OTOO"||s[i]=="OOTO"||s[i]=="OOOT")
                {
                    result="O won";
                    f=1;
                    break;
                }
            }
        }
        if(f==0)
        {
            if(d1=="OOOO"||d1=="TOOO"||d1=="OTOO"||d1=="OOTO"||d1=="OOOT"||d2=="OOOO"||d2=="TOOO"||d2=="OTOO"||d2=="OOTO"||d2=="OOOT")
            {
                result="O won";
                f=1;
                
                
            }
        }
        if(f==0)
        {
            string c[4];
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                    c[i].push_back(s[j][i]);
            }
            for(i=0;i<4;i++)
            {
                if(c[i]=="XXXX"||c[i]=="TXXX"||c[i]=="XTXX"||c[i]=="XXTX"||c[i]=="XXXT")
                {
                    result="X won";
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                
                for(i=0;i<4;i++)
                {
                    
                    if(c[i]=="OOOO"||c[i]=="TOOO"||c[i]=="OTOO"||c[i]=="OOTO"||c[i]=="OOOT")
                    {
                        result="O won";
                        f=1;
                        break;
                    }
                }
            }
                
                
        }
        if(f==0)
        {
            for(i=0;i<4;i++)
            {
                unsigned long found=s[i].find(".");
                if(found!=string::npos)
                {
                    z=1;break;
                    
                }
                
                
            }
            if(z==1)
                result="Game has not completed";
            else
                result="Draw";
        }
         cout<<"Case #"<<index<<": "<<result<<"\n";
        
        index++;
    }
    
    
    return 0;
}

