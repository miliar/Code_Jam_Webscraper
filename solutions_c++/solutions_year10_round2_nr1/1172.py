#include<algorithm>
#include<cstdlib>
#include<set>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

int T,M,N,line;
set<string> exist;
vector<string> create,input;

void solve()
{
  typedef string::iterator SCI;

  for(int i=0;i<input.size();++i) {
      SCI p=input[i].begin();
      ++p;
      while(p!=input[i].end()) {
          if(*p=='/'){
              string str=string(input[i].begin(),p);
              if(exist.find(str)==exist.end()) {

                  exist.insert(str);
              }
          }
          ++p;
      }
      if(exist.find(input[i])==exist.end()) {

           exist.insert(input[i]);
      }
  }
  int count=0;
  for(int i=0;i<create.size();++i) {
      SCI p=create[i].begin();
      ++p;
      while(p!=create[i].end()) {
          if(*p=='/'){
              string str(create[i].begin(),p);
              if(exist.find(str)==exist.end()) {
                  count++;
                  exist.insert(str);
              }
          }
          ++p;
      }
      if(exist.find(create[i])==exist.end()) {
           count++;
           exist.insert(create[i]);
      }
  }
  create.clear();
  input.clear();
  exist.clear();
  printf("Case #%d: %d\n",line,count);

}

int main()
{
      freopen("E:\\³Ì±ó\\Round 1B 2010\\A\\A-large.in","r",stdin);
      freopen("E:\\³Ì±ó\\Round 1B 2010\\A\\A-large.out","w",stdout);
      scanf("%d",&T);
      for(line=1;line<=T;++line) {
              scanf("%d%d",&N,&M);
              for(int i=0;i<N;++i) {
                 string str;
                 cin>>str;
                 input.push_back(str);
              }
              for(int i=0;i<M;++i) {
                 string str;
                 cin>>str;
                 create.push_back(str);
              }
              solve();
      }
     // system("PAUSE");
      return 0;
}

