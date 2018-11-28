#include <iostream>
#include <fstream>
using namespace std;

//void Sort(const int* A, const int* B, int N)
//{
//	int min = a[0];
//	int minIndex = 0;
//	for(int i = 0; i<N-1; i++)
//	{
//		for(int j = i; j<N; j++)
//		{
//			if(a[j] < min)
//			{
//				min = a[j];
//				minIndex = j;
//			}
//			if(b[j] < min)
//			{
//				min = b[j];
//				minIndex = j;
//			}
//		}
//		swap(A[minIndex], A[i]);
//		swap(B[minIndex], B[i]);
//		min = 100000;
//		minIndex = -1;
//	}
//}

bool Intersect(int a1, int b1, int a2, int b2)
{
	if((a1 - a2) * (b1 - b2) < 0)
		return true;
	else
		return false;
}

int main () 
{
  string line;
  ifstream inFile("input.txt");
  ofstream outFile("C-small.out");
  int A[1000];
  int B[1000];
  int T;
  inFile>>T;
  for(int i = 0; i<T; i++)
  {
	  int ans = 0;
	  int N;
	  inFile>>N;
      for(int j = 0; j<N; j++)
	  {
		  inFile>>A[j]>>B[j];
	  }
	  //Sort(A,B);
	  for(int j = 0; j<N; j++)
	  {
		  for(int i = 0; i<N; i++)
		  {
			  if((i != j) && (Intersect(A[i], B[i], A[j], B[j])))
			  {
				  ans++;
			  }
		  }
	  }
	  ans /= 2;
	  outFile<<"Case #" << i+1 <<": " << ans << endl;
  }
  outFile.close();
  inFile.close();

  return 0;
}