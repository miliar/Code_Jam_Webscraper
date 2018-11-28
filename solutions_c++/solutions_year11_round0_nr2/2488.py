#include <iostream>
#include <algorithm>

using namespace std;

const int elemsize = 'Z'+1;
char rule[elemsize][elemsize];
const int NOOP = elemsize+1;
bool opposed[elemsize][elemsize];

char stack[101];
int top = -1;

void dmp()
{
  /*
    for (int i='A';i<elemsize;i++)
    {
      for (int j='A';j<elemsize;j++)
	cout << (rule[i][j]!=NOOP ? rule[i][j] : '.');
      cout << endl;
    }
  */
    cout << "[";
    for (int i=0;i<=top;i++)
    {
      cout << stack[i];
      if (i < top)
	cout << ", ";
    }
    cout << "]" << endl;
}


int main(void)
{
  int T;
  cin >> T;
  for (int t=1;t<=T;t++)
  {
    cout << "Case #" << t << ": ";
    for(int i=0;i<elemsize;i++) for(int j=0;j<elemsize;j++) rule[i][j] = NOOP;
    memset(opposed,0,elemsize*elemsize*sizeof(bool));
    for(int i=0;i<101;i++) stack[i] = NOOP;
    top = -1;
    int C;
    cin >> C;
    for (int i=0;i<C;i++)
    {
      char c1,c2,c3;
      cin >> c1 >> c2 >> c3;
      rule[c1][c2] = c3;
      rule[c2][c1] = c3;
      // cout << c1 << c2 << "->" << c3 << " ";
    }
    int D;
    cin >> D;
    for (int i=0;i<D;i++)
    {
      char c1,c2;
      cin >> c1 >> c2;
      opposed[c1][c2] = true;
      opposed[c2][c1] = true;
      // cout << c1 << c2 << " ";
    }
    int N;
    cin >> N;
    for (int i=0;i<N;i++)
    {
      char c;
      cin >> c;
      // cout << c;
      stack[++top] = c;
      while((top > 0) && (rule[stack[top]][stack[top-1]] != NOOP))
      {       
	// cout << "<" << stack[top-1] << stack[top]  << rule[stack[top]][stack[top-1]]  << ">"; 
	stack[top-1] = rule[stack[top]][stack[top-1]];
	top--;
      }
      for(int i=0;i<top;i++)
      {
	if(opposed[stack[top]][stack[i]])
	{
	  // cout << "X" <<  stack[top] << stack[i] << "X";
	  top = -1;
	  break;
	}
      }
    }
    dmp();
  }

  return 0;
}


