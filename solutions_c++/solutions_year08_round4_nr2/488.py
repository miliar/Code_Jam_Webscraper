#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

using namespace std;

int main()
{
   int T;
   cin>>T;
   
   int ans = 0;

   int N,M;

   ll A;
   int x[3],y[3];

   for (int c = 1;c<=T;c++)
   {
       cin >> N >>M >>A;	

	   bool flag = false;
	   x[0] = 0; y[1] = 0;
	   for (y[0] = 0;y[0]<=M;y[0]++)
		    for (x[1] = 0;x[1] <= N; x[1]++)
				for (x[2]= 0;x[2]<=N;x[2]++)
					for (y[2]=0;y[2]<=M;y[2]++)
					{
						int sum = 0;
						for (int j = 0;j<3;j++)
							sum += x[(j+1)%3]*y[j] - y[(j+1)%3]*x[j];
						sum = abs(sum);
						if (sum == A)
						{
							flag = true;
							printf("Case #%d:", c , ans);
							for (int j = 0;j<3;j++)
								cout<<' ' << x[j]<< ' ' << y[j];
							printf("\n");
							goto end;
						}
					}
	   //cout<<"hello"<<endl;
	   
end: if (!flag) printf("Case #%d: IMPOSSIBLE\n", c);
   }
   return 0;
}
