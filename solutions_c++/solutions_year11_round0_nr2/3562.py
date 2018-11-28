#include<set>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int main(void){
    int tcnum;
    scanf("%d ", &tcnum);
    for (int z=1; z<=tcnum; z++){
	set<pair<char, char> > opsd;
	map<pair<char, char>, char> comb;
	int cbnum;
	scanf("%d ", &cbnum);
	for (int k=1; k<=cbnum; k++){
	    char a, b, c;
	    scanf(" %c %c %c ", &a, &b, &c);
	    comb[make_pair(a,b)]=c;
	    comb[make_pair(b,a)]=c;
	}
	int opnum;
	scanf("%d ", &opnum);
	for (int k=1; k<=opnum; k++){
	    char a, b;
	    scanf(" %c %c ", &a, &b);
	    opsd.insert(make_pair(a, b));
	    opsd.insert(make_pair(b, a));
	}
	int inum;
	vector<char> elelist;
	scanf("%d ", &inum);
	for (int k=1; k<=inum; k++){
	    char cinv;
	    scanf(" %c ", &cinv);
	    elelist.push_back(cinv);
	    bool doit=true;
	    while (doit){
		doit=false;
		int last=elelist.size()-1;
		if (elelist.size()==0)
		    break;
		else if (elelist.size()==1){
		    if (opsd.count(make_pair(elelist[last], elelist[last]))>0){
			elelist.clear();
			break;
		    }
		}
		else{
		    if (comb.count(make_pair(elelist[last], elelist[last-1]))>0){
			elelist[last-1]=comb[make_pair(elelist[last], elelist[last-1])];
			elelist.erase(elelist.begin()+last);
			doit=true;
		    }
		    else{
			for (int j=0; j<(int)elelist.size(); j++)
			    if (opsd.count(make_pair(elelist[last], elelist[j]))>0){
				elelist.clear();
				break;
			    }
			
		    }
		    
		}
	    }
	}
	printf("Case #%d: [", z);
	for (int k=0; k<(int)elelist.size(); k++)
	    printf("%c%s", elelist[k], (k!=(int)elelist.size()-1)?", ":"");
	    
	puts("]");

    }
    return 0;
}

