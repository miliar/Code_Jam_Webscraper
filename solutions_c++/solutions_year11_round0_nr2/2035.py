#include<iostream>
#include<string>
#include<cstdio>
#include<vector>

using namespace std;
char find_combine(char a, char b, vector<string> combine);

char find_combine(char a, char b, vector<string> combine) {
	int size = combine.size();
	for(int i = 0; i < size; i++) {
		if(combine[i][0] == a && combine[i][1] == b)
			return combine[i][2];
		if(combine[i][0] == b && combine[i][1] == a)
			return combine[i][2];
	}
	return 'Q';
}
int find_ind(char ch) {
	//{Q, W, E, R, A, S, D, F}
	switch(ch) {
	case 'Q' : return 0;
	case 'W' : return 1;
	case 'E' : return 2;
	case 'R' : return 3;
	case 'A' : return 4;
	case 'S' : return 5;
	case 'D' : return 6;
	case 'F' : return 7;
	default : return 8;
	}
}
	
main()
{
	int t, n, c, d, no = 1;
	scanf("%d", &t);
	vector<string> combine(10);
	vector< vector<int> > oppose(8, vector<int> (8, 0));
	while(t--) {
		scanf("%d ", &c);
//		cout<<"C: "<<c<<endl;
		combine.resize(c);
		for(int i = 0; i < c; i++) {
			cin>>combine[i];
		}
		scanf("%d ", &d);
//		cout<<"D: "<<d<<endl;
		for(int i = 0; i < 8; i++) {
			for(int j = 0; j < 8; j++) {
				oppose[i][j] = 0;
			}
		}
		char opp1, opp2;
		int ind1, ind2;
		for(int i = 0; i < d; i++) {
			scanf("%c", &opp1);
			scanf("%c", &opp2);
			ind1 = find_ind(opp1);
			ind2 = find_ind(opp2);
			oppose[ind1][ind2] = 1;
			oppose[ind2][ind1] = 1;
//			cout<<"Opposing pairs: "<<opp1<<" "<<opp2<<endl;
			scanf("%c", &opp1);
		}
//		cout<<"Taking striing input"<<endl;
		scanf("%d ", &n);
		string s = "";
		char ch, new_ch;
		int size = 0;
		for(int i = 0; i < n; i++) {
//			cout<<"String till now: "<<s<<endl;
			scanf("%c", &ch);
//			cout<<"invoked char: "<<ch<<endl;
			new_ch = 'Q';
			if(size != 0) {
				new_ch = find_combine(ch, s[size-1], combine);
			}
			if(new_ch != 'Q') {
				s[size-1] = new_ch;
			}else {
			//TODO: Check if oppose.
				s += ch;
				size++;
				ind1 = find_ind(ch);
				for(int j = 0; j < size - 1; j++) {
					ind2 = find_ind(s[j]);
					if(ind2 != 8 && oppose[ind1][ind2] == 1) {
						s = "";
						size = 0;
						break;
					}
				}
			}
		}
		printf("Case #%d: [", no++);
		if(size!=0)
		printf("%c", s[0]);
		for(int i = 1; i < size; i++) {
			printf(", %c", s[i]);
		}
		printf("]\n");
	}
}
