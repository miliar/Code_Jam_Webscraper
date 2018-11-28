#include <vector>
#include <fstream>
using namespace std;

int main(int argc,char* argv[])
{
	ifstream ifs(argv[1]);
	ofstream ofs(argv[2]);


	int T;
	ifs>>T;
	for(int i=1;i<=T;i++)
	{
		int N,K;
		ifs>>N>>K;
		vector<bool> status;		
		vector<bool> andstatus;

		status.resize(N+1);
		
		andstatus.resize(N+1);
		status[0]=true;
		andstatus[0]=true;
		
		for(int m=1;m<=N;m++)
			status[m]=false;
		for(int m=1;m<=N;m++)
		 {
		 andstatus[m]=andstatus[m-1]&status[m];
		 }
		for(int j=0;j<K;j++)
		{
			
		
		for(int m=1;m<=N;m++)
		{
		if(andstatus[m-1])
		status[m]=(!status[m]);
		}
			
		
		 for(int m=1;m<=N;m++)
		 {
		 andstatus[m]=andstatus[m-1]&status[m];
		 }
								   

		}

		if (andstatus[N])
		ofs<<"Case #"<<i<<": "<<"ON"<<endl;
		else
		ofs<<"Case #"<<i<<": "<<"OFF"<<endl;
	}


	ifs.close();
	ofs.close();

}

