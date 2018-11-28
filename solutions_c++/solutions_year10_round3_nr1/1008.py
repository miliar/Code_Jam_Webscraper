#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int num_case;

  cin>>num_case;

  for(int i=0; i!=num_case; i++)
  {
    vector<int> A;
    vector<int> B;
    A.reserve(1001);
    B.reserve(1001);
    
    int N;

    int x;
    cin>>N;
    for(int j=0; j!=N ;j++)
      {
	cin>>x;
	A.push_back(x);
	cin>>x;
	B.push_back(x);
	
      }

    int count=0;
    
    for(int j=0; j!=N-1;j++)
      {
	for(int k=j+1; k!=N; k++)
	  {
	    if((A[j]<A[k] && B[j]>B[k]) || (A[j]>A[k] && B[j]<B[k]))
	      count++;
	  }
      }

    cout<<"Case #"<<i+1<<": "<<count<<endl;
	      
    
	  

  }

  return 0;
}

