#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	int T; cin >> T;
	for(int t=0;t<T;t++){
		int N; cin >> N;
		vector <vector <double> > score;

		for(int n=0;n<N;n++){
			string str; cin >> str;
			vector <double> temp;
			for(int i=0;i<str.size();i++){
				if(str[i]=='1')	temp.push_back(1.0);
				if(str[i]=='0')	temp.push_back(0.0);
				if(str[i]=='.')	temp.push_back(-1.0);
			}
			score.push_back(temp);
		}

		vector <vector <double>> WP;
		vector <double>	OWP, OOWP;
		for(int i=0;i<N;i++){
			double sum = 0.0;
			int no = 0;
			for(int j=0;j<N;j++){
				if(score[i][j]<0.0)	no++;
				else				sum+=score[i][j];
			}
			
			vector <double>	wp;
			for(int j=0;j<N;j++){
				if(i==j)	wp.push_back(sum/(double)(N-no));
				else if(score[i][j]<0.0)	wp.push_back(-1.0);
				else{
					if(N-no==1)	wp.push_back(0.0);	
					else		wp.push_back((sum-score[i][j])/(double)(N-no-1));
				}
			}
			WP.push_back(wp);
		}
		//for(int i=0;i<N;i++)	for(int j=0;j<N;j++)	if(j==N-1)	cout << WP[i][j] << endl;	else	cout << WP[i][j] << " ";
		for(int i=0;i<N;i++){
			double owp = 0.0;
			int no = 0;
			for(int j=0;j<N;j++){
				if(score[i][j]<0.0 || i==j)	no++;
				else				owp+=WP[j][i];
			}
			owp /= N-no;
			OWP.push_back(owp);
		}
		for(int i=0;i<N;i++){
			double oowp = 0.0;
			int no = 0;
			for(int j=0;j<N;j++){
				if(score[i][j]<0.0 || i==j)	no++;
				else				oowp+=OWP[j];
			}
			oowp /= N-no;
			OOWP.push_back(oowp);
		}

		//cout << "WP\tOWP\tOOWP" << endl;
		//for(int i=0;i<N;i++){
		//	cout << WP[i][i] << "\t" << OWP[i] << "\t" << OOWP[i] << endl;
		//}
		printf("Case #%d:\n", t+1);
		for(int i=0;i<N;i++)	printf("%.12lf\n", 0.25*WP[i][i]+0.50*OWP[i]+0.25*OOWP[i]);
	}
	return 0;
}