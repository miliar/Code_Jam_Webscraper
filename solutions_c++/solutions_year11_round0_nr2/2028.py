#include<iostream>
using namespace std;
int t,c,d,n;
struct combine{
    char a,b,c;
}com[100];
struct opposed{
    char a,b;
}opp[100];
string check(string s)
{
    int i,j,k,h=s.size();
    bool flag=true;
    while(flag && s.size()>1){
        flag=false;
        for(i=0;i<c;i++)
        {
            if((s[h-2]==com[i].a && s[h-1]==com[i].b )||(s[h-2]==com[i].b && s[h-1]==com[i].a))
            {
                s[h-2]=com[i].c;
                h--;
                flag=true;
            }
        }
    }
    string str="";
    for(i=0;i<h;i++) str+=s[i];
    s=str;
    for(i=0;i<d;i++)
    {
        for(j=0;j<h;j++)
        if(s[j]==opp[i].a)
        {
            for(k=j;k<h;k++) if(s[k]==opp[i].b)
            {
                s="";
                return s;
            }
        }else if(s[j]==opp[i].b)
        {
            for(k=j;k<h;k++) if(s[k]==opp[i].a)
            {
                s="";
                return s;
            }
        }
    }
    return s;
}
int main()
{
    freopen("B-large.in","r",stdin);
   freopen("B.out","w",stdout);
   scanf("%d",&t);
   char s[1000];
   int i,j,h;
   for(i=1;i<=t;i++)
   {
       scanf("%d",&c);
       for(j=0;j<c;j++)
       {
           scanf("%s",s);
           //cout<<s<<endl;
           com[j].a=s[0];
           com[j].b=s[1];
           com[j].c=s[2];
       }
       scanf("%d",&d);
       for(j=0;j<d;j++)
       {
           scanf("%s",s);
         //  cout<<s<<endl;
           opp[j].a=s[0];
           opp[j].b=s[1];
        }
       scanf("%d",&n);
       scanf("%s",s);
      // cout<<s<<endl;
       h=strlen(s);
       string str="";
       str+=s[0];
      // cout<<str;
       for(j=1;j<h;j++)
       {
           str+=s[j];
           if(str.size()>1)
           {
               //cout<<str<<endl;
               str=check(str);
              // cout<<"~~"<<str<<endl;
           }
       }
       printf("Case #%d: [",i);
       h=str.size();
       if(h>0)
       {
        for(j=0;j<h-1;j++)
        printf("%c, ",str[j]);
        printf("%c",str[h-1]);
       }
       printf("]\n");
    }

}
