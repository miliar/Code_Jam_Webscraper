#include <iostream>
#include <algorithm>
#include <iterator>
#define INF 100000000
using namespace std;
int main()
{
   int n, len;
   int t = 0;
   int i;
   freopen("A-small-attempt1.in", "r", stdin);
   freopen("A-small-attempt1.out", "w", stdout);
   cin>>n;
   int x[900], y[900];
   int inx[900];
   while(n--)
   {
		scanf("%d", &len);
		for(i = 0; i < len; i++) cin>>x[i];
		for(i = 0; i < len; i++) 
		{
			cin>>y[i];
			inx[i] = i+1;
		}
		int  min = INF;
		do {
    	 int tmp = 0;
    	 for(i = 0; i < len; i++) tmp += x[i]*y[inx[i]-1];
    	 
    	 if(tmp < min) min = tmp;
   		}while( next_permutation(inx, inx+len));
   		
   		cout<<"Case #"<<++t<<": "<<min<<endl;
	}
   return 0;
}