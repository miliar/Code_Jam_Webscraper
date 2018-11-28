#include<fstream>
#include<iostream>
using namespace std;

int main()
{
  int n;
  ifstream filein("B-large.in");
  ofstream fileout("output.txt");
  streambuf *inbuf = cin.rdbuf(filein.rdbuf());
  streambuf *outbuf = cout.rdbuf(fileout.rdbuf());
  cin >> n;
  for(int i = 0; i < n; i++)
	{
    int m;
    int s;
    int p;
    int cnt = 0;
    cin >> m >> s >> p;
    int resn = 3 * p - 2;
    int ress = 3 * p - 4;
    for(int j = 0;j < m; j++)
		{
      int t;
      cin >> t;
      if(t >= resn)
          cnt++;
      else if(ress > 0 && t >= ress && s)
			{
        cnt++;
        s--;
      }
    }
    cout << "Case #" << i+1 <<": " << cnt << endl;
  }
  filein.close();
  fileout.close();
  cin.rdbuf(inbuf);
  cout.rdbuf(outbuf);
  return 0;
}
