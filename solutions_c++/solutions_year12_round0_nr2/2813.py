#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("B.in");
    ofstream out("B.out");

    int T;
    in >> T;
    for (int i=1; i<=T; ++i) {
	int N, S, P;
	in >> N >> S >> P;
	int rst = 0;
	int line = P * 3;
	out << "Case #" << i << ": ";
	while (N--) {
	    int num;
	    in >> num;
	    cout << num << ":";
	    if (num == 0 && line != 0) {
		continue;
	    } else if (num >= line) {
		rst++;
	    } else if (line-num == 1) {
		rst++;
	    } else if (line-num == 2) {
		rst++;
	    } else if (line-num == 3 || line-num == 4) {
		if (S > 0) {
		    S--;
		    rst++;
		}
	    }
	    cout << rst << endl;
	}
	out << rst << endl;
    }

    out.close();
    in.close();

    return 0;
}
