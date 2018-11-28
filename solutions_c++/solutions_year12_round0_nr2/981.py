#include<iostream>

using namespace std;

int googlers, surprising_results, best_score;
int scores[1000];

int solve()
{
  int i,j,k;
  int count=0;
  for(i=0;i<googlers;i++)
    {
      int t = 3*best_score-2;
      if(scores[i] >= max(0,t>=0 ? t : t+2)) 
	count ++;
      else if(surprising_results && scores[i] >= 3*best_score -4 && 3*best_score-4>=0)
	surprising_results--, count++;
    }
  return count;
}

int main()
{
  int n;
  int i,j,k;
  cin >> n;
  for(i=0;i<n;i++)
    {
      cin >> googlers;
      cin >> surprising_results;
      cin >> best_score;

      for (j=0;j<googlers;j++) 
	cin >> scores[j];

      cout << "Case #" << i+1 << ": " << solve() << endl;;
    }

      
}
