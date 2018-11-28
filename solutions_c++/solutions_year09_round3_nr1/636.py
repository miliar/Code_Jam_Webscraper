#include<iostream.h>
#include<string.h>
#include<fstream.h>

struct
{
  char sym;
  int val;
}db[40];

int main()
{
//  ifstream ip("ip.txt");
  ifstream ip("ipal.txt");
  ofstream op("op.txt");
  int tests,t,bs,a[70],i,j,k;
  long long raise,ans;
  char txt[70];
  ip>>tests;
  ip.getline(txt,70);
  for(t=1;t<=tests;t++)
  {
    ip.getline(txt,70);
    i=0; j=0;
    db[i].sym=txt[j];
    db[i].val=1;

    while(db[i].sym==txt[j]&&j<strlen(txt))
    a[j++]=1;
    i++;
    if(j<strlen(txt))
    {
      db[i].sym=txt[j];
      db[i].val=0;
      a[j]=0;
    }
    i++;
    j++;
    bs=2;
    while(j<strlen(txt))
    {
      for(k=0;k<i;k++)
      if(txt[j]==db[k].sym)
      break;
      if(k==i)
      {
        db[i].sym=txt[j];
        db[i].val=bs;
        a[j]=bs;
        i++;
        bs++;
      }
      else
      a[j]=db[k].val;
      j++;
    }
    raise=1;
    ans=0;
    for(k=strlen(txt)-1;k>=0;k--)
    {
      ans+=a[k]*raise;
      raise*=bs;
    }

//    cout<<"Case #"<<t<<": "<<ans<<endl;
    op<<"Case #"<<t<<": "<<ans<<endl;
  }
  ip.close();
  op.close();
//  getchar();
  return 1;
}
