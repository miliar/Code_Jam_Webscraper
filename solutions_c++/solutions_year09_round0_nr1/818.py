#include <cstdio>
#include <vector>
#include <string>
using namespace std;

struct Wrd
  {
  Wrd();
  Wrd(string &s);
  int letters[20];
  };

Wrd::Wrd()
  {
  for(size_t i=0;i<20;++i)
    letters[i]=0;
  }

Wrd::Wrd(string &s)
  {
  for(size_t i=0;i<s.size();++i)
    {
    letters[i]=(1<<(s[i]-'a'));
    }
  }

int main()
  {
  int L,D,N;

  vector<Wrd> words;

  scanf("%d %d %d\n",&L,&D,&N);
  for(int d=0;d<D;++d)
    {
    char buf[256];
    gets(buf);
    string s(buf);
    Wrd wrd(s);
    words.push_back(wrd);
    }

  for(int n=0;n<N;++n)
    {
    char buf[1024];
    gets(buf);
    string s(buf);
    vector<string> vs;

    int l=0;
    string s2;
    for(size_t i=0;i<s.size();++i)
      {
      if (s[i]=='(') ++l; else
        if (s[i]==')') {--l;vs.push_back(s2);s2="";} else
          if (l==0) vs.push_back(string(1,s[i])); else
            s2.append(string(1,s[i]));
      }

    Wrd pattern;
    for(size_t i=0;i<vs.size();++i)
      for(size_t j=0;j<vs[i].size();++j)
        pattern.letters[i]=pattern.letters[i] | (1<<(vs[i][j]-'a'));

    int ret=0;
    for(size_t i=0;i<words.size();++i)
      {
      bool match=true;
      for(size_t j=0;j<L;++j)
        {
        Wrd &wrd = words[i];
        if ((wrd.letters[j] & pattern.letters[j])==0)
          {match=false;break;}
        }

      if (match) ++ret;
      }

    printf("Case #%d: %d\n", n+1, ret);
    }

  return 0;
  }