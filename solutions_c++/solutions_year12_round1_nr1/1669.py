#include<fstream>
#include<iomanip>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;

	int i,j,k,tNum;
	int a,b;
	double prob[3];
	double avr[4];
	double tmp=0;
	double sum;

	fin.open("A-small-attempt0.in");
	fout.open("output.txt");

	fin>>tNum;
	for(i=0; i<tNum; i++){
		fin>>a>>b;
		for(j=0; j<a; j++){
			fin>>prob[j];
		}
		avr[3]=b+2;
		tmp=0;
		sum=1;
		for(j=0; j<a; j++){
			sum*=prob[j];
		}
		tmp=sum*(b-a+1);
		tmp+=(1-sum)*(2*b-a+2);
		avr[0]=tmp;

		tmp=sum/prob[a-1]*(1-prob[a-1])+sum;
		avr[1]=tmp*(b-a+3)+(1-tmp)*(2*b-a+4);
		
		if(a<=2){
			avr[2]=b+3;

		}
		else{
			tmp=sum;
			tmp+=sum/prob[a-1]*(1-prob[a-1]);
			tmp+=sum/prob[a-1]/prob[a-2]*(1-prob[a-1])*(1-prob[a-2]);
			avr[2]=tmp*(b-a+5)+(1-tmp)*(2*b-a+6);

		}

		tmp=avr[0];

		for(j=1; j<4; j++){
			if(tmp>avr[j]){
				tmp=avr[j];
			}
		}

		fout<<::fixed;
		fout.precision(6);
		fout<<"Case #"<<i+1<<": "<<tmp<<endl;

		
	}




	fin.close();
	fout.close();

	return 0;
}