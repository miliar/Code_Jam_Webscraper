#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<sstream>

using namespace std;

char buffer[2048];

//istream ss(buffer,2048);

ifstream iFile("A_input.in");
ofstream oFile("A_output.txt");

int main(){
	int T=1;
	iFile>>T;
	//cout<<T<<endl;
		
	iFile.getline(buffer,2048);

	for(int i=0;i<T;i++){
		iFile.getline(buffer,2048);
		//cout<<buffer<<"\t"<<strlen(buffer)<<endl;

		int arr[2][100]={0};//for small data set replace 100 with 10

		stringstream ss(buffer);
		int nB;
		ss>>nB;
		
		int seqArr[2][100]={0};//for small data set replace 100 with 10
		int seq=0;
		int curO=0,curB=0;

		//cout<<nB<<"\t";

		while(ss.good()){
			char c;
			ss>>c;
			int k;
			ss>>k;

			if(c == 'O'){
				seqArr[0][seq++]=1;
				arr[0][curO++]=k;
			}
			if(c == 'B'){
				seqArr[1][seq++]=1;
				arr[1][curB++]=k;
			}

		//	cout<<"("<<c<<","<<k<<") ";
		}
		
		curO=0;
		curB=0;

		int time=0;
		int oButton=1,bButton=1;
		
		int a=0;

		while(a<nB){

			if(seqArr[0][a]){
				if(arr[0][curO]==oButton){
					a++;
					curO++;
				}else if(arr[0][curO]>oButton){
					oButton++;
				}else{
					oButton--;
				}

				if(arr[1][curB]>bButton){
					bButton++;
				}else if(arr[1][curB]<bButton){
					bButton--;
				}

				time++;	
			}else{
				if(arr[1][curB]==bButton){
					a++;
					curB++;
				}else if(arr[1][curB]>bButton){
					bButton++;
				}else{
					bButton--;
				}
				
				
				if(arr[0][curO]>oButton){
					oButton++;
				}else if(arr[0][curO]<oButton){
					oButton--;
				}

				time++;
			}
		}
		//cout<<"Case #"<<(i+1)<<": "<<time<<endl;
		oFile<<"Case #"<<(i+1)<<": "<<time<<endl;
	}
	
}
