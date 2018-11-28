#include <iostream>
#include <cstdlib>
using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main( int argc, const char* argv[] )
{
  int x, count;
  cin >> x;
  for (int i = 1; i<x+1; i++)
  {
    count = 0;
    int n, s, p, scores[200];
    cin >> n >> s >> p;
    for (int j=0; j < n; j++)
    {
      cin >> scores[j];
    }
    qsort(scores, n, sizeof(int), compare);
    for ( int j=0; j<n; j++)
    {
        if ((scores[j]-1)/3+1>=p && scores[j]>=p) count++;
        else if ((scores[j]-2)/3+2>=p && s>0 && scores[j]>=p)
        {
            count++;
            s--;
        }
        else break;
    }
    
    cout << "Case #" << i << ": " << count << endl;
  }
}