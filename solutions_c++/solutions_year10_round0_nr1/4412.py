#include <iostream>
#include <fstream>
using namespace std;

int snapper(int N, int K)
{
	int power[30];
	power[0]=1;
	for (int i=1;i<N;i++)
		power[i]=0;
	int stage [30];
	for (int j=0;j<N;j++)
		stage[j]=0;
	int result=1;
	for (int k=1;k<=K;k++)
	{
		for (int i=0;i<N;i++){
			if (power[i]==1)
			stage[i]=1-stage[i];}
		int flag=0;
		for (int j=1;j<N;j++)
		{
			if (!flag){
				if (stage[j-1]==1) power[j]=1;
				else {power[j]=0;flag=1;}
			}
			else {power[j]=0;}
		}
	}
	for (int i=0;i<N;i++)
	{ if (stage[i]==0) result=0;
		//else result=1;
	}
	return result;
}
int main(int argc,char **argv)
{
 int num_case=0;
 int N=0;
 int K=0;
 //ifstream infile("A-small.in");
 ifstream infile(argv[1]);
 infile>>num_case;
 ofstream outfile("result.txt",ios_base::app);
 for (int ii=1;ii<=num_case;ii++){
	infile >> N >>K;
	if (snapper(N,K))
	{cout<< "Case #"<< ii <<": ON"<<endl;
	outfile<< "Case #"<< ii <<": ON"<<endl;}
	else{ cout<<"Case #"<< ii <<": OFF" <<endl;
		outfile<<"Case #"<< ii <<": OFF" <<endl;}

}
//	cout<<snapper(4,47)<<endl;
//	cout<<snapper(1,0)<<endl;
//cout<<snapper(1,1)<<endl;
//cout<<snapper(4,0)<<endl;
}
		 
  		
