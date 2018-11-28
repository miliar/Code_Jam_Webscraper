#include<iostream>
#include<cmath>

using namespace std;

bool __inline is_integer(float f){
    int i = f;
    return (f == static_cast<float>(i));
}

string solve() {
	int n, pd, pg;
	cin >> n >> pd >> pg;
	if (pg == 100 && pd < 100) return "Broken";
	if (pg == 0 && pd > 0) return "Broken";
	
	int d = 1;
	double p = (double)pd / 100.0;
	while (d <= 100) {
		if (is_integer(p)) break;
		p += (double)pd /100.0;
		d++;
	} 
	if (d <= n) return "Possible";
	else return "Broken";
}

int main() {
	int tc; cin >> tc;

	for (int t = 1; t <= tc; t++) cout << "Case #" << t << ": " << solve() << endl;

	return 0;
}
