#include <stdio.h>
#include <vector>

using namespace std;

#define W   0
#define L   1
#define NP -1

typedef long double DOUBLE;

struct Team
{
  vector<int> plays;
  int WPwin, WPplays;
  DOUBLE WP;
  DOUBLE OWP;
  DOUBLE OOWP;

  DOUBLE RPI;
};

int main()
{
  int t;
  scanf("%d",&t);
  char p[200];
  for (int i=1; i<=t; ++i)
    {
      int n;
      scanf("%d",&n);
      vector<Team> teams;
      teams.reserve(n);
      int j = n;
      while (j--)
        {
          Team t;
          scanf("%s",p);
          t.WPwin=0;
          t.WPplays=n;
          for (char* d = p; *d; ++d)
            {
              if (*d=='1')
                {
                  t.plays.push_back(W);
                  t.WPwin++;
                }
              else if (*d=='0')
                {
                  t.plays.push_back(L);
                }
              else
                {
                  t.plays.push_back(NP);
                  t.WPplays--;
                }
            }
          t.WP = (DOUBLE)t.WPwin/(DOUBLE)t.WPplays;
          teams.push_back(t);
        }
      for (j=0; j<n; j++)
        {
          DOUBLE OWPsum=0;

          for (int k=0; k<n; k++)
            {
              if (teams[j].plays[k]==W)
                OWPsum += (DOUBLE)teams[k].WPwin/(DOUBLE)(teams[k].WPplays-1);
              else if (teams[j].plays[k]==L)
                OWPsum += (DOUBLE)(teams[k].WPwin-1)/(DOUBLE)(teams[k].WPplays-1);
            }
          teams[j].OWP = OWPsum/teams[j].WPplays;
        }
      for (j=0; j<n; j++)
        {
          DOUBLE OOWPsum=0;

          for (int k=0; k<n; k++)
            {
              if (teams[j].plays[k]!=NP)
                OOWPsum += teams[k].OWP;
            }
          teams[j].OOWP = OOWPsum/teams[j].WPplays;
        }
      printf("Case #%d:\n",i);
      for (j=0; j<n; j++)
        {
          printf("%.10f\n",(double)(0.25*teams[j].WP+0.5*teams[j].OWP+0.25*teams[j].OOWP));
        }
    }
  return 0;
}
