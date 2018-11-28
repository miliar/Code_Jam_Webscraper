#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int main()
{
int t;
cin >> t;
for(int i = 0 ; i < t ; i++)
  {
  int r, k, n, earned = 0;
  queue<int> int_que;
  cin >> r >> k >> n;
  for(int j = 0 ; j < n ; j++)
    {
    int q;
    cin >> q;
    int_que.push(q);
    }
  for(int m = 0 ; m < r ; m++)
    {
    int tmp = 0;
    vector<int> tmp_queue;
    for( ; ; )
      if(!int_que.empty())
	{
	int tmp_g;
	tmp += int_que.front();
	tmp_g = int_que.front();
	if(tmp <= k)
	  {
	  tmp_queue.push_back(tmp_g);
	  int_que.pop();
	  }
	else
	  {
	  tmp -= tmp_g;
	  earned += tmp;
	  for(int p = 0 ; p < tmp_queue.size() ; p++)
	    int_que.push(tmp_queue[p]);
	  break;
	  }
	}
      else
	{
	earned += tmp;
	for(int p = 0 ; p < tmp_queue.size() ; p++)
	  int_que.push(tmp_queue[p]);
	break;
	}
    }
  cout << "Case #" << i + 1 << ": " << earned << endl;
  }
return 0;
}