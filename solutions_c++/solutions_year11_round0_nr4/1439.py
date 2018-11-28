#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

void print( const vector<float> & v);
int free(const vector<float> & array, const vector<float> & sorted);

float N;
int T=1, TC;
int  LC;

int main()
{
  for(scanf("%d ", &TC);T<=TC; ++T)
  {
    int L=0;
    vector<float> array;
    for(scanf("%d ", &LC); L<LC;++L)
    {
      scanf("%f ", &N);
      array.push_back(N);
    }
    vector<float> sorted;
    sorted = array;
    vector<float>::iterator it = sorted.begin();
    sort(it, it+sorted.size());
    //print(sorted);
    //print(array);
    int n, x, h;
    float e;
    n=array.size();
    cout << "Case #" << T <<": ";
    cout << float(free( array, sorted)) << endl;

  }
}

void print( const vector<float> & v)
{
  cout <<"Case #" << T << ": ";
  cout << "[";
  int i = 0;
  if(!v.size()==0)
  {
  while (i<v.size()-1)
  {
    cout << v[i] << ", ";
    ++i;
  }
  cout << v.back();
  }
  cout << "]"<< endl;

}

int free(const vector<float> & array, const vector<float> & sorted)
{
  int hold=0;
  for(int i = 0; i<array.size();++i)
  {
    if(array[i]==sorted[i])
      ++hold;
  }
  int free = array.size()-hold;
  return free;
}
