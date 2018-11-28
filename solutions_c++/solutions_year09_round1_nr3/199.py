#include <iostream>
#include <fstream>

using namespace std;

double probs[41][41], fracs[41], choose[41][41];

double ev(int owned);
double evs[40];
bool visited[40];
int total, packSize;

int main() {
	ofstream fout ("google1ac.out");
	ifstream fin ("google1ac.in");
	fracs[0]=1;
	for(int n=1; n<42; n++)
		fracs[n]=fracs[n-1]*(double)n;
	for(int i=0; i<42; i++)
		for(int j=0; j<=i; j++)
			choose[i][j]=fracs[i]/(fracs[j]*fracs[i-j]);
	int numCases;
	fin>>numCases;
	fout.precision(10);
	for(int caseNum=0; caseNum<numCases; caseNum++){
		fin>>total>>packSize;
		for(int i=0; i<=total; i++)	//have
			for(int j=0; j<=total; j++){	//want
				if(j<packSize-i || j>total-i || j>packSize)
					probs[i][j]=0;
				else
					probs[i][j]=choose[total-i][j]*choose[i][packSize-j]/choose[total][packSize];
			}
		for(int i=0; i<total; i++)
			visited[i]=false;
		fout<<"Case #"<<caseNum+1<<": "<<ev(0)<<endl;
	}
	return 0;
}

double ev(int owned){
	if(owned>=total)
		return 0;
	if(visited[owned])
		return evs[owned];
	visited[owned]=true;
	evs[owned]=0;
	for(int n=1; n<=total; n++)
		evs[owned]+=probs[owned][n]*(ev(owned+n)+1.0);
	evs[owned]+=probs[owned][0];
	evs[owned]/=(1.0-probs[owned][0]);
	return evs[owned];
}
