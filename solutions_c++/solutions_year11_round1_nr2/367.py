#include <cstdio>
#include <cstring>

int N, M;
char W[100000][16];
char L[100][32];

inline void
read_input()
{
  scanf("%d %d", &N, &M);

  for (int i = 0; i < N; ++i)
    scanf("%s", W[i]);

  for (int i = 0; i < M; ++i)
    scanf("%s", L[i]);
}

int Lpos;
int size;
char game[16];
bool is_out[32];

inline bool
match(int w)
{
  if (strlen(W[w]) != size)
    return (false);

  for (int i = 0; i < size; ++i)
    if ((game[i] != '_' && game[i] != W[w][i]) ||
	(game[i] == '_' && is_out[W[w][i]-'a']))
      return (false);
  
  return (true);
}

inline bool
relevant(char c)
{
  for (int i = 0; i < N; ++i) {
    if (!match(i))
      continue;

    for (int j = 0; j < size; ++j)
      if (W[i][j] == c) {
	//	fprintf(stderr, "%c is relevant (appears in %s which matches %s)\n", c, W[i], game);
	return (true);
      }
  }

  return (false);
}

inline char
next_letter(int i)
{
  while (!relevant(L[i][Lpos]))
    ++Lpos;

  int p = Lpos;
  ++Lpos;

  return (L[i][p]);
}

inline int
nb_points_lost(int i, int w)
{
  int found = 0;
  int res = 0;

  while (found != size) {
    //    fprintf(stderr, "Cur game : %s\n", game);
    char c = next_letter(i);

    //    fprintf(stderr, "%c...", c);

    int count = 0;
    for (int j = 0; j < size; ++j)
      if (W[w][j] == c) {
	game[j] = c;
	++count;
      }
      is_out[c-'a'] = true;
    if (count == 0) {
      //      fprintf(stderr, "Not found in %s -- losing 1 point !\n",
      //    W[w]);
      //      fprintf(stderr, "(-1)\n");
      ++res;
    } else {
      found += count;
    }
  }

  //  fprintf(stderr, "--- lost %d points\n", res);

  return (res);
}

inline void
solve()
{
  for (int i = 0; i < M; ++i) {
    int res = 0;
    int max_loss = 0;

    //    fprintf(stderr, "Cur strategy : %s\n", L[i]);

    for (int w = 0; w < N; ++w) {
      //      fprintf(stderr, "Cur word : %s\n", W[w]);

      Lpos = 0;
      size = strlen(W[w]);
      for (int j = 0; j < 26; ++j)
	is_out[j] = false;

      for (int j = 0; j < size; ++j)
	game[j] = '_';
      game[size] = 0;
      
      int cur_loss = nb_points_lost(i, w);
      if (cur_loss > max_loss) {
	max_loss = cur_loss;
	res = w;
      }
    }
    printf(" %s", W[res]);
  }

  printf("\n");
}

int
main()
{
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i) {
    printf("Case #%d:", i + 1);

    read_input();
    solve();
  }

  return (0);
}
