#include <iostream>
#include <algorithm> 
#include <vector> 
#include <iterator> 
#include <stdlib.h> 

using namespace std;

int main()

{

vector<int> v;
vector<int> v2;


		
		
		int t;
		cin>>t;
		int next,n;
		int x=0;
		
		for(int i=0;i<t;i++)
		{ v.clear();
		v2.clear();
		  x=0;
		cin>>n;
		next=n;
        	
			v.push_back(0);
			while(n!=0)
			{
				//v.push_back(n%10);
				v2.push_back(n%10);
				x++;
				n/=10;
			}
			for(int j=x-1;j>=0;j--)
			        v.push_back(v2[j]);

		
  
  next_permutation(v.begin(), v.end());
  cout<<"Case #"<<(i+1)<<": ";
  if(v[0]!=0)
  cout<<v[0];
  for(int j=1;j<v.size();j++)
     {
               cout<<v[j];
               }
		cout<<endl;	
		} 




//system("PAUSE");

return 0;

}
