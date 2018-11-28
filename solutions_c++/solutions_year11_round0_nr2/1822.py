#include "fstream.h"
using namespace std;
void main()
{
 ifstream inp("input.txt");
 ofstream oup("output.txt");
 int t;
 inp>>t;
 for (int r=1;r<=t;r++)
 {
  struct
  {
   char a; char b;
  } opp[100];
  char tra[256][256]={0};
  bool has[256]={0};
  char str[1000];
  char res[1000]={0};
  int c,o;
  inp>>c;
  for (int i=0;i<c;i++)
  {
   inp>>str;
   tra[str[0]][str[1]]=str[2];
   tra[str[1]][str[0]]=str[2];   
  }
  inp>>o;
  for (int i=0;i<o;i++)
  {
   inp>>str;
   opp[i].a=str[0];
   opp[i].b=str[1];
  }
  inp>>c>>str;
  for (int i=0;i<c;i++)
  {
   res[strlen(res)]=str[i];
   has[str[i]]=1;
   bool check=true;
   while (check&&strlen(res)>1)
   {
    check=false;
    if (tra[res[strlen(res)-1]][res[strlen(res)-2]]!=0)
    {
     char buf[2000]={0};
     for (int j=0;j<strlen(res)-2;j++)
      buf[j]=res[j];
     buf[strlen(buf)]=tra[res[strlen(res)-1]][res[strlen(res)-2]];
     strcpy(res,buf);
     for (int j='A';j<='Z';j++)
      has[j]=0;
     for (int j=0;j<strlen(res);j++)
      has[res[j]]=1;
     check=true;
    }
    bool cl=false;
    for (int j=0;j<o&&!cl;j++)
      if (has[opp[j].a]&&has[opp[j].b])
       cl=true;
    if (cl)
    {
     for (int j='A';j<='Z';j++)
      has[j]=0;
     int w=strlen(res);
     for (int j=0;j<w;j++)
      res[j]=0;
    }
   }
  }
  oup<<"Case #"<<r<<": [";
  for (int i=0;i<strlen(res);i++)
  {
   oup<<res[i];
   if (i!=strlen(res)-1)
    oup<<", ";
  }
  oup<<"]"<<endl;
 }
 oup.close();
 inp.close();
}
