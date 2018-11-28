#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>

int m, n;

char fixed[2000];
char toggled[2000];
char care[2000][2000];
char want[2000][2000];
int nCare[2000];
std::set<int> caring[2000];

int Sweep(){
    std::vector<int> critical;
    for(int i = 0; i < m; ++i)
	if(nCare[i] == 0) return -1;
	else if(nCare[i] == 1)
	    critical.push_back(i);
    if(critical.empty()) return 0;

    fprintf(stderr, "criticals:");
    for(std::vector<int>::iterator i = critical.begin(),
	    end = critical.end(); i < end; ++i){
	fprintf(stderr, " %d", *i);
    }
    fputc('\n', stderr);
    for(std::vector<int>::iterator i = critical.begin(),
	    end = critical.end(); i < end; ++i){
	fprintf(stderr, "process: %d\n", *i);
	int milk = *caring[*i].begin();
	if(want[*i][milk] == 1){
	    if(fixed[milk]){
		if(!toggled[milk])
		    return -1;
		else
		    continue;
	    }
	    toggled[milk] = 1;
	    fixed[milk] = 1;
	    fprintf(stderr, "sweeping %d\n", milk);
	    for(int k = 0; k < m; ++k){
		if(care[k][milk]){
		    fprintf(stderr, "hitted %d\n", k);
		    if(want[k][milk])
			nCare[k] = 3000;
		    else if(nCare[k] > 1){
			--nCare[k];
			care[k][milk] = 0;
			caring[k].erase(milk);
		    }
		}
	    }
	}else{
	    if(fixed[milk]){
		if(toggled[milk])
		    return -1;
		else
		    continue;
	    }
	    fixed[milk] = 1;
	    fprintf(stderr, "sweeping %d\n", milk);
	    for(int k = 0; k < m; ++k){
		if(care[k][milk]){
		    fprintf(stderr, "hitted %d\n", k);
		    if(!want[k][milk])
			nCare[k] = 3000;
		    else if(nCare[k] > 1){
			--nCare[k];
			care[k][milk] = 0;
			caring[k].erase(milk);
		    }
		}
	    }
	}
	nCare[*i] = 3000;
    }
    return 1;
}

int main(){
    int nc;
    scanf(" %d", &nc);
    for(int cc = 1; cc <= nc; ++cc){
	int p, q;

	scanf(" %d%d", &n, &m);
	for(int i = 0; i < m; ++i){
	    std::fill(care[i], care[i] + n, 0);
	    caring[i].clear();
	    scanf(" %d", &nCare[i]);
	    for(int j = 0; j < nCare[i]; ++j){
		scanf(" %d%d", &p, &q);
		--p;
		care[i][p] = 1;
		want[i][p] = q;
		caring[i].insert(p);
	    }
	}
	std::fill(fixed, fixed + n, 0);
	std::fill(toggled, toggled + n, 0);

	int result;
	while((result = Sweep()) > 0);
	if(result < 0){
	    printf("Case #%d: IMPOSSIBLE\n", cc);
	}else{
	    printf("Case #%d:", cc);
	    for(int i = 0; i < n; ++i)
		printf(" %d", toggled[i]);
	    putchar('\n');
	}
    }
}
