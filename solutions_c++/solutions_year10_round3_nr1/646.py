#include <vector>
#include <fstream>
#include <iostream>

using namespace std;
int compute(vector<int> A, vector<int> B, int N)
{
int res=0;
for(int i=0;i<N;i++)
	for(int j=i+1;j<N;j++)
	{
		if(((A[i]>A[j])&&(B[i]<B[j]))||((A[i]<A[j])&&(B[i]>B[j])))
			res++;
	}
 return res;
}

int main(int argc,char* argv[])
{
	ifstream ifs(argv[1]);
	ofstream ofs(argv[2]);


	int T;
	ifs>>T;

		 
	 for(int i=1;i<=T;i++)
	 {
		 int N;
		 ifs>>N;
		 vector<int> A;
		 vector<int> B;
		 int Ai,Bi;
		 for(int j=0;j<N;j++)
		 {
			 ifs>>Ai>>Bi;
			 A.push_back(Ai);
			 B.push_back(Bi);
		 }
	

		ofs<<"Case #"<<i<<": "<<compute(A,B,N)<<endl;	 
	 }

	ifs.close();
	ofs.close();
}




