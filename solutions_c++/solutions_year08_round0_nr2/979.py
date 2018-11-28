#include <stdio.h>
#include <stdlib.h>

#define N 1000
#define INVAL 999999

struct timetable
{
  int id;
  int s, t;
} p[N];
int sta[N], stb[N], bota, botb;

int comp(const void *a, const void *b) 
{
  return ((struct timetable *)a)->s == ((struct timetable *)b)->s ? ((struct timetable *)a)->t - ((struct timetable *)b)->t : ((struct timetable *)a)->s - ((struct timetable *)b)->s;
}

inline int read_time()
{
  int h, m;
  scanf("%d:%d", &h, &m);
  return 60*h+m;
}

inline int topa()
{
  return bota > 0 ? sta[1] : INVAL;
}

inline void popa()
{
  int x, pa, ch;
  if(bota <= 0)return;
  x = sta[bota]; --bota;
  for(pa = 1, ch = 2; ch <= bota; pa = ch, ch <<= 1){
    if(ch+1 <= bota && sta[ch+1] < sta[ch]) ++ch;
    if(sta[ch] >= x) break;
    sta[pa] = sta[ch];
  }
  sta[pa] = x;
}

inline void pusha(int x)
{
  int pa, ch;
  ++bota;
  for(ch = bota, pa = (ch>>1); pa > 0; ch = pa, pa >>= 1){
    if(sta[pa] <= x) break;
    sta[ch] = sta[pa];
  }
  sta[ch] = x;
}

inline int topb()
{
  return botb > 0 ? stb[1] : INVAL;
}

inline void popb()
{
  int x, pa, ch;
  if(botb <= 0)return;
  x = stb[botb]; --botb;
  for(pa = 1, ch = 2; ch <= botb; pa = ch, ch <<= 1){
    if(ch+1 <= botb && stb[ch+1] < stb[ch]) ++ch;
    if(stb[ch] >= x) break;
    stb[pa] = stb[ch];
  }
  stb[pa] = x;
}

inline void pushb(int x)
{
  int pa, ch;
  ++botb;
  for(ch = botb, pa = (ch>>1); pa > 0; ch = pa, pa >>= 1){
    if(stb[pa] <= x) break;
    stb[ch] = stb[pa];
  }
  stb[ch] = x;
}

int main()
{
  int n, index;
  int t, i, j;
  int na, nb;
  int traina, trainb;
  
  scanf("%d", &n);
  for(index = 1; index <= n; index++){
    scanf("%d%d%d", &t, &na, &nb);
    for(i = 0; i < na+nb; i++) {
      p[i].id = i;
      p[i].s = read_time();
      p[i].t = read_time();
    }
    qsort(p, na+nb, sizeof(struct timetable), comp);
    bota = botb = 0; traina = trainb = 0;
    for(i = 0; i < na+nb; i++) {
      if(p[i].id < na){
        if(topb() + t <= p[i].s)
          popb();
        else
          traina++;
        pusha(p[i].t);
      } else {
        if(topa() + t <= p[i].s)
          popa();
        else
          trainb++;
        pushb(p[i].t);
      }
    }
    printf("Case #%d: %d %d\n", index, traina, trainb);
  }
  return 0;
}
