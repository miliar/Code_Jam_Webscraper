#include <iostream>
#include <fstream>
using namespace std;

int find_next(char *r, int N, int R, int n) {
	while (n<N && r[n]!=R) n++;
	return n;
}

int main(int argc, char *argv[]) {
	
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	const int cl='Z'-'A'+1;
	char comb[cl][cl];
	char opos[cl][cl];
	char res[101];
	
	int C;
	fin>>C;
	for (int cc=0;cc<C;cc++) {
		
		for (int i=0;i<cl;i++) {
			for (int j=0;j<cl;j++) {
				comb[i][j]=opos[i][j]=0;
			}
		}
		
		int n;
		char a,b,c;
		fin>>n;
		for (int i=0;i<n;i++) {
			fin>>a>>b>>c;
			comb[a-'A'][b-'A']=c;
			comb[b-'A'][a-'A']=c;
		}
		
		fin>>n;
		for (int i=0;i<n;i++) {
			fin>>a>>b;
			opos[a-'A'][b-'A']=1;
			opos[b-'A'][a-'A']=1;
		}
		
		int l=0;
		fin>>n;
		for (int i=0;i<n;i++) {
			fin>>a;
			if (l && comb[a-'A'][res[l-1]-'A'])
				res[l-1]=comb[a-'A'][res[l-1]-'A'];
			else {
				bool clear=false;
				for (int j=0;j<l;j++) {
					if (opos[a-'A'][res[j]-'A']) {
						clear=true;
						break;
					}
				}
				if (clear) l=0;
				else res[l++]=a;
			}
		}
		
		if (l) {
			fout<<"Case #"<<cc+1<<": [";
			for (int i=0;i<l-1;i++)
				fout<<res[i]<<", ";
			fout<<res[l-1]<<"]"<<endl;
		} else {
			fout<<"Case #"<<cc+1<<": []"<<endl;
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
	
}

