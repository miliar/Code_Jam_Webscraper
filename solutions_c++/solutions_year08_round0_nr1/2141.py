#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
const int SMAX = 20000;
int main(){

    int num_case;
    scanf("%d", &num_case);

    for (int case_no = 1; case_no <= num_case; case_no ++){
	map<string, int> engine;

	int s;
	char data[1000];
	scanf("%d", &s);
	fgets(data, sizeof(data), stdin);
	
	for(int i = 0; i < s; i ++){
	    fgets(data, sizeof(data), stdin);
	    //	    printf("%s", data);
	    engine[string(data)] = i;
	}
	
	int q;
	scanf("%d", &q);
	vector<int> query(q);
	fgets(data, sizeof(data), stdin);
	
	for (int i = 0; i < q; i ++){
	    fgets(data, sizeof(data), stdin);
	    query[i] = engine[string(data)];
	}

	vector<vector<int> > d(2000, vector<int>(2000, 0));
	
	if (q > 0)
	    d[0][query[0]] = SMAX;

	for (int i = 1; i < q; i ++){

	    for (int j = 0; j < s; j ++){
		int Min = SMAX;
		
		for (int k = 0; k < s; k ++){
		    int tmp = d[i - 1][k];
		    if (k != j)
			tmp ++;
		    if (tmp < Min)
			Min = tmp;
		}
		d[i][j] = Min;
	    }
	    d[i][query[i]] = SMAX;
	}
	
	int Min = SMAX;
	
	if(q > 0){
	    for (int i = 0; i < s; i ++)
		Min = min(Min, d[q - 1][i]);
	}
	else
	    Min = 0;
	
	printf("Case #%d: %d\n", case_no, Min);
    }
    
    return 0;
}
