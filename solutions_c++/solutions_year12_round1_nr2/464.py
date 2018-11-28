#include <iostream>
#define maxn 1010
using namespace std;

int tn;
int n;
int a1[maxn],a2[maxn];
int s[maxn];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    cin >> tn;
    for (int t=1;t<=tn;t++)
    {
        cin >> n;
        for (i=0;i<n;i++)
            cin >> a1[i] >> a2[i];
        memset(s,0,sizeof s);
        int ans = 0;
        int star = 0;
        bool ansflg = true;
        while (star<2*n)
        {
              bool flag = false;
              do {
                  flag = false;
                  for (i=0;i<n;i++)
                      if (s[i]<2 && a2[i]<=star)
                      {
                          star += 2-s[i];
                          s[i] = 2;
                          ans++;
                          flag = true;
                      }
              } while (flag == true);
              
              if (star == 2*n)
                 break;
              
              int max2 = -1,mid = -1;
              for (i=0;i<n;i++)
                  if (!s[i] && a1[i]<=star && a2[i]>max2)
                  {
                      max2 = a2[i];
                      mid = i;
                  }
              if (star<2*n && mid == -1)
              {
                  ansflg = false;
                  break;
              }
              star += 1-s[mid];
              s[mid] = 1;
              ans++;
        }
        
        if (!ansflg)
        {
            cout << "Case #" << t << ": Too Bad" << endl;
        }
        else
        {
            cout << "Case #" << t << ": " << ans << endl;
        }
    }
}
