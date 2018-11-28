#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;


float readTime(ifstream& inFile) {
	int tempA, tempB;
	char tchar;
	inFile>>tempA>>tchar>>tempB;
	cerr<<tempA<<" "<<tchar<<" "<<tempB;
	return (tempA)+(tempB/60.0);
}

class schedule {
	public:
		float t0;
		float t1;
		static bool isSmaller(schedule a, schedule b) {
			return a.t0 < b.t0;
		}
};

void displaySchedule(string iden, vector<schedule>& A) {
	cout<<"Schedule for "<<iden<<":\n";
	for(int i=0; i<A.size(); i++)
		cout<<A[i].t0<<" to "<<A[i].t1<<endl;
}

void readCase(ifstream& inFile, vector<schedule>& A, vector<schedule>& B) {
	int T, nA, nB, temp;
	char tchar;
	inFile>>T>>nA>>nB;
	cerr<<T<<" "<<nA<<" "<<nB<<endl;
	A.resize(nA);
	for(int i=0; i<nA; i++) {
		A[i].t0=readTime(inFile);
		A[i].t1=readTime(inFile)+(T/60.0);
	}
	B.resize(nB);
	for(int i=0; i<nB; i++) {
		B[i].t0=readTime(inFile);
		B[i].t1=readTime(inFile)+(T/60.0);
	}
	displaySchedule("A", A);
	displaySchedule("B", B);
}

class traintable {
	public:
	int prev, next;
	traintable(int a, int b) {
		prev=a; next=b;
	}
};

class distAB {
	public:
	int rA, rB;
	float dist;
	distAB(int a, int b, float ff) {
		rA=a; rB=b; dist=ff;
	}
	static bool isSmaller(distAB a, distAB b) {
		return a.dist < b.dist;
	}
};

int runConnectClosest(ofstream& outFile, vector<schedule>& A, vector<schedule>& B) {
	vector<distAB> alldistsAB;
	for(int i=0; i<A.size(); i++) {
		for(int j=0; j<B.size(); j++) {
			float tempDist=B[j].t0-A[i].t1;
			if(tempDist<0) continue;
			alldistsAB.push_back(distAB(i, j, tempDist));
		}
	}
	vector<distAB> alldistsBA;
	for(int i=0; i<A.size(); i++) {
		for(int j=0; j<B.size(); j++) {
			float tempDist=A[i].t0-B[j].t1;
			if(tempDist<0) continue;
			alldistsBA.push_back(distAB(i, j, tempDist));
		}
	}

	std::sort(alldistsAB.begin(), alldistsAB.end(), distAB::isSmaller);
	std::sort(alldistsBA.begin(), alldistsBA.end(), distAB::isSmaller);
	for(int i=0; i<alldistsAB.size(); i++) {
		cerr<<alldistsAB[i].dist<<"->";
	}

	vector<traintable> alltrains(A.size()+B.size(), traintable(-1, -1));

	int nnext=0;
	for(int i=0; i<alldistsAB.size() && nnext<A.size(); i++) {
		int ai=alldistsAB[i].rA;
		int bi=alldistsAB[i].rB+A.size();
		if(alltrains[ai].next<0 && alltrains[bi].prev<0) {
			alltrains[ai].next=bi;
			alltrains[bi].prev=ai;
			nnext++;
		}
	}

	nnext=0;
	for(int i=0; i<alldistsBA.size() && nnext<B.size(); i++) {
		int ai=alldistsBA[i].rA;
		int bi=alldistsBA[i].rB+A.size();
		if(alltrains[bi].next<0 && alltrains[ai].prev<0) {
			alltrains[bi].next=ai;
			alltrains[ai].prev=bi;
			nnext++;
		}
	}
	int ntrainsA=0, ntrainsB=0;
	for(int i=0; i<A.size(); i++)  {
		if(alltrains[i].prev<0) ntrainsA++;
	}
	for(int i=A.size(); i<A.size()+B.size(); i++)  {
		if(alltrains[i].prev<0) ntrainsB++;
	}
	
	outFile<<ntrainsA<<" "<<ntrainsB<<endl;
	return ntrainsA+ntrainsB;
}

int processCase(ifstream& inFile, ofstream& outFile) {
	vector<schedule> A, B;
	readCase(inFile, A, B);
	return runConnectClosest(outFile, A, B);
}

void processFile(char* infname, char* outfname) {
	// SETUP
	// open all files
	ifstream inFile(infname);
	ofstream outFile(outfname);

	int N=0;
	inFile>>N;
	cerr<<"N="<<N<<endl;
	for(int i=0; i<N; i++) {
		cerr<<"Case #"<<i+1<<" of "<<N<<endl;
		outFile<<"Case #"<<i+1<<": ";
		processCase(inFile, outFile);
		cerr<<endl<<endl;
	}

	// CLEANUP
	// close all files
	inFile.close();
	outFile.close();
}


int main(int argv, char** argc) {
	processFile(argc[1], argc[2]);
	return 0;
}
