#include<iostream>
#include<string>
using namespace std;
char C[40][3];
char D[40][2];

int main()
{
  int t , c , d , n; 
  int count = 0;
  string N, result;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    result = "";
    cin >> c;
    for (int j = 0; j < c; j++)
      cin >>C[j][0] >> C[j][1] >> C[j][2];
    cin >> d;
    for (int j = 0; j < d; j++)
      cin >>D[j][0] >> D[j][1];
    cin >> n >> N;
    
    for (int j = 0; j < n; j++)
    {
      result += N[j];
      int length = result.length();
      if (length>=2)
        for (int k =0; k < c; k++)
          if ((result[length-2] == C[k][0] && result[length-1] == C[k][1])||(result[length-2] == C[k][1] && result[length-1] == C[k][0]))
          {
            result.erase(length-2,2);
            result += C[k][2];
            length --;
          }
      if (length>=2)
        for (int k =0; k < d; k++)
          if (result.find(D[k][0]) != string::npos 
           && result.find(D[k][1]) != string::npos)
          {
            result = "";
          }
    }    
    
    
    cout << "Case #" << ++count << ": [";
    if (result.length() > 1)
    for (int m = 0; m < result.length()-1; m++)
      cout << result[m] <<", ";
    if (result.length() > 0)
      cout << result[result.length()-1];
      cout << "]" <<endl;
  }
}

