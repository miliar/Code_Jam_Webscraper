#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;
int compute(int L, int P, int C)
{
	if(P<=L*C)
	return 0;

	int res=1;
	long long low=L;
	long long high=P;
	long long middle=(long long)(sqrt((double)L*(double)P)+1e-9);

	if (middle*middle<low*high)
		middle++;
	while (middle>C*low || high>C*middle)
	{
					
	high=middle;	
		
	middle=(long long)(sqrt((double)low*(double)high)+1e-9); 
	if (middle*middle<low*high)			middle++;
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
		 int L,P,C;
		 ifs>>L>>P>>C;
		 printf("%d %d %d\r\n",L,P,C);
	

		ofs<<"Case #"<<i<<": "<<compute(L,P,C)<<endl;	 
	 }

	ifs.close();
	ofs.close();

}



