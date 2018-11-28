#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
  // just do this, write vector<the type you want,
  // in this case, integer> and the vector name
  vector<long> v1;
  vector<long> v2;
  
  int T,I,n,K;
  // try inserting 7 different integers, not ordered
  scanf("%d",&T);
  
  long temp;
  long producto=0;
	for (I=0;I<T;I++)
	{
		v1.clear();
		v2.clear();
		scanf("%d",&n);
		for (K=0;K<n;K++)
	  		{
	  		scanf("%ld",&temp);
	  		v1.push_back(temp);
			}
		for (K=0;K<n;K++)
	  		{
	  		scanf("%ld",&temp);
	  		v2.push_back(temp);
			}
	
	sort(v1.begin(),v1.end()); 
	
	sort(v2.begin(),v2.end()); 
	
	vector<long>::iterator i;
	vector<long>::iterator j;
	
	for (i = v1.begin(),j = v2.end()-1 ; i!= v1.end(); i++,j--)
	{
		producto+=(*i)*(*j);
		//printf("%ld ",producto);
		
		//printf("%d ",*j);
		
		
	}
	printf("Case #%d: %ld\n",I+1,producto);
	producto=0;
	
	}
	
	
	//sort(v2.end(),v2.begin()); 
	
	
/*	vector<int>::iterator i;
	
	printf("Sorted version2\n");
  	for (i = v2.begin(); i!= v2.end(); i++)
    printf("%d ",*i); // iterator's pointer hold the value
  printf("\n");
	*/
  /*
  v.push_back(3); v.push_back(1); v.push_back(2);
  v.push_back(7); v.push_back(6); v.push_back(5);
  v.push_back(4);
  */
  
  
  // to access the element, you need an iterator...
  
  //printf("Unsorted version\n");
  // start with 'begin', end with 'end', advance with i++
  
  
  /*
  for (i = v.begin(); i!= v.end(); i++)
    printf("%d ",*i); // iterator's pointer hold the value
  printf("\n");
  sort(v.begin(),v.end()); // default sort, ascending
  printf("Sorted version\n");
  for (i = v.begin(); i!= v.end(); i++)
    printf("%d ",*i); // iterator's pointer hold the value
  printf("\n");
  printf("ReSorted version\n");
  for (i = v.end()-1 ; i>= v.begin(); i--)
    printf("%d ",*i); // iterator's pointer hold the value
  printf("\n");
  */
  
  
  return 0;
}
