#include<iostream>
#include<string>

using namespace std;
// "welcome to code jam"



int main()
{
  string in;
  int t;

   freopen("cjam.out","w",stdout);
    freopen("cjam.in","r",stdin);

   scanf("%d",&t);
   getchar();
  for(int tt=0;tt<t;tt++)
  {
    int dp[19]; // dp[18] has answer 
    getline(cin,in);
   
    fill(dp,dp+19,-1);

    int l=in.length();
    
   //   cout<<l<<endl;
    for(int i=0;i<l;i++)
     {
      if(in[i]=='w')
       {
          if(dp[0]==-1)
             dp[0]=1;
          else
             dp[0]++;
       }
      if(in[i]=='e')
       {
           if(dp[0]!=-1) // der exists a "w"
            {
               if(dp[1]==-1)
                     dp[1]=0;         
              dp[1]=dp[0]+dp[1];
            }
           if(dp[5]!=-1) // der exists a "welcom"
            {
               if(dp[6]==-1)
                     dp[6]=0;
              dp[6]=dp[5]+dp[6];
            }
           if(dp[13]!=-1) // der exists a "welcome to cod"
            {
               if(dp[14]==-1)
                     dp[14]=0;
              dp[14]=dp[13]+dp[14];
            }         
       }
      if(in[i]=='l')
       {

         if(dp[1]!=-1) // der exists a "we"
           {
               if(dp[2]==-1)
                     dp[2]=0;
            dp[2]=dp[2]+dp[1];
           }
       }
      if(in[i]=='c')
       {

           if(dp[2]!=-1) // der exists a "wel"
            {
               if(dp[3]==-1)
                     dp[3]=0;
              dp[3]=dp[2]+dp[3];
            }
           if(dp[10]!=-1) // der exists a "welcome to "
            {
               if(dp[11]==-1)
                     dp[11]=0;
              dp[11]=dp[10]+dp[11];
            }
       }
      if(in[i]=='o')
       {
           if(dp[3]!=-1) // der exists a "welc"
            {
               if(dp[4]==-1)
                     dp[4]=0;
              dp[4]=dp[3]+dp[4];
            }
           if(dp[8]!=-1) // der exists a "welcome t"
            {
               if(dp[9]==-1)
                     dp[9]=0;
              dp[9]=dp[8]+dp[9];
            }
           if(dp[11]!=-1) // der exists a "welcome to c"
            {
               if(dp[12]==-1)
                     dp[12]=0;
              dp[12]=dp[11]+dp[12];
            }
       }
      if(in[i]=='m')
       {
           if(dp[4]!=-1) // der exists a "welco"
            {
               if(dp[5]==-1)
                     dp[5]=0;
              dp[5]=dp[4]+dp[5];
            }
           if(dp[17]!=-1) // der exists a "welcome to code ja"
            {
               if(dp[18]==-1)
                     dp[18]=0;
              dp[18]=dp[17]+dp[18];
            }
       }       
      if(in[i]==' ')
       {
           if(dp[6]!=-1) // der exists a "welcome"
            {
               if(dp[7]==-1)
                     dp[7]=0;
              dp[7]=dp[6]+dp[7];
            }
           if(dp[9]!=-1) // der exists a "welcome to"
            {
               if(dp[10]==-1)
                     dp[10]=0;
              dp[10]=dp[9]+dp[10];
            }
           if(dp[14]!=-1) // der exists a "welcome to code"
            {
               if(dp[15]==-1)
                     dp[15]=0;
              dp[15]=dp[14]+dp[15];
            }
       }
      if(in[i]=='t')
       {
           if(dp[7]!=-1) // der exists a "welcome "
            {
               if(dp[8]==-1)
                     dp[8]=0;
              dp[8]=dp[7]+dp[8];
            }
       }
      if(in[i]=='d')
       {
           if(dp[12]!=-1) // der exists a "welcome to co"
            {
               if(dp[13]==-1)
                     dp[13]=0;
              dp[13]=dp[12]+dp[13];
            }
       }
      if(in[i]=='j')
       {
           if(dp[15]!=-1) // der exists a "welcome to code "
            {
               if(dp[16]==-1)
                     dp[16]=0;
              dp[16]=dp[15]+dp[16];
            }
       }
      if(in[i]=='a')
       {
           if(dp[16]!=-1) // der exists a "welcome to code j"
            {
               if(dp[17]==-1)
                     dp[17]=0;
              dp[17]=dp[16]+dp[17];
            }
       }

    
      for(int j=0;j<19;j++)     
         dp[j]%=10000;
     }
      if(dp[18]==-1)
         dp[18]++;

      char ans[5];
      ans[4]='\0';
        for(int j=3;j>=0;j--)
         {
           ans[j]=dp[18]%10+'0';
           dp[18]/=10;
         }

      printf("Case #%d: %s\n",tt+1,ans);
   }
 
  return 0;
}
