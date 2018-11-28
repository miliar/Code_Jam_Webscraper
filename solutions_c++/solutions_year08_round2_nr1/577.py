#include<iostream>
using namespace std;

int main()
{
   long long cases,i,j,k,l,m;
   cin >> cases;
   for (i = 0; i < cases; i++)
   {
      long long n, A, B, C, D, xo, yo, M, count=0;
      cin >> n >> A >> B >> C >> D >> xo >> yo >> M;
      long long treex[n], treey[n];
      treex[0] = xo;
      treey[0] = yo;
//      j = 0;
//         cout << "tree:" << j << " = " << treex[j] << "," << treey[j] << endl;
      for (j = 1; j <= n-1; j++)
      {
         treex[j] = (A * treex[j-1] + B) % M;
         treey[j] = (C * treey[j-1] + D) % M;
//         cout << "tree:" << j << " = " << treex[j] << "," << treey[j] << endl;
      }

      for (k = 0; k < n; k++)
	for (l = k+1; l < n; l++)
	   for(m = l+1; m < n; m++)
      {
            double xc = (treex[k] + treex[l] + treex[m]) / 3.0;
            double yc = (treey[k] + treey[l] + treey[m]) / 3.0;
//            cout << "xc = " << xc << ", yc = " << yc << endl;
            if ((xc == (long long)xc) && (yc == (long long)yc))
            count++;
      }
      cout << "Case #" << i+1 << ": " << count << endl;
   }
}
