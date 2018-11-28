#include <iostream>
#include <string>
using namespace std;

void result(int num, string buf)
{
	int i;
	cout << "Case #" << num << ": [";
	if(buf.size() > 0) {
		cout << buf[0];
		for(i = 1; i < buf.size(); i++)
			cout << ", " << buf[i];
	}
	cout << "]" << endl;
}

void solve(int num)
{
	int i, j, k;
	int com, opp, len, buflen;
	cin >> com;
	string combine[com];
	for(i = 0; i < com; i++)
		cin >> combine[i];
	cin >> opp;
	string oppose[opp];
	for(i = 0; i < opp; i++)
		cin >> oppose[i];
	cin >> len;
	string word;
	cin >> word;
	string buf = "";
	for(i = 0; i < len; i++) {
		buf += word[i];
		buflen = buf.size() - 1;
		if(buflen > 0) {
			for(j = 0; j < com; j++) {
				if(buf[buflen - 1] == combine[j][0] && buf[buflen] == combine[j][1]) {
					buf = string(buf, 0, buflen - 1) + combine[j][2];	
					break;
				} else if(buf[buflen - 1] == combine[j][1] && buf[buflen] == combine[j][0]) {
					buf = string(buf, 0, buflen - 1) + combine[j][2];
					break;
				}
			}
		}
		buflen = buf.size() - 1;
		if(buflen > 0) {
			for(j = 0; j < opp; j++) {
				if((buf.find(oppose[j][0], 0) != string::npos) && (buf.find(oppose[j][1], 0) != string::npos)) {
					buf = "";
					break;
				}
/*
				for(k = 0; k < buf.size() / 2; k++) {
					if(buf[k] == oppose[j][0] && buf[buflen - k] == oppose[j][1]) {
						buf = "";
						break;
					} else if(buf[k] == oppose[j][1] && buf[buflen - k] == oppose[j][0]) {
						buf = "";
						break;
					}
				}
*/
			}
		}
	}
	result(num, buf);
}

int main(void)
{
	int i, n;
	cin >> n;
	for(i = 0; i < n; i++)
		solve(i + 1);
	return 0;
}
