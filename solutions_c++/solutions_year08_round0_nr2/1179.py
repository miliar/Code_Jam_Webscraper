#include <stdio.h>
#include <queue>
#include <iostream>
using namespace std;

int getint(char* S)
{
     return ((S[0] - '0')*10 + S[1] - '0')*60 + (S[3] - '0')*10 + S[4] - '0';
}

int main()
{
     int Q; scanf("%d\n", &Q);
     for (int qqq = 0; qqq < Q; qqq++)
     {
           int trains[2] = {0, 0};
           
           int T;
           scanf("%d\n", &T);
           int NA, NB;
           scanf("%d %d\n", &NA, &NB);
           
           priority_queue<int> arr[2];
           priority_queue<pair<int, pair<int, int> > > q;
           
           for (int i = 0; i < NA; i++)
           {
               char Sa[6], Sb[6];
               scanf("%s %s\n", Sa, Sb);
               q.push(make_pair( -getint(Sa), make_pair( getint(Sb), 0 ) ) );
           }
           for (int i = 0; i < NB; i++)
           {
               char Sa[6], Sb[6];
               scanf("%s %s\n", Sa, Sb);
               q.push(make_pair( -getint(Sa), make_pair( getint(Sb), 1 ) ) );
           }
           
           while (!q.empty())
           {
                 int side = q.top().second.second;
                 int dep = -q.top().first;
                 int arrive = q.top().second.first;
                 q.pop();
                         
                 if (arr[side].empty() || -arr[side].top() + T > dep) trains[side]++; 
                 else arr[side].pop();
                 
                 arr[side^1].push(-arrive);
           }
           printf("Case #%d: %d %d\n", qqq + 1, trains[0], trains[1]);
     }
     
     
}
