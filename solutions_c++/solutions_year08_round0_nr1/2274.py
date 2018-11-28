#include <cstdio>
#include <cassert>
#include <map>
#include <string>

std::map<std::string, int> SearchEngineName;
int appearance[100][1000];
int appeared[100];

int main(){
    char buf[128];
    int nc;
    scanf(" %d", &nc);
    for(int cc = 1; cc <= nc; ++cc){
	int nSearchEngine;
	scanf(" %d", &nSearchEngine);
	getchar();

	SearchEngineName.clear();
	for(int i = 0; i < nSearchEngine; ++i){
	    fgets(buf, sizeof(buf), stdin);
	    buf[strlen(buf) - 1] = 0;
	    if(!SearchEngineName.insert(
		    std::make_pair(
			std::string(buf),
			SearchEngineName.size())).second)
		fprintf(stderr, "Shit happened: SearchEngine '%s' multiply declared\n", buf);
	}

	int nQuery;
	scanf(" %d\n", &nQuery);
	for(int i = 0; i < 100; ++i)
	    appeared[i] = 0;
	for(int i = 0; i < nQuery; ++i){
	    fgets(buf, sizeof(buf), stdin);
	    buf[strlen(buf) - 1] = 0;
	    std::map<std::string, int>::iterator p
		= SearchEngineName.find(std::string(buf));

	    if(p == SearchEngineName.end())
		fprintf(stderr, "Shit happened: SearchEngine '%s' not found\n", buf);
	    else
		appearance[p->second][appeared[p->second]++] = i;
	}
	for(int i = 0; i < nSearchEngine; ++i)
	    appearance[i][appeared[i]++] = nQuery;

	// find the first one to use
	int currEngine = -1, currPoint = -1;
	for(int i = 0; i < nSearchEngine; ++i)
	    if(appearance[i][0] > currPoint){
		currPoint = appearance[i][0];
		currEngine = i;
	    }

	// sweep
	int sweep[100];
	int nSwitch = 0;
	for(int i = 0; i < 100; ++i)
	    sweep[i] = 0;
	while(currPoint < nQuery){
	    assert(currPoint == appearance[currEngine][sweep[currEngine]]);

	    int nextEngine = -1, nextPoint = currPoint;
	    for(int i = 0; i < nSearchEngine; ++i){
		while(appearance[i][sweep[i]] < currPoint) ++sweep[i];
		if(appearance[i][sweep[i]] > nextPoint){
		    nextPoint = appearance[i][sweep[i]];
		    nextEngine = i;
		}
	    }

	    assert(nextEngine != currEngine && nextPoint > currPoint);
	    currEngine = nextEngine;
	    currPoint = nextPoint;
	    ++nSwitch;
	}

	printf("Case #%d: %d\n", cc, nSwitch);
    }
    return 0;
}
