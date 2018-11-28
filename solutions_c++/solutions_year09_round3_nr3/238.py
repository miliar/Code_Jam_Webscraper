#include <fstream>
#include <string.h>

using namespace std;

ifstream fin("c-small.in");
ofstream fout("c-small.out");

int p,q;
int used[120];
int pos[120];
int index[120];
int ans;


void check() {
	int tmpans=0;
	memset(used,0,sizeof used);
    used[0]=used[q+1]=1;
	for (int i = 1; i <= q; i++) {
		int ind=index[i];
		int l=ind-1,r=ind+1;
		while (!used[l]) {
			l--;
		}
		while (!used[r]) {
			r++;
		}
		tmpans+=pos[r]-pos[l]-2;
		used[ind]=1;
	}
	if (tmpans<ans) 
	  ans=tmpans;
 
}

int b[120];
void sub(int s) {
	if (s>q) check();
	else 
	  for (int i = 1; i <= q; i++)
	    if (!b[i]) {
	    	b[i]=1;
	    	index[s]=i;
	    	sub(s+1);
	    	b[i]=0;
	    }
}

int main() {
	int ncase;
	fin>>ncase;
	for (int curcase=1;curcase<=ncase;curcase++) {

		fin>>p>>q;
		pos[0]=0;
		pos[q+1]=p+1;
		for (int i = 1; i <= q; i++) 
		  fin>>pos[i];
		  
		  
    ans=999999999;
    memset(b,0,sizeof b);
    
    sub(1);
    fout<<"Case #"<<curcase<<": "<<ans<<endl;
	}
	
}
    
	
