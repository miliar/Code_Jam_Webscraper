#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n, m;
	char temp;
	cin >> n;
	for(int i=1; i<=n; i++){
		vector<vector<int> > score;
		vector<double> wp, owp, oowp;
		cin >> m;
		for(int j=0; j<m; j++){
      vector<int> row;
      
      for(int k=0; k<m; k++){
			cin >> temp;
			
			switch(temp){
				case '0': row.push_back(0);break;
				case '1': row.push_back(1);break;
				case '.': row.push_back(-1);break;
			}
			
			}
			
			score.push_back(row);
		}
		// wp
		for(int j=0; j<m; j++){
			int win=0, total=0;
			for(int k=0; k<m; k++){
				if(score[j][k]>-1){
					total++;
				}
				if(score[j][k]>0){
					win++;
				}
			}
			if(total==0)
						wp.push_back(double(win)/total);
		 else
				wp.push_back(double(win)/total);
		}
		// owp
		for(int j=0; j<m; j++){
			double a=0; int b=0;
			for(int o=0; o<m; o++){
				if(j!=o && score[j][o]>-1){
					int win=0, total=0;
					for(int k=0; k<m; k++){
						if(j!=k && score[o][k]>-1){
							total++;
						}
						if(j!=k && score[o][k]>0){
							win++;
						}						
					}
					a += double(win)/total;
					b++;
				}
			}
			if(b==0)
			  owp.push_back(0);
			else
				owp.push_back(a/b);
		}
		
		// oowp
		for(int j=0; j<m; j++){
			double a=0; int b=0;
			for(int k=0; k<m; k++){
				if(j!=k && score[j][k]>-1){
					a += owp[k];
					b++;
				}
			}
			if(b==0)
						oowp.push_back(0);
			else
				oowp.push_back(a/b);
		}
		
		cout << "Case #" << i << ":" << endl;
		// final score
		for(int j=0; j<m; j++){
			cout << 0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j] << endl;
		}
	}
	//system("pause");
}
