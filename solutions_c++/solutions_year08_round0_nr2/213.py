#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

struct event
{
   int type, x, y, z, num;
};

   bool operator < (event first, event other)
   {
      return (first.x<other.x || (first.x==other.x && first.y<other.y) || 
         (first.x==other.x && first.y==other.y && first.num<other.num));
   }


set <event> a;
event temp;
int k=1;

int main(void)
{
   int i, x, y, na, nb, T, ra, rb;
   //freopen("B-small-attempt0.in", "r", stdin);
   //freopen("B-small-attempt0.out", "w", stdout);
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);
   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      a.clear();
      scanf("%d%d%d\n", &T, &na, &nb);

      for (i=0; i<na; i++)
      {
         temp.type=0;
         scanf("%d:%d", &x, &y);
         temp.x=x*60+y;
         scanf("%d:%d", &x, &y);
         temp.y=x*60+y;
         temp.z=0;
         temp.num=k++;
         a.insert(temp);
      }
      for (i=0; i<nb; i++)
      {
         temp.type=0;
         scanf("%d:%d", &x, &y);
         temp.x=x*60+y;
         scanf("%d:%d", &x, &y);
         temp.y=x*60+y;
         temp.z=1;
         temp.num=k++;
         a.insert(temp);
      }

      na=0, nb=0;
      ra=0, rb=0;

      while (!a.empty())
      {
         temp.type=a.begin()->type;
         temp.x=a.begin()->x;
         temp.y=a.begin()->y;
         temp.z=a.begin()->z;
         fprintf(stderr, "%d %d %d %d\n", temp.type, temp.x, temp.y, temp.z);
         a.erase(a.begin());
         if (temp.type==0)
         {
            if (temp.z==0)
            {
               if (na==0) ra++;
               else na--;
            }
            else
            {
               if (nb==0) rb++;
               else nb--;
            }

            temp.type=1;
            temp.x=temp.y+T;
            temp.y=-1;
            temp.z=1-temp.z;
            temp.num=k++;
            a.insert(temp);
         }
         else
         {
            if (temp.z==0) na++;
            else nb++;
         }
      }
      fprintf(stderr, "\n");

      printf("Case #%d: ", tn+1);
      printf("%d %d\n", ra, rb);
   }
   return 0;
}
