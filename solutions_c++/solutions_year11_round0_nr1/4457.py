#include <cstdio>
#include <cmath>
using namespace std;

typedef struct tagROBOT 
{
  char type;
  int push;
} ROBOT;

int main()
{
  unsigned int idx = 1;
  unsigned int t = 0;
  unsigned int n[151] = {0,};
  unsigned int seq = 0;
  char type[151][151];
  ROBOT o[151][151];
  ROBOT b[151][151];
  int push = 0;
  int i = 0;
  int j = 0;

  for (i = 0; i < 151; ++i) 
  {
    for (j = 0; j < 151; ++j)
    {
      o[j][i].type = 'F';
      o[j][i].push = 0;
      b[j][i].type = 'F';
      b[j][i].push = 0;
      type[j][i] = 'F';
    }
  }

  scanf("%d",&t);
  int o_idx = 0;
  int b_idx = 0;
  for(idx = 0; idx < t; ++idx)
  {
    seq = 0;
    scanf("%d",&n[idx]);
    while (seq < n[idx])
    {
      scanf("%*c%c%d",&type[idx][seq],&push);
      if (type[idx][seq] == 'O') {
        o[idx][o_idx].type = type[idx][seq];
        o[idx][o_idx++].push = push;               
      }
      else {
        b[idx][b_idx].type = type[idx][seq];
        b[idx][b_idx++].push = push;
      }
      seq++;
    }
  }

  int result[151] = {0,};
  o_idx = 0;
  b_idx = 0;
  int o_cur = 0;
  int b_cur = 0;
  int move_o = 0;
  int move_b = 0;
  for (idx = 0; idx < t; ++idx)
  {
    o_cur = 1;
    b_cur = 1;
    seq = 0;
    while (seq < n[idx])
    {
      if (type[idx][seq] == 'O')
      {
		move_o = o[idx][o_idx].push - o_cur;
		if (b[idx][b_idx].type == 'B')
			move_b = b[idx][b_idx].push - b_cur;
		else
			move_b = 0;
		
		o_cur += move_o; 

        if (std::abs(move_o) > std::abs(move_b))
        {   
			if (b[idx][b_idx].type == 'B')
				b_cur += move_b;			
			result[idx] += std::abs(move_o); // move to button
			result[idx]++; // push			
        }
        else if (std::abs(move_o) < std::abs(move_b))
        {         			
          if (move_b > 0)
            b_cur += (abs(move_o) + 1);
          else
            b_cur -= (abs(move_o) + 1);
			result[idx] += std::abs(move_o);
			result[idx]++; // push	
        }
        else
        {
			b_cur += move_b;
			result[idx] += std::abs(move_o); // move to button
			result[idx]++;
        }		
        ++seq;
        ++o_idx;
      }
      else
      {
		if (o[idx][o_idx].type == 'O')
			move_o = o[idx][o_idx].push - o_cur;
		else
			move_o = 0;
		move_b = b[idx][b_idx].push - b_cur;

		b_cur += move_b; 

        if (std::abs(move_b) > std::abs(move_o))
        {   
			if (o[idx][o_idx].type == 'O')
				o_cur += move_o;			
			result[idx] += std::abs(move_b); // move to button
			result[idx]++; // push			
        }
        else if (std::abs(move_b) < std::abs(move_o))
        {         			
          if (move_o > 0)
            o_cur += (abs(move_b) + 1);
          else
            o_cur -= (abs(move_b) + 1);
			result[idx] += std::abs(move_b);
			result[idx]++; // push	
        }
        else
        {
			o_cur += move_o;
			result[idx] += std::abs(move_b); // move to button
			result[idx]++;
        }
        ++seq;
        ++b_idx;
      }
    }
  }

  for (idx = 0; idx < t; ++idx)
  {
    printf("Case #%d: %d\n", idx + 1, result[idx]);
  }

  getchar();

  return 0;
}
