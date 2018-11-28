#include <iostream>
#include <fstream>

using namespace std;

int Exp(int n)
{
	int res =  1;
	for(int i=0; i<n; i++)
		res = res<<n;
	return res;
}

void main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout<<"usage error"<<endl;
		exit(0);
	}
	ifstream caseReader(argv[1]);
	ofstream resWriter(argv[2]);

	int nLine;
	caseReader>>nLine;

	int N;
	int K;
	for(int lid=1; lid<=nLine; lid++)
	{
		caseReader>>N;
		caseReader>>K;
		K++;
	
		bool isOn = true;
		for(int i=0; i<N; i++)
		{
			int bit = K&1;
			if(bit == 1)
			{
				resWriter<<"Case #"<<lid<<": OFF"<<endl;
				isOn = false;
				break;
			}
			K = K>>1;
		}
		if(isOn)
			resWriter<<"Case #"<<lid<<": ON"<<endl;
	}
	caseReader.close();
	resWriter.close();
}