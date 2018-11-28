#include<stdio.h>
#include<iostream>
#include<algorithm>
#include"string"
#include<vector>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<queue>
#include<set>
#include<stdafx.h>
using namespace std;
const int INF=0x7fffffff;
const double eps=(1.0e-9);
const double PI=atan2(0.0,-1.0);


       int main()
        {

			int cas;
            string line;
            cin>>cas;
            int num=1;
            int i,j,mod=10000;
            while(cas--)
            {
               int dp[20];
			   memset(dp,0,sizeof(dp));
                cin>>line;
				int len.line.size();
                for(i=0;i<len;i++)
                {
                    if(line[i]=='w')
                    {
                        dp[1]++;
                    
                    }
                    else if(line[i]=='e')
                    {
                        dp[2]+=dp[1];
                      
                        dp[7]+=dp[6];
                       
                        dp[15]+=dp[14];
                    }
                    else if(line[i]=='l')
                    {
                        dp[3]+=dp[2];
                      
                    }
                    else if(line[i]=='c')
                    {
                        dp[4]+=dp[3];
                     
                        dp[12]+=dp[11];
                     
                    }
                    else if(line[i]=='o')
                    {
                        dp[5]+=dp[4];
                     
                        dp[10]+=dp[9];
                       
                        dp[13]+=dp[12];
                       
                    }
                    else if(line[i]=='m')
                    {
                        dp[6]+=dp[5];
                        dp[19]+=dp[18];
                    }
                    else if(line[i]==' ')
                    {
                        dp[8]+=dp[7];
                        dp[11]+=dp[10];
                        dp[16]+=dp[15];
                    }
                    else if(line[i]=='t')
                    {
                        dp[9]+=dp[8];
                    }
                    else if(line[i]=='d')
                    {
                        dp[14]+=dp[13];
                    }
                    else if(line[i]=='j')
                    {
                        dp[17]+=dp[16];
                    }
                    else if(line[i]=='a')
                    {
                        dp[18]+=dp[17];
                    }
                    for (j = 0; j < 20;j++ )
                        dp[j] %= mod;
                }
                string ans="";
				while(dp[19])
				{
					ans+=dp[19]%10;
					dp[19]/=10;
				}
				for(i=0,j=ans.size()-1;i<ans.size();i++,j--)
					ans[j]=ans[i];
                string blank="";
                int k=ans.Length;
                while(k<4)
                {
                    k++;
                    blank+='0';
                }
                blank+=ans;
                //w.WriteLine("Case #{0}: {1}",num++,blank);
				cout<<"Case#"<<num<<": "<<blank<<endl;
				num++;
            }
        }
    }
}
