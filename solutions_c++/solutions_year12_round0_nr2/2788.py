#include <iostream>

using namespace std;

//#define _DEB_

int tt[100];

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T, res;

	cin >> T;
	for(int t=1; t<=T; t++)
	{
	        #ifdef _DEB_ 
	           cout << "Test " << t << endl;
	        #endif
		/************************************
		*	Input Data
		*************************************/
		int N, S, P;
		cin >> N >> S >> P;
	        #ifdef _DEB_ 
		   cout << "N = " << N << " S = " << S << " P = " << P << endl;
		#endif
		for(int i=0; i<N; i++)
		{
		   cin >> tt[i];
       	           #ifdef _DEB_ 
       		      cout << "t[" << i << "] = " << tt[i] << endl;
       		   #endif
		}
		/************************************
		*	Solve the Problem
		*************************************/
		res=0;
		for(int i=0; i<N; i++)
		{
		   int q = tt[i]/3 + (tt[i]%3>0);
       	           #ifdef _DEB_ 
       		      cout << "   q = " << q << endl;
       		   #endif
		   // Условия достижения "best result":
		   // 1) "бесплатное"
		   if(q>=P) res++;
		   // 2) "платное"
		   else
		      if(q>0 && q==P-1 && S>0)
		      {
		         S--;
		         res++;
		      }
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
