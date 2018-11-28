#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <map>

using namespace std;

void MoveLeft(string & str)
{
    char ch = str[0];
    int loop = str.size() - 1;
    for (int i=0; i<loop; ++i)
	str[i] = str[i+1];
    str[loop] = ch;
}

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");

    int T;
    in >> T;
    string str;
    char buffer[10];
    map<int,int> match;
    for (int i=1; i<=T; ++i) {
	match.clear();
	int low, high;
	in >> low >> high;
	int rst = 0;
	for (int l=low; l<=high; ++l) {
	    sprintf(buffer, "%d", l);
	    int a = atoi(buffer);
	    str = buffer;
	    int len = str.size();
	    for (int k=0; k<len; ++k) {
		MoveLeft(str);
		int b = atoi(str.c_str());
		if (a < b && b <= high) {
		    if (match[a] != b) {
			rst ++;
			match[a] = b;
		    }
		}
	    }
	}
	out << "Case #" << i << ": " << rst << endl;
    }

    out.close();
    in.close();

    return 0;
}
