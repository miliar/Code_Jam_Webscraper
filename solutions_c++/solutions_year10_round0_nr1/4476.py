#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main () {
	ifstream fin;
	ofstream  fout;
	char ch;
	fin.open("A-small-attempt2.in");
	fout.open("input.txt");
	while (fin){
		fin.get(ch);
		if (ch==' ') ch='\n';
		fout<<ch;
	}
	fin.close();
	fout.close();
	int T;
	
	ifstream f1;
	ofstream f2;
	f1.open("input.txt");
	//f2.open("output.txt");
	char temp[100];
	f1>>temp;
	
	T=atoi(temp);	
//	return 0;
	//cin>>T;
	int N[10001],K[10001];
	for (int j=0;j<T;j++) {
		//cin>>N[j]>>K[j];
		f1>>temp;
		N[j]=atoi(temp);				
		f1>>temp;
		K[j]=atoi(temp);
	}
	
	
	
	
	
	class snapper{
	public:
		int power;
		int state;
		snapper(){
			power=0;
			state=0;
			//cout<<"init";
		}
		
		void givepower(){
			power=1;
		}
		void takepower(){
			power=0;
		}
		void togglestate(){
						if (state==0) state=1;
				else if (state==1) state=0;
		}
			
	}snp[30];
	int n,k;
	for (int j=0;j<T;j++){
		n=N[j]; k=K[j];
		for (int q=0;q<=n;q++) snp[q].power=0;
		for (int q=0;q<=n;q++) snp[q].state=0;		
		
		
	snp[0].givepower();
/*	cout<<"\nStatIP: ";
	for (int q=0;q<n+1;q++) cout<<snp[q].power<<"\t";
	cout<<"\nStatIT: ";
	for (int q=0;q<n+1;q++) cout<<snp[q].state<<"\t";
*/	
	for (int i=0;i<k;i++){ //iterating SNAPS
		
		for (int q=0;q<n;q++){
			if ((snp[q].power==1)) snp[q].togglestate();
		}
		
		for (int q=0;q<n;q++){
			if ((snp[q].power==1)&&(snp[q].state==1)) snp[q+1].givepower();
			else snp[q+1].takepower();	
			
			
		}
/*		
		//display state:
 		cout<<"\nStateP: ";
		for (int q=0;q<n+1;q++) cout<<snp[q].power<<"\t";
		cout<<"\nStateT: ";
		for (int q=0;q<n+1;q++) cout<<snp[q].state<<"\t";

*/
	}
	
	
	//	stringstream out;
	//	out << j+1;
		if (snp[n].power==1) {
			cout<<"Case #"<<j+1<<": ON\n";
		}
		if (snp[n].power==0) {cout<<"Case #"<<j+1<<": OFF\n";	
		}
}
	f1.close();
	f2.close();
    return 0;
}
