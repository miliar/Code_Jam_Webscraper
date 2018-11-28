#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int t,c,d,n;
	char ca[37][4], da[29][3], na[101];
	char e[101];
	int ei=0;
	char tc;
	int cf=0;

	ifstream fin("in.txt");
	ofstream fout("out.txt");

	fin>>t;
	for(int i=0; i<t; i++){
		fin>>c;
		for(int j=0; j<c; j++){
			fin>>ca[j];
		}

		fin>>d;
		for(int j=0; j<d; j++){
			fin>>da[j];
		}

		fin>>n;
		fin>>na;

		ei = 0;

		for(int j=0; na[j]!='\0'; j++){
			cf=0;
			for(int k=0; k<c; k++){
				if((ca[k][0] == na[j] && ca[k][1] == e[ei-1]) || (ca[k][0] == e[ei-1] && ca[k][1] == na[j])){
					e[ei-1] = ca[k][2];
					cf=1;
					break;
				}
			}
			if(cf == 0){
				e[ei++] = na[j];

				for(int k=0; k<d; k++){
					if(na[j] == da[k][0]){
						tc = da[k][1];
					}else if (na[j] == da[k][1]){
						tc = da[k][0];
					}else{
						continue;
					}

					for(int h=0; h<ei-1; h++){
						if(e[h] == tc){
							// Clear The list
							ei = 0;
							break;
						}
					}
				}
			}

		}

		fout<<"Case #"<<i+1<<": [";
		for(int i=0; i<ei; i++){
			fout<<e[i];
			if(i != ei-1){
				fout<<", ";
			}
		}
		fout<<"]"<<endl;

	}

	return 0;
}