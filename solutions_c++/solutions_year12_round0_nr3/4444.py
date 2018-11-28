#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <fstream>
#include <set>
#include <unordered_map>
#include <pthread.h>

#define MAX_WIDTH 7 

using std::string;
using std::ifstream;
using std::ofstream;
using std::unordered_map;

unordered_map<int,unordered_map<int,int>> _G_bucket;

pthread_spinlock_t _G_lock;
char* __restrict__ _G_n_buf;
char* __restrict__ _G_m_buf; 

int configure(char* __restrict__, char* __restrict__, const int& inf, const int& sup);
int solve_pair(char* __restrict__, char* __restrict__, const int&, const int&);

struct inf_sup 
{
  int inf;
  int sup;
};

void* 
threaded_build(void* dat)
{
  struct inf_sup* infsup = (struct inf_sup*) dat;
  char* __restrict__ n_buf = (char* __restrict__)malloc(sizeof(char* __restrict__)*MAX_WIDTH*2 + 1);
  char* __restrict__ m_buf = (char* __restrict__)malloc(sizeof(char* __restrict__)*MAX_WIDTH+1);

  int* ret = new int;
  *ret = configure(n_buf, m_buf, infsup->inf, infsup->sup);
  free(n_buf);
  free(m_buf);

  return (void*) ret;
}

int 
main(int argc, char* argv[])
{
  pthread_spin_init(&_G_lock, PTHREAD_PROCESS_PRIVATE);

  if (argc != 3)
    return 1;

  char* __restrict__ n_buf = (char* __restrict__)malloc(sizeof(char* __restrict__)*MAX_WIDTH*2 + 1);
  char* __restrict__ m_buf = (char* __restrict__)malloc(sizeof(char* __restrict__)*MAX_WIDTH+1);
  
  pthread_t p1[4];

  FILE* ifile = fopen(argv[1], "r");
  char buffer[MAX_WIDTH*2 + 1];
  fgets(buffer, MAX_WIDTH*2 +1, ifile);

  std::ofstream ofile(argv[2]);

  int q = atoi(buffer);
  std::cerr << "Count:" << q << std::endl;

  int i=0;
  int inf, sup;
  for (; i < q-4; i+=4)
    {
      fscanf(ifile, "%i %i", &inf, &sup); 
      struct inf_sup is0 = { inf, sup }; 
      pthread_create(&p1[0], NULL, threaded_build, (void*)&is0);
      
      fscanf(ifile, "%i %i", &inf, &sup); 
      struct inf_sup is1 = { inf, sup }; 
      pthread_create(&p1[1], NULL, threaded_build, (void*)&is1);
      
      fscanf(ifile, "%i %i", &inf, &sup); 
      struct inf_sup is2 = { inf, sup }; 
      pthread_create(&p1[2], NULL, threaded_build, (void*)&is2);
      
      fscanf(ifile, "%i %i", &inf, &sup); 
      struct inf_sup is3 = { inf, sup }; 
      pthread_create(&p1[3], NULL, threaded_build, (void*)&is3);
     
      for (int j=0; j<4 ;++j)
        {
          int* ret=new int;
          pthread_join(p1[j], (void**)&ret);
          ofile << "Case #" << i+j+1 << ": " << *ret << std::endl;
          delete ret;
        }
    }
  for (; i<q; ++i)
    {
      fscanf(ifile, "%i %i", &inf, &sup); 
      int ret = configure(n_buf, m_buf, inf, sup);
      ofile << "Case #" << i+1 << ": " << ret << std::endl;
    }

  ofile.close();
  fclose(ifile);
  free(n_buf);
  free(m_buf);
}


int 
configure(char* __restrict__ n_buf, char* __restrict__ m_buf, const int& inf, const int& sup)
{
  int perm_count=0;
  for (int i=inf; i<=sup; ++i)
    {
      for (int j=i+1; j<=sup; ++j)
        {
          perm_count += solve_pair(n_buf, m_buf, i, j);
        }
    }

  return perm_count;
}

inline int 
solve_pair(char* __restrict__ n_buf, char* __restrict__ m_buf, const int& n, 
           const int& m)
{
  if (_G_bucket.count(n) != 0 && 
      _G_bucket[n].count(m) != 0)
    return _G_bucket[n][m];
  sprintf(n_buf, "%d%d\0", n, n);
  sprintf(m_buf, "%d\0", m);
 
  int permutes = strlen(m_buf);

  for (int i=0; i<permutes; ++i)
    {
      if (n_buf[i] == m_buf[0])
        {
          if (0 == strncmp((char*)n_buf+i, m_buf, permutes))
            return 1;
        }
    }
  return 0;
}

