#include <iostream>
#include <deque>
#include <algorithm>
#include <iterator>

#define PRINT(a) cout << #a << " = " << (a) << endl

using namespace std;

deque<char> order;
deque<int> o_seq;
deque<int> b_seq;

template < typename T > void printList( const deque<T> &l )
{
  ostream_iterator<T> output( cout, " " );
  copy( l.begin(), l.end(), output );
}

void dump()
{
return;
  printList(order);
  cout << endl;
  printList(o_seq);
  cout << endl;
  printList(b_seq);
  cout << endl;
}

void prepare_input()
{
  order.clear();
  o_seq.clear();
  b_seq.clear();

  int button_cnt   = 0;

  int last_o_button_num = 1;
  int last_b_button_num = 1;

  char bot_color;
  int button_num;

  cin >> button_cnt;
  for ( int i = 0; i < button_cnt; ++i )
  {
    cin >> bot_color;
    cin >> button_num;

    switch( bot_color )
    {
      case 'O': 
        order.push_back( 'O' );
        o_seq.push_back( abs( button_num - last_o_button_num ) + 1 );
        last_o_button_num = button_num;
        break;
      case 'B':
        order.push_back( 'B' );
        b_seq.push_back( abs( button_num - last_b_button_num ) + 1 );
        last_b_button_num = button_num;
        break;
      default:
        abort();
    }
  } 

  o_seq.push_back( 0 );
  b_seq.push_back( 0 );

}

int play_algo( deque<int>& first, deque<int>& second )
{
  int seconds = 0;
  
  if ( 0 == first.front() ) 
  {
    cout << "smth's wrong\n";
    abort();
  } else {
    int first_seq_element  = first.front();
    int second_seq_element = second.front();
    if ( second_seq_element > 1 ) 
    {
      if ( second_seq_element > first_seq_element )
      {
        second_seq_element -= first_seq_element;
      } else {
        second_seq_element = 1;
      }
    }
    first.pop_front();
    second.pop_front();
    second.push_front( second_seq_element );

    seconds = first_seq_element;
  }

  return seconds;
}

void solve_one_case( int case_num )
{
  int seconds = 0;
 
  for ( int i = 0; i < order.size(); ++i )
  {
//    PRINT(seconds);
    dump();
    switch( order[i] )
    {
      case 'O':
        seconds += play_algo( o_seq, b_seq );
        break;
      case 'B':
        seconds += play_algo( b_seq, o_seq );
        break;
      default:
        abort();
    }
  }
 
  cout << "Case #" << case_num << ": " << seconds << endl;
}

int main()
{
  int tc_cnt = 0;
  cin >> tc_cnt;
  for ( int i = 0; i< tc_cnt; ++i )
  {
    prepare_input();
    solve_one_case( i+1 );
  }
}
