#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int cc(int a,int b)
{
	if(a == 0) return 1;
	else if(a == 1) return b;
	else return (cc(a-1,b) * (b - a + 1) / a) % 100003;
}
int main(){
	ifstream in("input");
	ofstream out("output");
	int cases;
	in >> cases;
	int table[30][30] = {0};
	for(int i = 2; i <= 25; i++)
		table[i][1] = 1;
	for(int i = 2; i <= 25; i++)
		for(int j = 2; j < i; j++)
		{
			int pos = 1;
			int cnt = 0;
			while(1){
			if(j - pos - 1 < 0) break;
			if(i - j - 1 >= j - pos - 1){
				cnt += table[j][pos] * cc(j-pos-1,i-j-1);
			}

			pos++;
			}
			table[i][j] = cnt % 100003;
		}
	for(int i = 2; i <= 25; i++)
	{
		for(int j = 1; j < i; j++){
			cout << table[i][j] << " ";
		}
		cout << endl;
	}
	for(int casenum = 1; casenum <= cases; casenum++){
		out << "Case #" << casenum << ": ";
		cout << "Case " << casenum << endl;
		int n;
		in >> n;
		int cnt = 0;
		for(int i = 1; i < n; i++){
			cnt += table[n][i] % 100003;
			cnt = cnt % 100003;
		}
		out << cnt << endl;

	}
	return 0;
}
