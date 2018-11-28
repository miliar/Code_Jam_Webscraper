#include<iostream>
#include<cstdio>

using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    int c_rule, d_rule, num_char;
    int c_table[26][26], d_table[26][26];
    int d_exist[26], pre_d[26],d_element[26];
    char comb[4],input[102], output[102];
    for (int t = 0 ; t < TIME; t++) {
	cin >> c_rule;
	if (c_rule > 0) {
	    for (int i = 0 ; i < 26; ++i) {
		for (int j = 0 ;j < 26; ++j) {
		    c_table[i][j] = -1;
		}
	    }
	    for (int i = 0 ; i < c_rule; ++i) {
		cin >> comb;
		c_table[comb[0]-'A'][comb[1]-'A'] = comb[2] - 'A';
		c_table[comb[1]-'A'][comb[0]-'A'] = comb[2] - 'A';
	    }
	}

	cin >> d_rule;
	if (d_rule > 0) {
	    for (int i = 0 ; i < 26; ++i) { 
		for (int j = 0 ; j < 26; ++j) {
		    d_table[i][j] = 0;
		}
		d_exist[i] = 0;
		pre_d[i] = 0;
		d_element[i] = 0;
	    }
	    for (int i = 0 ; i < d_rule; ++i) {
		cin >> comb;
		d_table[comb[0]-'A'][comb[1]-'A'] = 1;
		d_table[comb[1]-'A'][comb[0]-'A'] = 1;
		d_element[comb[0]-'A'] = 1;
		d_element[comb[1]-'A'] = 1;
	    }
	}

	cin >> num_char >> input; 
	int num_out;
	int now_char, pre_char;
	int d_flag;
	num_out = 0;
	for (int i = 0 ; i < num_char; ++i) {
	    d_flag = 0;
	    now_char = input[i] -'A';
	    if (c_rule > 0 && num_out > 0) {
		if (c_table[pre_char][now_char]!=-1) {
		    num_out--;
		    now_char = c_table[pre_char][now_char];
		    if (pre_d[pre_char] == num_out) {
			d_exist[pre_char] = 0;
		    }
		}
	    }
	    if (d_rule > 0 && num_out > 0) {
		if (d_element[now_char] == 1) {
		    for (int i = 0 ; i < 26; ++i) {
			if (d_exist[i] && (d_table[now_char][i] == 1)) {
			    for (int j = 0 ;j < 26; ++j) {
				d_exist[j] = 0;
			    }
			    num_out = 0;
			    d_flag = 1;
			    break;
			}
		    }
		}
	    }
	    if (d_flag == 1) {
		continue;
	    }
	    output[num_out] = now_char;
	    if (d_exist[now_char] == 0 ) {
		d_exist[now_char] = 1;
		pre_d[now_char] = num_out;
	    }
	    pre_char = now_char;
	    num_out++;
	}
if (0) {	
	cout << c_rule;
	if (c_rule > 0) {
	    for (int i = 0 ; i < 26; ++i) {
		for (int j = i ; j < 26; ++j) {
		    if (c_table[i][j]>=0) {
			cout << " " << (char)('A'+i) << (char)('A'+j) << (char)('A' + c_table[i][j]) ;
		    }
		}
	    }
	}
	cout << " " << d_rule;
	if (d_rule > 0) {
	    for (int i = 0 ; i < 26; ++i) {
		for (int j = i ; j < 26; ++j) {
		    if (d_table[i][j]==1) {
			cout << " " << (char)('A'+i) << (char)('A'+j );
		    }
		}
	    }
	}
	    cout << " " << num_char << " " << input << endl;
}
	printf("Case #%d: [",t+1);
	for (int i = 0 ; i < num_out; ++i) {
	    cout << (char)(output[i] + 'A');
	    if (i < num_out -1) cout <<", ";
	}
	printf("]\n");

	
	//output
    }
    return 0;
}
