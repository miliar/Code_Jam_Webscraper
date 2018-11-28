#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxNotSurprising(int score)
{
  int max = 0;

  for(int a=0; a <= 10; ++a)
  {
    
    for(int b=a; b <= 10 && b-a <= 1; ++b)
    {
      for(int c=a; c <= 10 && c-a <= 1; ++c)
      {
        if(a+b+c == score)
        {
          max = std::max(max, std::max(b,c));
        }
      }
    }
    
  }
  
  return max;
}

int maxSurprising(int score)
{
  int max = 0;

  for(int a=0; a <= 10; ++a)
  {
    
    for(int b=a; b <= 10 && b-a <= 2; ++b)
    {
      for(int c=a; c <= 10 && c-a <= 2; ++c)
      {
        
        if(a+b+c == score)
        {
          max = std::max(max, std::max(b,c));
        }
      }
    }
    
  }
  
  return max;
  
  return max;
}


int main()
{
  int T;
  cin >> T;
  
  int numCases = 1;
  
  int N, S, p, score;
  
  int greaterP;
  
  
  while(numCases <= T)
  {
    cin >> N;
    cin >> S;
    cin >> p;
    
    greaterP = 0;
    
    for(int i=0; i < N; ++i)
    {
      cin >> score;
      
      //cout << score << ": " << maxNotSurprising(score) << "," << maxSurprising(score) << endl;
      
      if(maxNotSurprising(score) >= p)
      {
        ++greaterP;
      }
      else if(S > 0 && maxSurprising(score) >= p)
      {
        ++greaterP;
        --S;
      }
    }
    
    cout << "Case #" << numCases << ": " << greaterP << endl;
    ++numCases;
    
  }


  return 0;
}
