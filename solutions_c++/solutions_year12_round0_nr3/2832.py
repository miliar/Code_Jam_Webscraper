#include <iostream>

using namespace std;

bool was_considered[2000001];

//#define _DEB_

/*
   Получить следующее число циклическим сдвигом
   (пропускаем числа, которые имеют ведущие нули)
*/
int shift(int i)
{
   int r,i0,count = 0;
   // считаем младшие нули
   while( (r = i%10)==0)
   {
      i = i/10;
      count++;
   }
   i = i/10;
   i0 = i;
   // считаем сколько остальных цифр
   while(i)
   {
      i = i/10;
      count++;
   }
   // сдвигаем бывшую младшую (ненулевую) цифру на count (десятичных) позиций влево
   while(count)
   {
      r = r*10;
      count--;
   }
   r = r+i0;
   return r;
}

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
		int A, B;
		cin >> A >> B;
	        #ifdef _DEB_ 
		   cout << "A = " << A << " B = " << B << endl;
		#endif
		/************************************
		*	Solve the Problem
		*************************************/
		int j0, j;
		memset(was_considered+A,false,B-A+1);
		res=0;
		for(int i=A; i<=B; i++)
		{
    	           #ifdef _DEB_ 
		      cout << "i = " << i << " res = " << res << endl;
		   #endif
		   if(!was_considered[i])
		   {
		      int n = 1;                          // длина цикла
		      was_considered[i] = true;
		      j0 = i;
		      while( (j = shift(j0))!=i )
		      {
		         #ifdef _DEB_ 
  		            cout << "   j = " << j << endl;
		         #endif
		         if(A<=j && j<=B && !was_considered[j])
		         {
		            was_considered[j] = true;
		            n++;
		         }
		         j0 = j;
		      }
		      res+=n*(n-1)/2;     // comb(n,2)
		   }
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
