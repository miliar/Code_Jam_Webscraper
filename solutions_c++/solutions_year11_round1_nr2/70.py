#include <iostream>
#include <fstream>
#include <map>
using namespace std;

#define FILENAME "B-large"

struct tmask {
	int count;
	string mask;
	bool done;
	bool abc['z'-'a'+1];
	void reset() {
		for (char i='a';i<='z';i++)
			abc[i-'a']=false;
	}
	tmask() {
		reset();
		count=0; done=false;
	}
};

bool update_mask(string w, string o, string &n, char l) {
	n=o; bool ret=false;
	for (int i=0;i<o.size();i++) {
		if (w[i]==l) {
			ret=true;
			n[i]=l;
		}
	}
	return ret;
}

void setabc(string w, tmask *m) {
	for (int i=0;i<w.size();i++)
		m->abc[w[i]-'a']=true;
}

int main(int argc, char *argv[]) {
	
	ifstream fin(FILENAME".in");
	ofstream fout(FILENAME".out");
	
	int C;
	fin>>C;
	int *pts=new int[10000];
	string *word=new string[10000];
	tmask **mask=new tmask*[10000];
	
	
	for (int c=0;c<C;c++) {
		cerr<<c<<endl;
		int N,M;
		fin>>N>>M;
		for (int i=0;i<N;i++)
			fin>>word[i];
		fout<<"Case #"<<c+1<<":";
		for (int i=0;i<M;i++) {
			map<string,tmask> m;
			map<string,tmask>::iterator it;
			char abc[27];
			int mc=0;
			for (int k=0;k<N;k++) {
				string str(word[k].size(),'_');
				( mask[k] = &(m[str]) ) -> count++;
				mask[k]->mask=str;
				setabc(word[k],mask[k]);
				pts[k]=0;
			}
//			for (int k=0;k<n;k++) {
//				cerr<<"   "<<word[k]<<"  "<<mask[k]->mask<<"  "<<pts[k]<<endl;
//			}
			fin>>abc;
			string nmask;
			for (int j=0;j<26;j++) {
				char l=abc[j];
				for (int k=0;k<N;k++) {
					if (mask[k]->done) continue;
					if (!mask[k]->abc[l-'a']) continue;
					if (update_mask(word[k],mask[k]->mask,nmask,l)) {
						m[mask[k]->mask].count--;
						( mask[k]=&(m[nmask]) )-> count++;
						mask[k]->mask=nmask;
					} else {
						pts[k]++;
					}
				}
				for (int k=0;k<N;k++) mask[k]->reset();
				for (int k=0;k<N;k++) 
					if (!mask[k]->done) setabc(word[k],mask[k]);
				for (int k=0;k<N;k++) {
					if (mask[k]->done) continue;
					if (mask[k]->count==1 /*&& mask[k]->mask==word[k]*/) mask[k]->done=true;
//					else if (mask[k]->mask==word[k]) mask[k]->done=true;
				}
//				cerr<<l<<endl;
//				for (int k=0;k<n;k++) {
//					cerr<<"   "<<word[k]<<"  "<<mask[k]->mask<<"  "<<pts[k]<<endl;
//				}
			}
			int max=pts[0], imax=0;
			for (int k=1;k<N;k++) {
				if (pts[k]>max) {
					imax=k; max=pts[k];
				}
			}
			fout<<" "<<word[imax];
		}
		fout<<endl;
	}
	
	fin.close();
	fout.close();
	return 0;
	
}

