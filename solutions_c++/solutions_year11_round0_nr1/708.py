#include<iostream>
using namespace std;
char a_col[101];
int a_no[101];

int main()
{
  int num = 0;
  int t, n;
  int no, b_pos, b_no, o_pos, o_no, step;
  char color, cur_color;
  cin >> t;
  for (int i =0; i< t; i++)
  {
    cin >> n;
    no = step = 0;
    b_pos = o_pos = 1;
    for (int j = 1; j<= n; j++)
    {
      cin >> cur_color >> no;
      a_col[j] = cur_color;
      a_no[j] = no;
    }
    for (int j = 1; j<= n; j++)
    {
      int N_B = 0;
      int N_O = 0;
      cur_color = a_col[j];
      no = a_no[j];

      for (int k = j; k <= n; k ++)
      {
        if (cur_color == 'B')
          if (a_col[k] == 'O')
          {
            N_O = a_no[k];
            break;
          }
        if (cur_color == 'O')
          if (a_col[k] == 'B')
          {
            N_B = a_no[k];
            break;
          }
      }
      int move;
      if(cur_color == 'B')
      {
        if (b_pos > no)
          move = b_pos-no + 1;
        else
          move = no-b_pos + 1;
        b_pos = no;
        step += move;
        if (N_O > o_pos)
        { 
          if (o_pos + move < N_O)
            o_pos += move;
          else
            o_pos = N_O;
        }
        else
        {
        if (o_pos - move > N_O)
            o_pos -= move;
          else
            o_pos = N_O;
        }
      }
      else
      {
        if (o_pos > no)
          move = o_pos-no + 1;
        else
          move = no-o_pos + 1;
        o_pos = no;
        step += move;
        if (N_B > b_pos)
        { 
          if (b_pos + move < N_B)
            b_pos += move;
          else
            b_pos = N_B;
        }
        else
        {
        if (b_pos - move > N_B)
            b_pos -= move;
          else
            b_pos = N_B;
        }
      }
    }
    cout << "Case #" << ++num <<": " << step << endl;
  }
}
