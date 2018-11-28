#include <fstream>
#include <iostream>
using namespace std;

typedef unsigned long long Integer;
Integer Calc(Integer N,Integer M);
int main(int argc,char* argv[])
{
	ifstream foo;
	char buf[0x200];
	sprintf(buf,"%s.in",argv[1]);
	foo.open(buf);
	if(foo.is_open()==false){
		cout<<"input file error!\n";
		return -1;
	}
	ofstream fout;
	sprintf(buf,"%s.out",argv[1]);
	fout.open(buf);
	int nCase=0;
	foo>>nCase;
	cout<<"Number of Case :"<<nCase+1<<endl;
	for(int i=0;i<nCase;i++){
		cout<<"Processing: "<<i+1<<"/"<<nCase<<endl;
		Integer N,M;
		foo>>N>>M;
		Integer result= Calc(N,M);
		if(result==0)
			fout<<"Case #"<<i+1<<": OFF"<<endl;
		else
			fout<<"Case #"<<i+1<<": ON"<<endl;
	}
	foo.close();
	fout.close();
}
Integer Calc(Integer N,Integer M)
{
	if(M==0)
		return 0;
	int MM=M+1;
	for(int i=0;i<N;i++){
		if(MM%2!=0)
			return 0;
		MM=MM/2;
	}
	return 1;
}

/*Integer Calc(Integer N,Integer M)
{
	if(M==0)
		return 0;
	int MM=M;
	for(int i=0;i<N-1;i++){
		MM=MM/2;
	}
	if(MM%2==0)
		return 0;
	else
		return 1;
}*/
// Integer Calc(Integer N,Integer M)
// {
// 	//N: number of socket;
// 	//M: number of snaps
// 	
// 	bool socket[30];
// 	for(int i=0;i<30;i++)
// 		socket[i]=false;
// 	for(int i=0;i<M;i++){
// 		int index=0;
// 		while(socket[index]){
// 			socket[index]= !socket[index];
// 			index++;
// 			if(index==N)
// 				break;
// 		}
// 	}
// }