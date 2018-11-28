#include <iostream>
#include <string>
#include <iterator>
#include <set>
using namespace std;

unsigned int TC, tc;
long long ans;
string str, welcome = "welcome to code jam";
char str2[500], *welcome2 = "welcome to code jam";
set<char> chars;
string zeros;
long long soln[19][500];

void compute(int wi, int si){
	if(strlen(str2+si) < strlen(welcome2+wi)){
		soln[wi][si] = 0;
		return;
	}

	if(strcmp(welcome2+wi, str2+si) == 0){
		soln[wi][si] = 1;
		return;
	}

	//call for compute(w, s+1)
	int s1 = si+1;
	long long sum = 0;
	while(*(str2 + s1) && (*(str2 + s1) != *(welcome2+wi)))
		s1++;
	if(*(str2 + s1)){
		if(soln[wi][s1] == -1)
			compute(wi, s1);
		sum = (sum+ soln[wi][s1]%10000)%10000;
	}

	s1 = si+1;
	if(*(welcome2+wi+1) == 0)
		sum += factor;//last matching char
	else {//call for compute(w+1, s+1)
		while(*(str2 + s1) && (*(str2 + s1) != *(welcome2+wi+1)))
			s1++;
		if(*(str2 + s1)){
			if(soln[wi+1][s1] == -1)
				compute(wi+1, s1);
			sum = (sum + (soln[wi+1][s1] * factor)%10000 ) % 10000;
		}
	}

	soln[wi][si] = sum;
	return;
}

int main(){
	unsigned int i, j;
	cin >> TC;
	getline(cin, str);
	for(tc=0; tc<TC; ++tc){
		getline(cin, str);
		str.copy(str2, str.size()+1);
		str2[str.size()]=0;
		ans = 0;
		soln[0][0] = -1;
		for(j=0; j < str.size(); j++){
			for(i=0; i<19; i++){
				soln[i][j] = -1;
			}
		}
		if(str.size()){
			compute(0, 0);
			ans = soln[0][0] % 10000;
		} else
			ans = 0;
		zeros = (ans > 999) ? "" : (ans > 99) ? "0" : (ans > 9) ? "00" : "000";
		cout << "Case #" << tc+1 << ": " << zeros << ans << endl;
	}
	return 0;
}
