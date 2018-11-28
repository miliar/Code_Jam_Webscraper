#include <iostream>
#include <cstdio>

using namespace std;

char search_engines[100][110];
int v_distance[100];
int num_dist_evaluated;
char query_list[1000][110];
int S, Q;

int evaluate_distance_from(int index_in_query)
{
   // initialize
   for(int i=0;i < S;i++) v_distance[i] = -1; 
   num_dist_evaluated = 0;

   for(int j=index_in_query;j < Q && num_dist_evaluated < S;j++)
   {
      for(int i=0;i < S;i++)
      {
         if((strlen(query_list[j]) == strlen(search_engines[i])) && (strcmp(query_list[j], search_engines[i]) == 0))
         {
            if(v_distance[i] != -1) break;
            v_distance[i] = j - index_in_query;  // 
            num_dist_evaluated++; 
         } 
      }
   }

   // find maximum distance
   int max_index = 0;
   int max_dist = 0;
   for(int i=0;i < S;i++) 
   {
      if(v_distance[i] == -1)
         return i;
      if(v_distance[i] > max_dist)
      { max_dist = v_distance[i]; max_index = i; }
   }
   return max_index;
}

int get_minimum_switches(void)
{
   int engine_index = 0;
   int num_switches = 0;
   int query_index = 0;

   /* First choice.. */
   engine_index = evaluate_distance_from(0);
   while(v_distance[engine_index] != -1) /* end of switching condition */
   {
      query_index += v_distance[engine_index];
      engine_index = evaluate_distance_from(query_index);
      num_switches++;
   }

   return num_switches;
}

int main(void)
{
   int N;
   scanf("%d\n", &N);

   for(int i=1;i <= N;i++)
   {
      scanf("%d\n", &S);
      for(int j=0;j < S;j++)
      {
         gets(search_engines[j]);
         // printf("%s\n", search_engines[j]);
      }

      scanf("%d\n", &Q);
      for(int j=0;j < Q;j++)
      {
         gets(query_list[j]);
         // printf("%s\n", query_list[j]);
      }

      printf("Case #%d: %d\n", i, get_minimum_switches());
   }
   return 0;
}
