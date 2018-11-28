#include <vector>
#include <fstream>
#include <iostream>
#include <bitset>
using namespace std;

int main(int argc,char* argv[])
{
	ifstream ifs(argv[1]);
	ofstream ofs(argv[2]);


	int T;
	ifs>>T;

		 
	 for(int i=1;i<=T;i++)
	 {
		 int R,k,N;
		 ifs>>R>>k>>N;
		 int g[1000];
		 int next[1000];
		 int opt[1000];
		 for(int j=0;j<N;j++)
			 ifs>>g[j];
		 int pivot=0;
		 
		 long long sum_g=0;
		 long long res=0;
		 for(int j=0;j<N;j++)
			 sum_g+=g[j];

		 if(sum_g<k)
			 res=sum_g*R;
		 else
		 {
		  
		 for(int j=0;j<N;j++)
		 {
			 pivot=j;
			 int count=0;
			 while(count+g[pivot]<=k)
			 {
			 count+=g[pivot];
			 pivot++;
			 if(pivot==N) pivot=0;
			 }
			 next[j]=pivot;
			 opt[j]=count;			 
		 }
		 pivot=0;
		 for(int j=0;j<R;j++)
		 {
			 res+=opt[pivot];
			 pivot=next[pivot];
		 }
		 
		
		/* for(int j=0;j<R;j++)
		 {
			 int count=0;
			 while(count+g[pivot]<=k)
			 {
			 count+=g[pivot];
			 pivot++;
			 if(pivot==N) pivot=0;
			 }
			 res+=count;			 
		 }
		 */

		 }

		ofs<<"Case #"<<i<<": "<<res<<endl;	 
	 }

	ifs.close();
	ofs.close();

}


