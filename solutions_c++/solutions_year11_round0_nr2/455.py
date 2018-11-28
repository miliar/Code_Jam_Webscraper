#include<iostream>
#include<string>
#include<memory.h>
#include<algorithm>
using namespace std;
string h[1000],o[1000];
int main()
{
   int tcase,cas,c,d,n,j,k,i;
   string s,ans;
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   cin>>tcase;
   for(cas=1;cas<=tcase;cas++)
   {
	   cin>>c;
	   for(i=1;i<=c;i++)
		   cin>>h[i];
	   cin>>d;
	   for(i=1;i<=d;i++)
		   cin>>o[i];
	   cin>>n;
	   cin>>s;
       ans="";
	   for(i=0;i<s.length();i++)
	   {
		   if (ans=="") {ans=ans+s[i];continue;}
        char ch=s[i];
		bool fl=false;
		for(j=1;j<=c;j++)
		{
			if ((ch==h[j][0])&&(ans[ans.length()-1]==h[j][1]))
			{
				ans[ans.length()-1]=h[j][2];
				fl=true;
				break;
			}
				if ((ch==h[j][1])&&(ans[ans.length()-1]==h[j][0]))
			{
				ans[ans.length()-1]=h[j][2];
				fl=true;
				break;
			}
		}
		if (fl) continue;
		char opch;
		bool cl=false;
		for(j=1;j<=d&&(!cl);j++)
		{
			opch='#';
			if (ch==o[j][0]) {opch=o[j][1];}
			if (ch==o[j][1]) {opch=o[j][0];}
			if (opch!='#')
			{
              for(k=0;k<ans.length();k++)
				  if (ans[k]==opch)
				  {
					  ans="";
					  cl=true;
					  break;
				  }
			}
		}
		if ((!fl)&&(!cl))
			ans=ans+s[i];
	   }
      printf("Case #%d: [",cas);
	  //cout<<int(ans.length())-1<<endl;
	  for(j=0;j<int(ans.length())-1;j++)
	  {
         printf("%c, ",ans[j]);
	  }
	  if (ans.length()>0)
	    printf("%c]\n",ans[ans.length()-1]);
	  else printf("]\n");
   }
}
