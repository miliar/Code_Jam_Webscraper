#include <stdio.h>
#include <vector>
#include <string.h>

class lit
{
private:
  char cnst;
public:
  lit() {};
  lit(char znak) {cnst=znak;}
  virtual bool matches(char znak) {
    return cnst==znak;
  }
};

class pat: public lit
{
private:
  bool list[256];
public:
  pat(char* strin, unsigned int* add) {
    memset(list,0,256);
    while (strin[0]!=')')
    {
      list[strin[0]]=true;
      strin++;
      (*add)++;
    }
  }
  bool matches(char znak) {
    return list[znak];
  }
};

struct hnus {char a[16];};

int main(int argc, char *argv[])
{
  FILE* in=fopen("A-large.in","r");
  FILE* out=fopen("A-large.out","w");
  int l,d,n;
  fscanf(in,"%i %i %i",&l,&d,&n);

  std::vector<hnus> dic;


  for (int i=0;i<d;i++)
  {

    hnus tmp;

    fscanf(in,"%s",tmp.a);

    dic.push_back(tmp);
  }


  for (int i=0;i<n;i++)
  {
    char tmp[2048];
    
    memset(tmp,0,2048);
    fscanf(in,"%s",tmp);

    std::vector<lit*> pattern;

    char* x=&tmp[0];
    while (x[0]!=0)
    {
      if (x[0]=='(') {
        x++;
        unsigned int add=1;
        pattern.push_back(new pat(x,&add));
        x+=add;
      } else {
        pattern.push_back(new lit(x[0]));
        x++;
      }
    }

    unsigned int ok=0;

    for (int y=0;y<d;y++)
    {
      ok++;
      for (int p=0;p<l;p++)
      {
        if (!pattern[p]->matches(dic[y].a[p])) {ok--;break;}
      }
    }

    fprintf(out,"Case #%u: %u\n",i+1,ok);
  }

  fclose (in);
  fclose (out);

}