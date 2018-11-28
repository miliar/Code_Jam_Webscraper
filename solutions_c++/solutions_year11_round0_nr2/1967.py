#include<stdio.h>
#include<iostream>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
string VC;
char c1,c2,c3,c4,c5;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A1.out","w",stdout);
    char com[129][129],opo[129][129];
    int t,cas=1,C,D,N,i,j,k,chk,chk1,ll;
    string inS,inD,S;
    scanf("%d",&t);
    while(t--)
    {

       scanf("%d",&C);
       for(i=0;i<129;i++)
        for(j=0;j<129;j++)
        {
           com[i][j]='1';
           opo[i][j]='0';
        }


       for(i=0;i<C;i++)
       {
            cin>>inS;
            com[inS[0]][inS[1]]=com[inS[1]][inS[0]]=inS[2];
       }



       scanf("%d",&D);

      for(i=0;i<D;i++)
      {
         cin>>inD;
         opo[inD[0]][inD[1]]=opo[inD[1]][inD[0]]='1';
      }
       scanf("%d",&N);
       cin>>S;
       string ans="";


       for(i=0;i<N;i++)
       {
           if(ans.size()==0) ans+=S[i];
           else
           {
               int sz=ans.size()-1;
               if(isalpha(com[ans[sz]][S[i]]))
               {
                   ans[sz]=com[ans[sz]][S[i]];
               }
               else
               {
                   for(j=sz;j>=0;j--)
                   {
                       if(opo[ans[j]][S[i]]=='1')
                       {
                         ans="";
                         break;
                       }

                   }
                    if(ans.size())
                    {
                        ans+=S[i];
                    }

               }
           }
       }
       string SS="";
       SS+='[';
       for(i=0;i<ans.size();i++)
       if(i!=(ans.size()-1)){
        SS+=ans[i];SS+=',';SS+=' ';}
        else SS+=ans[i];
        SS+=']';
      printf("Case #%d: ",cas++);
      cout<<SS<<endl;
    }

  return 0;
}
