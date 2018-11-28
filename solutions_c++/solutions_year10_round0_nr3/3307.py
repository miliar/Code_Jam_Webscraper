#include <fstream>
#include <iostream>
using namespace std;

typedef long Integer;
Integer Calc(Integer R,Integer k,Integer N,Integer* workspace);
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
		cout<<"Processing: "<<i<<"/"<<nCase<<endl;
		Integer R,k,N;
		foo>>R>>k>>N;
		Integer* workspace= new Integer [N];
		for(int j=0;j<N;j++){
			foo>>workspace[j];
		}
		Integer result= Calc(R,k,N,workspace);	
		fout<<"Case #"<<i+1<<": "<<result<<endl;
		delete[] workspace;
	}
	foo.close();
	fout.close();
}
Integer Calc(Integer R,Integer k,Integer N,Integer* g)
{
// 	if(N==1)
// 		return R*g[0];
	//R: time of coaster
	//k: capacity of coastr
	//N: number of group
	Integer Buffer=0;
	
	Integer iCnt=0; //count the number of people in the current time
	Integer ptr=0;
	Integer result=0;
	
	for(int i=0;i<R;i++){
		iCnt=0;
		Integer ptr0=ptr;
		while((iCnt+g[ptr])<=k ){
			iCnt+=g[ptr];
			ptr++;
			if(ptr==N)
				ptr=0;
			if(ptr==ptr0)
				break;
		}
		result+=iCnt;
		cout<<"\t Run:"<<i<<" "<<result<<endl;
	}
	
	return result;
}