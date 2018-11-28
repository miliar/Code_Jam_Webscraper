#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <cmath>

using namespace std;

int main(){
	ifstream in;
	ofstream out;
	
	in.open("A-large.in");
	out.open("output.txt");

	

	int T;
	in>>T;

	for(int u=0;u<T;u++){

		cout<<u<<endl;
		out<<"Case #"<<(u+1)<<": "<<endl;
		
		int t;
		in>>t;

		int amount[100][100];


		for(int i=0;i<t;i++){
			string val;
			in>>val;
			for(int j=0;j<t;j++){
				if(val[j]=='0'){
					amount[i][j]=0;
				}
				else if(val[j]=='1'){
					amount[i][j]=1;
				}
				else{
					amount[i][j]=-1;
				}
			}
		}


		for(int i=0;i<t;i++){
			double WP=0.0;
			double OWP=0.0;
			double OOWP=0.0;
			vector<int> index;
			
			double all=0.0;
			double wins=0.0;
			for(int j=0;j<t;j++){
				if(amount[i][j]!=-1){
					all+=1.0;
					index.push_back(j);
					if(amount[i][j]==1){
						wins+=1.0;
					}
				}
			}//end of WP

			WP = wins/all;

			for(int j=0;j<index.size();j++){
				double opall=0.0;
				double opwins=0.0;
				vector<int> op;
				//check his opponents

				for(int k=0;k<t;k++){
					if(amount[index[j]][k]!=-1){
						op.push_back(k);
						if(k==i){
							continue;
						}
						opall+=1.0;
						if(amount[index[j]][k]==1){
							opwins+=1.0;
						}
					}
				}

				OWP += opwins/opall;
				double local=0;

				for(int l=0;l<op.size();l++){
					double opallt=0.0;
					double opwinst=0.0;
					//cout<<j<<"j"<<endl;
					for(int k=0;k<t;k++){
						if(amount[op[l]][k]!=-1){
							if(k==index[j]){
								continue;
							}
							opallt+=1.0;
							if(amount[op[l]][k]==1){
								opwinst+=1.0;
							}
						}
					}
					//cout<<opwinst<<" "<<opallt<<endl;
					local += opwinst/opallt;
				}
				//cout<<local<<"local"<<endl;
				local /= op.size();
				OOWP += local;
				//cout<<OOWP<<" now"<<endl;
			}

			OWP /= index.size();
			OOWP /= index.size();

			//cout<<OWP<<"u"<<u<<endl;
			//cout<<OOWP<<"u"<<u<<endl;

			out<< 0.25 * WP + 0.50 * OWP + 0.25 * OOWP <<endl;



		}


		

	}

	in.close();
	out.close();

	return 0;
}