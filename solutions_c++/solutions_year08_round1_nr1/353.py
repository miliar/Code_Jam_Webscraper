#include <iostream>
#include <algorithm>
#include <iterator>
#define INF 100000000
using namespace std;
int main()
{
   int n, len;
   int t = 0;
   freopen("in.txt", "r", stdin);
   freopen("o.txt", "w", stdout);
   cin>>n;
   int x[900], y[900];
   int inx[900];
   while(n--)
   {
		scanf("%d", &len);
		for(int i = 0; i < len; i++) cin>>x[i];
		for(int i = 0; i < len; i++) 
		{
			cin>>y[i];
			inx[i] = i+1;
		}
		int  min = INF;
		do {
    	 int tmp = 0;
    	 for(int i = 0; i < len; i++) tmp += x[i]*y[inx[i]-1];
    	 /*for(int i = 0; i < len; i++) cout<<y[inx[i]-1]<<" ";
    	 cout<<endl;*/
    	 if(tmp < min) min = tmp;
   		}while( next_permutation(inx, inx+len));
   		
   		cout<<"Case #"<<++t<<": "<<min<<endl;
	}
   return 0;
}
