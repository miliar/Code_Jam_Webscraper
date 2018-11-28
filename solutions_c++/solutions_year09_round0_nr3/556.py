// Welcome to CodeJam problem.

/* This is of course dynamic programming.  The recursive procedure is
   possibilities (ws, ms) which finds the number of times that
   welcome(ws:end) is a sequence in message(ms:end).  */

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>

static const char* welcome = "welcome to code jam";
static const int welcome_len = 19;
static const int max_msg_len = 500;
static const int modulo = 10000;

static int cache[welcome_len][max_msg_len];

static char message[max_msg_len + 2];

static int
possibilities (const int ws, const int ms)
{
  assert (ws >= 0 && ws <= welcome_len);
  assert (ms >= 0 && ms <= max_msg_len);

  /* If nothing needs to be found, take it as one hit.  */
  if (ws == welcome_len)
    return 1;

  /* If message is exhausted, no hit.  */
  if (ms == max_msg_len || !message[ms])
    return 0;

  if (cache[ws][ms] == -1)
    {
      // Don't take current character.
      cache[ws][ms] = possibilities (ws, ms + 1);

      // If current one matches, try that, also.
      if (welcome[ws] == message[ms])
        cache[ws][ms] += possibilities (ws + 1, ms + 1);

      // Do modulo.
      cache[ws][ms] %= modulo;
    }

  assert (cache[ws][ms] != -1);
  return cache[ws][ms];
}

static void
solve_case (const int num)
{
  fgets (message, sizeof (message), stdin);
  std::fill ((int*) cache, ((int*) cache) + welcome_len * max_msg_len, -1);

  const int cnt = possibilities (0, 0);

  char numbuf[5];
  sprintf (numbuf, "%4.d", cnt);
  for (int i = 0; numbuf[i]; ++i)
    if (numbuf[i] == ' ')
      numbuf[i] = '0';

  printf ("Case #%d: %s\n", num, numbuf);
}

int
main ()
{
  int n;
  scanf ("%d\n", &n);

  for (int i = 1; i <= n; ++i)
    solve_case (i);

  return EXIT_SUCCESS;
}
