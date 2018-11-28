#include <iostream>
#include <string>
#include <queue>
#include <sstream>

using namespace std;

struct state
{
  int orange;
  int blue;
  state(int o, int b) { orange = o; blue = b;}
};

int main()
{
  int cases;
  cin >> cases >> ws ;
  for (int i = 1; i <= cases; i++)
  {
    int buttons;
    queue<int> os;
    queue<int> bs;
    queue<char> q;
    cin >> buttons;
    for (int j = 0; j < buttons; j++)
    {
       char c; int p;
       cin >> c >> p;
       if (c == 'O') os.push(p);
       else bs.push(p);
       q.push(c);
    }
    int time =0;
    state st(1, 1);
    while (!q.empty())
    {
       time++;
       //cerr << "time t = " << time << ": " << q.front() << ": " << os.front() << ": " << bs.front() << endl;
       bool is_blue = q.front()=='B';
       //cerr << is_blue << endl;
       if (!bs.empty())
       {
         if (st.blue > bs.front()) {
	    st.blue--;
	    //cerr << "blue moves to button " << st.blue << endl;
         }
         else if (st.blue < bs.front()) {
	   st.blue++;
	   //cerr << "blue moves to button " << st.blue << endl;
         }
         else if (is_blue)
         {
	   //cerr << "blue presses button " << st.blue << endl; 
	   q.pop();
	   bs.pop();
         }
         else
         {
	   //cerr << "blue stays at button " << st.blue << endl; 
         }
       }
       if (!os.empty())
       {
	 if (st.orange > os.front()) {
	   st.orange--;
	   //cerr << "orange moves to button " << st.orange << endl;
	  
         }
         else if (st.orange < os.front()) {
	   st.orange++;
	   //cerr << "orange moves to button " << st.orange << endl;
         }
         else if (!is_blue)
         {
           //cerr << "orange presses button " << st.orange << endl;
	   q.pop(); os.pop();
         }
         else 
	 {//cerr << "orange stays at button " << st.orange << endl;
	   
	 }
    
       }
    }
    cout << "Case #" << i << ": " << time << endl;
  }
}