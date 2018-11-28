#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int time(char* ch)
{
  return ((ch[4]-'0')+10*(ch[3]-'0')+60*(ch[1]-'0')+600*(ch[0]-'0'));
}

int main()
{
  int tt,nn;
  scanf("%d ",&nn);
  for(tt=1;tt<=nn;tt++)
  {
    int t,na,nb;
    scanf("%d %d %d ",&t,&na,&nb);
    vector<pair<int,int> > a,b;
    char t1[8],t2[8];
    for(int i=0;i<na;i++)
    {
      scanf("%s %s ",t1,t2);
      a.push_back(make_pair(time(t1),1));
      b.push_back(make_pair(time(t2)+t,-1));
    }
    for(int i=0;i<nb;i++)
    {
      scanf("%s %s ",t1,t2);
      b.push_back(make_pair(time(t1),1));
      a.push_back(make_pair(time(t2)+t,-1));
    }
    int ma=0,mb=0,sa=0,sb=0;
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    for(int i=0;i<a.size();i++) { sa+=a[i].second; ma>?=sa; }
    for(int i=0;i<b.size();i++) { sb+=b[i].second; mb>?=sb; }
    printf("Case #%d: %d %d\n",tt,ma,mb);
  }

  return 0;
}
