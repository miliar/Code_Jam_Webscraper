#include <stdio.h>
#include <vector>
using namespace std;


int main()
{
  int line;
  scanf("%d", &line);
  for(int i=0;i<line;i++)
  {
    int m;
    scanf("%d",&m);
    vector<int> v1;
    vector<int> v2;
    vector<char> clist;
    for(int j=0;j<m;j++)
    {
      char z;
     
      scanf("%c",&z);
      scanf("%c",&z);


//      printf("+%c+ ", z);

      int b;
      scanf("%d", &b);

      if(z == 'O')
      {
        v1.push_back(b);
        clist.push_back('O');
      }
      else
      {
        v2.push_back(b);
        clist.push_back('B');
      }

    }
/*
    printf("the first line\n");
    for(int j=0;j<v1.size();j++)
    {
      printf("O:%d ", v1[j]);
    }
    printf("\n");

   for(int j=0;j<v2.size();j++)
    {
      printf("B:%d ", v2[j]);
    }
    printf("\n");

    printf("=====\n");
*/

    int total = 0;
    int c1 = 1;
    int c2 = 1;

    int o1 = 0;
    int o2 = 0;
    for(int j=0;j<m;j++)
    {
      if(clist[j] != 'O')
      {
        int temp = abs(v2[o2] - c2) + 1;
        total += temp;
        c2 = v2[o2];

        if(o1 < v1.size())
        {
          if( temp >= abs(v1[o1] - c1) )
          {
            c1 = v1[o1];
          }
          else
          {
            if(c1 < v1[o1])
            {
              c1 += temp;
            }
            else c1 -= temp;
          }
        }
        o2 ++;
      }
      else
      {
        int temp = abs(v1[o1] - c1) + 1;
        total += temp;
        c1 = v1[o1];

        if(o2 < v2.size())
        {
          if( temp >= abs(v2[o2] - c2) )
          {
            c2 = v2[o2];
          }
          else
          {
            if(c2 < v2[o2])
            {
              c2 += temp;
            }
            else c2 -= temp;
          }
        }
        o1 ++;
      }

    }
    printf("Case #%d: %d\n",i+1,total);
  }
  return 0;
}


