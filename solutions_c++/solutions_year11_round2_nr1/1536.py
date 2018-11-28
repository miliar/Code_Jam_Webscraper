#include <fstream.h>
ifstream in("/Users/SunKim/Desktop/Codejam 2011/Round1-1/in.txt");
ofstream out("/Users/SunKim/Desktop/Codejam 2011/Round1-1/out.txt");
int t;
int data[101][101];
double owp[101],oowp[101],wp[101];
char input[101];
double total,win,sum;
int main(){
	in >> t;
	for(int z=0;z<t;z++){
		int n;
		in >> n;
		int i,j,k;
		for(i=0;i<n;i++){
			in >> input;
			total=0;
			win=0;
			for(j=0;j<n;j++){
				if(input[j]=='.'){
					data[i][j]=-1;
				}else if(input[j]=='1'){
					data[i][j]=1;
					total++;
					win++;
				}else if(input[j]=='0'){
					data[i][j]=0;
					total++;
				}
			}
			wp[i]=win/total;
		}
		for(i=0;i<n;i++){
			sum=0;
			int cnt=0;
			for(j=0;j<n;j++){
				total=0;
				win=0;
				if(data[i][j]!=-1){
					cnt++;
					for(k=0;k<n;k++){
						if(k==i || data[j][k]==-1) continue;
						if(data[j][k]==1){
							win++;
						}
						total++;
					}
					sum+=(win/total);
				}
				
			}
			owp[i]=sum/cnt;
		}
		for(i=0;i<n;i++){
			int cnt=0;
			sum=0;
			for(j=0;j<n;j++){
				if(data[i][j]!=-1){
					sum+=owp[j];
					cnt++;
				}
			}
			oowp[i]=sum/cnt;
		}
		out << "Case #" << z+1 << ":\n";
		for(i=0;i<n;i++){
			out << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << "\n";
		}
	}
	
	return 0;
}