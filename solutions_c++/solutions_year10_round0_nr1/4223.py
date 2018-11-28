//created by chairdog
//08052010

#include <iostream>
#include <fstream>
using namespace std;

int main(){
	char iFile[30], oFile[30];
	cout << "dataset: ";
	cin.getline(iFile,30);
	ifstream inf(iFile);
	cout << "outfile: ";
	cin.getline(oFile,30);
	ofstream outf(oFile);

	int T;
	inf >> T;
	for (int counter=1; counter <= T; counter++){
		long N, K;
		bool *snapper;
		inf >> N >> K;
		snapper = new bool [N];
		for(int i = 0; i < N; i++){
			snapper[i]=false;
		}
		for (int i=0; i<K; i++){
			int index=0;
			while(snapper[index]==true){
				snapper[index]=false;
				index++;
			}
			snapper[index]=true;
		}

		outf << "Case #" << counter << ": ";
		int i= 0;
		while(i<N && snapper[i]) i++;
		if (i==N){
			outf << "ON" << endl;
		}
		else{
			outf << "OFF" << endl;
		}
		delete [] snapper;
	}
	inf.close();
	outf.close();
}
