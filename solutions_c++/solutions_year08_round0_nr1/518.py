#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;


int main()
{
	int N,S,Q;
	int c = 1;
	
   string engine[101];   
   string queries[1001];
   string query;
   int engine_index[101],index;
   
	unsigned long long M;
	
	freopen("A-small.in","r",stdin);
	scanf("%d",&N);

	while (N--)
	{
		// Read Input
		scanf("%d\n",&S);
		for (int i=0;i<S;i++)
		{
		   getline(cin, engine[i]);		   
		}
		
      memset(engine_index,0,sizeof(engine_index));
      
      scanf("%d\n",&Q);

      int count = 0;
      int switch_count = 0;
      
	   for (int i=0;i<Q;i++)
	   {
		   getline(cin, query);
		   index = 0;
		   
         for (int j=0;j<S;j++)
            if (!engine[j].compare(query))
               index = j;
               
         if (engine_index[index] == 0 ) count++ ;         
         if (count == S)
         {
            count = 1;         
            switch_count ++;
            memset(engine_index,0,sizeof(engine_index));
         }
         engine_index[index] = 1;
      }
      
      cout<<"Case #"<<c++<<": "<<switch_count<<endl;
	}	
	
	return 1;
}
