#include <iostream>
#include <fstream>
#include <bitset>

using namespace std;

bool isHappy(int n, int b);

bitset<1000> visited[9], happy[9];

int main() {
	ofstream fout ("google1aa.out");
	ifstream fin ("google1aa.in");
	for(int n=0; n<9; n++){
		happy[n][1]=true;
		visited[n][1]=true;
		//for(int i=1; i<n+2; i++)
			//visited[n][i]=true;
		for(int i=1; i<1000; i++)
			isHappy(i, n+2);
	}
	int numCases;
	fin>>numCases;
	char buffer[50];
	fin.getline(buffer, 50);
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int bases[9], numBases=0;
		fin.getline(buffer, 50);
		for(int n=0; n<fin.gcount(); n++)
			if(buffer[n]>='1' && buffer[n]<='9'){
				if(buffer[n]=='1'){
					n++;
					bases[numBases]=10;
				}
				else
					bases[numBases]=buffer[n]-'0';
				numBases++;
			}
		for(int n=2; n<1000000; n++){
			bool works=true;
			for(int i=0; i<numBases; i++)
				if(!isHappy(n,bases[i]))
					works=false;
			if(works){
				fout<<"Case #"<<caseNum+1<<": "<<n<<endl;
				break;
			}
		}
	}
	return 0;
}

bool isHappy(int n, int b){
	//cout<<n<<" "<<b<<": ";
	if(n<1000){
		if(visited[b-2][n]){
			//cout<<happy[b-2][n]<<endl;
			return happy[b-2][n];
		}
		visited[b-2][n]=true;
	}
	int sum=0;
	for(int i=n; i>0; i/=b)
		sum+=(i%b)*(i%b);
	bool good=isHappy(sum, b);
	if(n<1000 && good)
		happy[b-2][n]=true;
	return good;
}
