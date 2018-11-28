#include<iostream.h>
#include<fstream.h>
#include<string.h>
#include<conio.h>

int main()
{
//  ifstream ip("ip.txt");
  ifstream ip("ipa.txt");
  ofstream op("op.txt");
  
  int l,d,n,i,j,t,tests,count,patlen,k,r,c;
  char dic[15005][17], ptrn[17][28],str[20000];
  
  ip>>l>>d>>tests;
  ip.getline(str,19990);
  for(i=0;i<d;i++)
  ip.getline(dic[i],16);

  for(t=0;t<tests;t++)
  {
    ip.getline(str,19990);
//    op<<"str : "<<str<<endl;

    count=0;
    r=0;
    c=0;
    for(i=0;i<strlen(str);i++)
    {
      c=0;
      if(str[i]=='(')
      {
        i++;
        while(str[i]!=')')
        ptrn[r][c++]=str[i++];
        ptrn[r][c]='\0';
      }
      else
      {
        ptrn[r][c++]=str[i];
        ptrn[r][c]='\0';
      }
      r++;
    }
/*    for(i=0;i<l;i++)
    op<<ptrn[i]<<"\n";*/
    for(i=0;i<d;i++)
    {
      for(k=0;k<l;k++)
      {
        patlen=strlen(ptrn[k]);
        for(j=0;j<patlen;j++)
        if(dic[i][k]==ptrn[k][j])
        break;
        if(j==patlen)
        break;
      }
      if(k==l)
      count++;
    }
    op<<"Case #"<<t+1<<": "<<count<<endl;
  }
  
//  getchar();
//  getch();

  ip.close();
  op.close();

  return 1;
}
