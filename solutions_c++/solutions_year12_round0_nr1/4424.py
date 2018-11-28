#include<stdio.h>
#include<string.h>
#include<string>
#include<iostream.h>
   
  using namespace std; 
main()
{
  freopen("h.in","r",stdin);
  freopen("h.out","w",stdout);
  char a[30]={'y' ,'h' ,'e' ,'s' ,'o' ,'c' ,'v' ,'x' ,'d' ,'u' ,'i' ,'g' ,'l' ,'b' ,'k' ,'r' ,'z' ,'t' ,'n' ,'w' ,'j' ,'p' ,'f' ,'m' ,'a' ,'q'};
  int i,j,n;
  string str;
  scanf("%d",&n);
    getline(cin,str);
  for(i=1;i<=n;i++)
  
  {
    getline(cin,str);
    printf("Case #%d: ",i);
    for(j=0;j<str.size();j++)
      if('a'<=str[j] && str[j]<='z')printf("%c",a[str[j]-97]);
        else printf(" ");
    printf("\n");
  }
}
