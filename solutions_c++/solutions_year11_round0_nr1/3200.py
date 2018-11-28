#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;

typedef struct {
    bool orange;
    int button;
} sequence;

int main() {
    freopen("out.txt", "w", stdout);
    int cases, n, b, i, j;
    string c;
    cin >> cases;
    for (int cas=1;cas<=cases;cas++) {
	cin >> n;
	
	sequence* seq = new sequence[n + 1];
	for (i=0;i<n;i++) {
	    cin >> c;
	    cin >> b;
	    seq[i].orange = (c == "O");
	    seq[i].button = b-1;
	}

	int time = 0, cur = 0;
	int opos = 0, bpos = 0;

	for (i=1;;i++) {
	    //cout << "Current Step " << i << endl;
	    if (seq[cur].orange) {
		if (opos == seq[cur].button) {
		    //cout << "Orange pressing button " << seq[cur].button << endl;
		    
		    cur ++;
		    //cout << "Current Sequence " << cur << endl;
		    if (cur >= n)
			break;
		} else {
		    //cout << "Orange Moving to button " << seq[cur].button << endl;
		    if (seq[cur].button > opos)
			opos ++;
		    else
			opos --;
		}
		for (j=cur;j<n;j++) {
		    if (!seq[j].orange)
			break;
		} 
		if (j < n) {
		    //cout << "Blue Moving to button " << seq[j].button << endl;
		    if (seq[j].button > bpos)
			bpos ++;
		    else if (seq[j].button < bpos)
			bpos --;
		}
	    } else {
		if (bpos == seq[cur].button) {
		    //cout << "Blue pressing button " << seq[cur].button << endl;
		    cur ++;
		    //cout << "Current Sequence " << cur << endl;
		    if (cur >= n)
			break;
		} else {
		    //cout << "Blue Moving to button " << seq[cur].button << endl;
		    if (seq[cur].button > bpos)
			bpos ++;
		    else
			bpos --;
		}
		for (j=cur;j<n;j++) {
		    if (seq[j].orange)
			break;
		} 
		if (j < n) {
		    //cout << "Orange Moving to button " << seq[j].button << endl;
		    if (seq[j].button > opos)
			opos ++;
		    else if (seq[j].button < opos)
			opos --;
		}

	    }
	}

	delete[] seq;
	cout << "Case #" << cas << ": " << i << endl;
	
    }
}
