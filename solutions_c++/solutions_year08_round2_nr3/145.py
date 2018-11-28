#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int main()
{
  int tc;
  cin >> tc;

  for(int z = 0; z < tc; z++)
  {
      int K, n;
      cin >> K;
      cin >> n;

      vector<int> faces;
      for(int i = 0; i < n; i++)
      {
	  int temp;
	  cin >> temp;
	  faces.push_back(temp - 1);
      }

      bool placed[K]; int pos[K];
      for(int i = 0; i < K; i++) placed[i] = false;

      pos[0] = 0; placed[0] = true;
      int cur = 0;
	  
      for(int i = 1; i < K; i++)
      {
	  //Placing the i-th card
	  int walked = 0;
	  while(walked < i + 1)
	  {
	      cur++;
	      if(cur == K) cur = 0;
	      if(!placed[cur]) walked++;
	  }
	  
	  pos[i] = cur;
	  placed[cur] = true;
      }

      int reverse[K];
      for(int i = 0; i < K; i++)
	reverse[pos[i]] = i;


      cout << "Case #" << z + 1 << ":";
      for(int i = 0; i < faces.size(); i++)
	  cout << " " << reverse[faces[i]] + 1;

      cout << endl;
  }
}
