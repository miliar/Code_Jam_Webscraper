#include<iostream>
#include<cstdio>

using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    int N, in[1001], index[1001], label[1001];
    double ans;
    int count;
    for (int t = 0 ; t < TIME; t++) {
	count = 0;
	ans = 0.0;
	cin >> N;
	for (int i = 1 ; i <= N; ++i) {
	    cin >> in[i];
	    index[i] = i;
	    if (in[i] == i) {
		label[i] = 1;
	    }
	    else{
		label[i] = 0;
	    }
	}
	
	int cycle, now_index;

	for (int i = 1; i <=N; ++i) {
	    if (label[i] == 1)
		continue;
	    label[i] = 1;
	    cycle = 1;
	    now_index = in[i];
	    do {
		label[now_index] = 1;
		now_index = in[now_index];
		cycle++;
	    }while (label[now_index]==0);
	    count += cycle;
	}
	//output
	printf("Case #%d: %lf\n",t+1, (double)count);
    }
    return 0;
}
