
/**
 * Michael V. Antosha   (mivael)
 *
 * Michael.Antosha@gmail.com
 *
 * April 2013
 */

#include <iostream>
using std::clog;
using std::endl;
using std::flush;
using std::istream;

#include <string>
using std::string;

#include <vector>
using std::vector;

#include <cstring>  // memset

#include <cassert>

const int MIN_NUMBER_OF_CASES = 1;

const int BOARD_SIZE = 4;

const char CH_X = 'X';
const char CH_O = 'O';
const char CH_T = 'T';
const char CH_EMPTY = '.';

const string X_WON = "X won";
const string O_WON = "O won";
const string NOT_FINISHED = "Game has not completed";
const string DRAW = "Draw";

#ifdef SMALL_DATASET
const int MAX_NUMBER_OF_CASES = 10;
#endif
//
#ifdef LARGE_DATASET
const int MAX_NUMBER_OF_CASES = 1000;
#endif

struct Counters
{
public:
  int row[BOARD_SIZE];
  int col[BOARD_SIZE];
  int diag[2];  // [0] for the main diagonal,  [1] for the secondary one
public:
  Counters(void);
};

Counters::Counters(void)
{
  for (int i = 0;  i < BOARD_SIZE;  ++i)
      row[i] = col[i] = 0;

  diag[0] = diag[1] = 0;
}

static bool ensure_eol(istream& in)
{
  assert(in.good());
  string str;
  getline(in, str);
  assert(in.good());
  assert(str.empty());
  return true;
}

static int read_next_integer(istream& in)
{
  assert(in.good());
  int num;
  in >> num;
  assert(in.good());
  return num;
}

static int read_last_integer(istream& in)
{
  int num = read_next_integer(in);
  ensure_eol(in);
  return num;
}

static int read_tc_number(istream& in)
{
  int tc = read_last_integer(in);
  assert(MIN_NUMBER_OF_CASES <= tc  &&  tc <= MAX_NUMBER_OF_CASES);
  return tc;
}

static void read_next_word(istream& in, string& word)
{
  word.clear();
  assert(in.good());
  in >> word;
  assert(in.good());
}

static string read_a_row(istream& in, int len)
{
  string row;
  read_next_word(in, row);
  assert(row.size() == len);
  ensure_eol(in);
  // clog << "\t\t" << "read_a_row: row='" << row << "'." << endl;
  return row;
}

static inline
void check_victory(const int cnt1, const int cnt2,
		   const int N,
		   string& res, const string& victory_string)
{
  assert(0 <= cnt1  &&  cnt1 <= N);
  assert(0 <= cnt2  &&  cnt2 <= N);

  // if the result is known already then we have nothing to do
  if (res.size())  return;

  if (cnt1 == N  ||  cnt2 == N)
    res = victory_string;
}

int main(void)
{
  using std::cin;
  using std::cout;

  clog << "Hello." << endl;

  const int T = read_tc_number(cin);
  const int N = BOARD_SIZE;

  for (int tc = 1;  tc <= T;  ++tc)
    {
      clog << "Test case #" << tc << "..." << endl;

      int empty_squares = 0;  // counter for empty squares
      Counters x_cnt;  // all counters for player X
      Counters o_cnt;  // same for O
      vector<Counters*> counters;

      for (int rind = 0;  rind < N;  ++rind)  // row index
	{
          // clog << "\t" << "row #" << rind << "..." << endl;

	  string row = read_a_row(cin, N);
          // clog << "\t\t" << "row='" << row << "'." << endl;

	  for (int cind = 0;  cind < N;  ++cind)  // column index
	    {
	      const char ch = row[cind];
	      const bool main_diag = (rind == cind);
	      const bool sec_diag = (rind + cind == N - 1);

	      // whose counters to increment?
	      counters.clear();
	      switch (ch)
		{
		case CH_X:
		  counters.push_back(&x_cnt);
		  break;
		case CH_O:
		  counters.push_back(&o_cnt);
		  break;
		case CH_T:
		  counters.push_back(&x_cnt);
		  counters.push_back(&o_cnt);
		  break;
		case CH_EMPTY:
		  empty_squares++;
		  break;
		default:
		  assert(false);
		}

	      // increment counters
	      for (int i = counters.size() - 1;  i >= 0;  --i)  // once or twice
		{
		  assert(counters[i]);
		  Counters& cnt = *(counters[i]);
		  (cnt.col[cind])++;
		  (cnt.row[rind])++;
		  if (main_diag)  (cnt.diag[0])++;
		  if (sec_diag)   (cnt.diag[1])++;
		}
	    }
	}

      string res = "";  // game result

      // check for vertical/horizontal victories
      for (int i = 0;  i < N  &&  res.empty();  ++i)  // both column and row index
	{
	  check_victory(x_cnt.col[i], x_cnt.row[i], N, res, X_WON);
	  check_victory(o_cnt.col[i], o_cnt.row[i], N, res, O_WON);
	}

      // check for diagonal victories
      if (res.empty())
	{
	  check_victory(x_cnt.diag[0], x_cnt.diag[1], N, res, X_WON);
	  check_victory(o_cnt.diag[0], o_cnt.diag[1], N, res, O_WON);
	}

      if (res.empty())  // nobody won?
	{
	  if (empty_squares > 0)
	    res = NOT_FINISHED;
	  else
	    res = DRAW;
	}

      assert(res.size());
      cout << "Case #" << tc << ": " << res << endl;
    }

  return 0;
}
