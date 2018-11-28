#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(){
	srand(13);
	int numCases;
	ifstream fin("g122b.in");
	ofstream fout("g122b.out");
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int numStudents, length, width;
		fin>>numStudents>>width>>length;
		long long radius[1000];
		for(int n=0; n<numStudents; n++)
			fin>>radius[n];
		int maxR=-1, maxRN;
		for(int n=0; n<numStudents; n++)
			if(radius[n]>maxR){
				maxR=radius[n];
				maxRN=n;
			}
		long long centers[1000][2];
		centers[0][0]=0;
		centers[0][1]=0;
		centers[maxRN][0]=width;
		centers[maxRN][1]=length;
		for(int n=1; n<numStudents; n++){
			if(n==maxRN)
				continue;
			bool good=false;
			while(!good){
				good=true;
				centers[n][0]=(rand()*RAND_MAX+rand())%(width+1);
				centers[n][1]=(rand()*RAND_MAX+rand())%(length+1);
				for(int i=0; i<n; i++)
					if((centers[n][0]-centers[i][0])*(centers[n][0]-centers[i][0])
							+ (centers[n][1]-centers[i][1])*(centers[n][1]-centers[i][1])
							< (radius[n]+radius[i])*(radius[n]+radius[i])){
						good=false;
						break;
					}
				int i=maxRN;
				if((centers[n][0]-centers[i][0])*(centers[n][0]-centers[i][0])
						+ (centers[n][1]-centers[i][1])*(centers[n][1]-centers[i][1])
						< (radius[n]+radius[i])*(radius[n]+radius[i]))
					good=false;
			}
			cout<<n<<" "<<centers[n][0]<<" "<<centers[n][1]<<endl;
		}
		fout<<"Case #"<<caseNum+1<<":";
		for(int n=0; n<numStudents; n++)
			fout<<" "<<centers[n][0]<<" "<<centers[n][1];
		fout<<endl;
	}
	return 0;
}
