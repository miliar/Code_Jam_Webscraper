#include <fstream>
#include <string>

using namespace std;

ifstream fin("a-large.in");
ofstream fout("a-large.out");

string words[6000];
string token[20];

int l,d,n;

int match(int ind) {
	for (int i = 0; i < l; i++)
	  if (token[i].find(words[ind][i])==string::npos) 
	    return 0;
  return 1;
	    
}

int main() {
	
  fin>>l>>d>>n;
	for (int i = 0; i < d; i++) {
		fin>>words[i];
	}
	for (int i = 0; i < n; i++) {
	  for (int j = 0; j < l; j++) {
	  	token[j]="";
	  	char tmp;
	    fin>>tmp;
	    if (tmp=='(') 
	    	while (1) {
	    		fin>>tmp;
	    		if (tmp==')') break;
	    		token[j] +=tmp;
	    	}
	    else token[j]=tmp;
	  }
	  int ans = 0;
	  for (int j = 0; j < d; j++)
	    if (match(j)) 
	      ans++;
    fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}
