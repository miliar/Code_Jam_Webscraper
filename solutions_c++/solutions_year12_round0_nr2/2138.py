#include <iostream>
#define LEN 31
#define FROM 2
#define TO 28
using namespace std;

int supr[LEN];
int unsupr[LEN];


int map(int N)
{
  int n = N/3;
  if(N%3==0)
  {
    unsupr[N] = n ;
    supr  [N] = n+1;
  }
  else if(N%3==1)
  {
    unsupr[N] = n+1;
    supr  [N] = n+1;
  }
  else if(N%3==2)
  {
    unsupr[N] = n+1;
    supr  [N] = n+2;   
  }  
}

void fill()
{
  for(int i = 0; i<LEN; i++)
    map(i);
}

int main()
{
  fill();
  int cases,num,sup,t,c,p;
  cin >> cases;
  for(int i = 0; i<cases; i++)
  {
    c = 0;
    cin >> num;
    cin >> sup;
    cin >> p;
    for(int j = 0; j<num; j++)
    {
      cin >> t;
      if(unsupr[t] >= p && unsupr[t] <= 10)
      {
	c++;
      }
      else if(t>=p && sup && t>=FROM && t<= TO && supr[t]>=p && supr[t] <= 10)
      {
	c++;
	sup--;
      }	
    }
    cout << "Case #" << i+1 << ": " << c << endl; 
  }
  return 0;
}