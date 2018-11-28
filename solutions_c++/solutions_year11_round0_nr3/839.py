#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
	int count_this;
	int ans_count = 0;
	int now_ans[2][1048576];
	int tmp_ans[1048576];
	int tmp1, tmp2, max_num;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    int C[1000];
    int N, tmp_in;
    int base2[21];
    int base_i;
    int ans_flag;
    int base_table[20][1000];
    int base_count[20];
    int sum = 0;
    int label[1000];
    for (int t = 0 ; t < TIME; t++) {
	sum = 0;
	cin >> N;
	for (int i = 0 ; i < 21; ++i) {
	    base2[i] = 0;
	    base_count[i] = 0;
	}
	for (int i = 0 ; i < N; ++i) {
	    cin >> tmp_in;
	    C[i] = tmp_in;
	    sum += tmp_in;
	    base_i = 0;
	    label[i] = 0;
	    while(tmp_in!=0) {
		base2[base_i] += tmp_in % 2;
		tmp_in/=2;
		base_i++;
	    };
	}

	ans_flag = 1;
	for (int i = 0 ; i < 21; ++i) {
	    if (base2[i]%2==1) {
		ans_flag = 0;
		break;
	    }
	}

	//output
	if (ans_flag == 1) {
	    sort (C, C+N);
	    max_num = sum - C[0];
	    
	}

	if (ans_flag ==1) {
	    printf("Case #%d: %d\n" ,t+1, max_num);
	}
	else {
	    printf("Case #%d: NO\n" ,t+1);
	}
    }
    return 0;

    }
