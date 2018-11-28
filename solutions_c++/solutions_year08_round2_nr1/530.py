#include <iostream>
#include <sstream>
#include <string>
#include <vector>
template<class T>
void Get(T &a)
{
  std::string s;
  std::getline(std::cin, s);
  std::istringstream is(s);
  is >> a;
}


struct point
{
  long  x,  y;
};






int main(int argc, char **argv)
{
  long int N;
  long int n, A, B, C, D, x0, y0, M;
  Get(N);
  for (int r = 1; r <= N;++r)
  {
    std::cin >> n >> A >> B >> C >> D >> x0 >> y0 >>M;
    std::vector<point> v;
    v.resize(n);
    v[0].x = x0;
    v[0].y = y0;
    for (int i = 1; i <n; ++i)
    {
      v[i].x = (A * v[i-1].x + B)%M;
      v[i].y = (C * v[i-1].y + D)%M;
    }
    long int count = 0;
    for (int i = 0; i <n; ++i)
      for(int j = i+1; j <n; ++j)
	for(int k = j+1; k<n; ++k)
	{
	  long sx = v[i].x + v[j].x + v[k].x;
	  long sy = v[i].y + v[j].y + v[k].y;
	  if (((sx%3)==0) && ((sy%3)==0))
	    count++;
	}
    std::cout << "Case #" << r << ": " << count << std::endl;
  }
}

