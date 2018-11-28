#include<fstream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;

	int tNum;
	int n,s,p;
	int score[100];
	int i,j,k;
	int cnt;

	fin.open("B-large.in");
	fout.open("output.txt");
	fin>>tNum;
	
	for(i=0; i<tNum; i++){
		fin>>n>>s>>p;
		for(j=0; j<n; j++)
			fin>>score[j];
		for(j=0; j<n-1; j++){
			for(k=1; k<n-j; k++){
				if(score[k-1]>score[k]){
					int tmp=score[k];
					score[k]=score[k-1];
					score[k-1]=tmp;
				}
			}
			
		}
		cnt=0;
		for(j=n-1; j>=0; j--){
			int p_1,p_2;
			if(p>=2){ p_1=p-1;
			p_2=p-2;
			}
			else if(p>=1) {p_1=p-1;
			p_2=0;}
			else{
				p_1=0;
				p_2=0;
			}



			if(score[j]>=p+2*(p_1))
				cnt++;
			else{
				if(s>0){
					s--;
					if(score[j]>=p+2*(p_2))
						cnt++;
					else break;
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<cnt<<endl;


	}



	fin.close();
	fout.close();

	return 0;
}