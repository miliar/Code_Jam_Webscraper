#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
using namespace std;

struct Trie {
	int koncowy;
	Trie *dzieci[26];
	Trie():
		koncowy(-1) {
		for(int i=0;i<26;++i)
			dzieci[i]=NULL;
	}
	void wstaw(const char *slowo,int id) {
		if(slowo[0]==0) {
			koncowy=id;
			return;
		}
		int x=slowo[0]-'a';
		if(dzieci[x]==NULL)
			dzieci[x]=new Trie();
		dzieci[x]->wstaw(slowo+1,id);
	}
	int ilePasuje(const vector<string> &wzorzec,int pozycja) {
		if(koncowy!=-1) {
			//printf("koncowy=%d\n",koncowy);
			return 1;
		}
		int wynik=0;
		for(int i=0,n=wzorzec[pozycja].size();i<n;++i) {
			int x=wzorzec[pozycja][i]-'a';
			if(dzieci[x]!=NULL) {
				wynik+=dzieci[x]->ilePasuje(wzorzec,pozycja+1);
			}
		}
		return wynik;
	}
};

int main() {
	char stemp[555];
	int liter,slow,testow;
	scanf("%d%d%d",&liter,&slow,&testow);
	Trie korzen;
	for(int i=0;i<slow;++i) {
		scanf("%s",stemp);
		korzen.wstaw(stemp,i);
	}
	for(int z=1;z<=testow;++z) {
		scanf("%s",stemp);
		vector<string> wzorzec;
		bool srodek=false;
		string ss;
		for(int i=0;stemp[i];++i) {
			if(srodek) {
				if(stemp[i]==')') {
					srodek=false;
				} else {
					ss+=stemp[i];
				}
			} else {
				if(stemp[i]=='(') {
					srodek=true;
					wzorzec.push_back(ss);
					ss="";
				} else {
					wzorzec.push_back(ss);
					ss="";
					ss+=stemp[i];
				}
			}
		}
		wzorzec.push_back(ss);
		/*for(int i=0,n=wzorzec.size();i<n;++i) {
			printf("i=%d (%s)\n",i,wzorzec[i].c_str());
		}*/
		printf("Case #%d: ",z);
		int wynik=korzen.ilePasuje(wzorzec,1);
		printf("%d\n",wynik);
	}
}
