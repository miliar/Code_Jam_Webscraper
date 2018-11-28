# include <iostream>
using namespace std;
int main()
{
  int a,b,c,d,i,j,k,m,n;
  int t;string s1,s2,s3;
  float wp,owp,oowp;int win,loss;
  cin>>t;
  m=0;
  while(t--)
   {
   m++;
     cin>>n;
     //char x[n][n];
     string st[n];
     for(i=0;i<n;i++)
      {
       cin>>st[i]; 
      }
      
      float awp[n],aowp[n],aoowp[n];int awin[n],aloss[n];
      for(i=0;i<n;i++)
       {
        loss=0;win=0;
        s1=st[i];
        for(j=0;j<n;j++)
         {
           if(s1[j]=='1')
           win++;
           else if(s1[j]=='0')
           loss++;
         }
         //cout<<"win=="<<win<<"\n";
         //cout<<"loss=="<<loss<<"\n";
         awin[i]=win;aloss[i]=loss;
         awp[i]=(float)win/(win+loss);
       }
       for(i=0;i<n;i++)
       {
         owp=0.0;c=0;
         //s2=st[i];
         for(j=0;j<n;j++)
          {
            if(st[i][j]!='.')
            {
             if(st[j][i]=='1')
              {
                c++;
                owp+=(float)(awin[j]-1)/(awin[j]+aloss[j]-1);
              }
              else if(st[j][i]=='0')
              {
                c++;
                owp+=(float)awin[j]/(awin[j]+aloss[j]-1);
              }
              
            }
          }
          //cout<<"owp=="<<owp<<"\n";
          aowp[i]=owp/(float)c;  
       }
       for(i=0;i<n;i++)
        {
        oowp=0.0;c=0;
        s1=st[i];
          for(j=0;j<n;j++)
          {
           if(s1[j]=='1'||s1[j]=='0')
           {
            oowp+=aowp[j];
            c++;
           }
          }
          aoowp[i]=oowp/(float)c;
        } 
        cout<<"Case #"<<m<<":"<<"\n";
        for(i=0;i<n;i++)
        {
          cout<<(0.25*awp[i])+((0.50*aowp[i])+(0.25*aoowp[i]))<<"\n";
        }
   }
  return 0;
}
