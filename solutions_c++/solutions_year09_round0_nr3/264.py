#include <iostream>
#include <fstream>

using namespace std;

int search(int i, int j);

const char goal[20]="welcome to code jam";
char input[501];
bool visited[500][19];
int answer[500][19], length;

int main() {
	ofstream fout ("googleqr3.out");
	ifstream fin ("googleqr3.in");
	int numCases;
	fin>>numCases;
	fin.get();
	for(int caseNum=0; caseNum<numCases; caseNum++){
		fin.getline(input, 501);
		length=fin.gcount()-1;
		for(int i=0; i<length; i++)
			for(int j=0; j<19; j++)
				visited[i][j]=false;
		int result=search(0, 0);
		fout<<"Case #"<<caseNum+1<<": ";
		if(result<1000)
			fout<<0;
		if(result<100)
			fout<<0;
		if(result<10)
			fout<<0;
		fout<<result<<endl;
	}
	return 0;
}

int search(int i, int j){
	if(j==19)
		return 1;
	if(i==length)
		return 0;
	if(visited[i][j])
		return answer[i][j];
	visited[i][j]=true;
	answer[i][j]=0;
	for(int n=i; n<length; n++){
		if(input[n]==goal[j]){
			answer[i][j]+=search(n+1, j+1)%10000;
			answer[i][j]%=10000;
		}
	}
	return answer[i][j];
}
