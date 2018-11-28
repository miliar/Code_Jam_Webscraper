#include <algorithm>

using namespace std;
FILE *in, *out;

pair<int, int> start[202], end[202];
bool check[202];

int main(){
    int n, T, na, nb;
    in = fopen("B.in", "r");
    out = fopen("B.out", "w");
    fscanf(in, "%d", &n);
    for(int x=1;x<=n;x++){
	fscanf(in, "%d", &T);
	fscanf(in, "%d %d", &na, &nb);

	int a, b, c, d;
	for(int i=1;i<=na;i++){
	    fscanf(in, "%d:%d %d:%d", &a, &b, &c, &d);
	    start[i] = make_pair(a*60+b, i);
	    end[i] = make_pair(c*60+d, i);
	}
	for(int i=1;i<=nb;i++){
	    fscanf(in, "%d:%d %d:%d", &a, &b, &c, &d);
	    start[na+i] = make_pair(a*60+b, 100+i);
	    end[na+i] = make_pair(c*60+d, 100+i);
	}
	fill(check+1, check+201, false);

	sort(start+1, start+na+nb+1);
	sort(end+1, end+na+nb+1);

	int result[2] = {0, 0};
	for(int i=1;i<=na+nb;i++){
	    if(check[end[i].second]) continue;

	    int now = i;
	    result[end[now].second/101]++;
	    while(true){
		check[end[now].second] = true;

		int next=0;
		for(int j=1;j<=na+nb && !next;j++)
		    if(!check[start[j].second] && end[now].first + T <= start[j].first && 
			    (end[now].second/101) != (start[j].second/101))
			next = j;
		if(!next) break;

		for(int j=1;j<=na+nb;j++)
		    if(end[j].second == start[next].second){
			now = j;
			break;
		    }
	    }
	}

	fprintf(out, "Case #%d: %d %d\n", x, result[0], result[1]);
    }
    fclose(in);
    fclose(out);
    return 0;
}