
#include <cassert>
#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;

unsigned long long groups[3002];
unsigned long long ride_groups[3001];
unsigned long long ride_people[3001];

unsigned long long people_accum[2000];
int visited[2000];

int r, k, n;

int determine_period(int & offset)
{
  int rounds = 0;
  int start = 0;
  people_accum[0] = 0;
  memset(visited, 0, sizeof visited);
  do
  {
    //printf("we can fit %d groups, starting at %d\n", ride_groups[start], start);
    //for (int i = 0; i < ride_groups[start]; i++)
    //  printf("%d ", groups[i + start]);
    //puts("");

    rounds++;
    people_accum[rounds] = people_accum[rounds - 1] + ride_people[start];

    visited[start] = rounds;
    start = (start + ride_groups[start]) % n;
    //printf("starting at %d\n", start);
  }
  while (!visited[start]);

  offset = visited[start] - 1;

  //printf("--- accum:\n");
  //for (int i = 0; i <= rounds; i++)
  //  printf("%d ", people_accum[i]);
  //  puts("");

  return rounds - offset;
}

void solve(int CASE)
{
  cin >> r >> k >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> groups[i];
    groups[i+n] = groups[i];
  }

  for (int i = 0; i < n; i++)
  {
    ride_groups[i] = 1;
    ride_people[i] = groups[i];
    for (int j = 1; j < n; j++)
      if (ride_people[i] + groups[i+j] <= k)
        ride_people[i] += groups[i+j],
        ride_groups[i]++;
      else
        break;
  }

  int offset = 0;
  int rounds = determine_period(offset);

  //printf("%d rounds with %d offset.\n", rounds, offset);

  unsigned long long int money = people_accum[min(r, offset)];
  //printf("%d rounds: %d people.\n", min(r, offset), money);

  if (r >= offset)
  {
    int periods = (r - offset) / rounds;
    unsigned long long int money_period = people_accum[offset + rounds] - people_accum[offset];
    //printf("%d periods, at %d per period: %d EUR\n", periods, money_period, periods*money_period);

    int final_offset = (r - offset) % rounds;
    unsigned long long int money_final = people_accum[offset + final_offset] - people_accum[offset];

    //printf("left %d rounds. won %d EUR.\n", final_offset, money_final);

    money += money_period * periods + money_final;
  }
  
  assert(money >= 0LL);
  printf("Case #%d: %llu\n", CASE, money);
}

int main()
{
  int t;
  cin >> t;

  for (int i = 1; i <= t; i++)
    solve(i);
  return 0;
}
