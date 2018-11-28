#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
  int d;
  scanf("%d",&d);
  for (int p=1; p<=d; p++)
    {
      int n;
      scanf("%d",&n);
      int sum=0;
      int solut=0;
      int min=1000001;
      while (n--)
        {
          int a;
          scanf("%d",&a);
          solut^=a;
          sum+=a;
          if (a<min)
            min=a;
        }
      if (solut==0)
        printf("Case #%d: %d\n",p,sum-min);
      else
        printf("Case #%d: NO\n",p);
    }
  return 0;
}
