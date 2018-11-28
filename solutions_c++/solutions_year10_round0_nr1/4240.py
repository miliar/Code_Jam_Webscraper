#include <iostream>
#include <string>
using namespace std;
/* start: power = 00000001; state = 00000000 */
/* snap:  power = 00000011; state = 00000001 */
/* snap:  power = 00000001; state = 00000010 */
/* snap:  power = 00000011; state = 00000001 */

int main() {
	int t;
	cin >> t;
	unsigned power; unsigned state;
	for(int i = 0; i < t; i++) {
		int n, k;
		cin >> n >> k;
		power = 0x1;
		state = 0x0;
		for(int itr = 0; itr < k; itr++) { 
			int toggles = ~state & power;
			int untouched = state & ~power;
			state = toggles | untouched;
			int low_bit_idx;
			if(state == 0) {
				low_bit_idx = 0; 
			} else {
				low_bit_idx = __builtin_ctz(~state);
			}
			low_bit_idx++;
			power = 0;
			for(int j = 0; j < low_bit_idx; j++) {
				power |= 1 << j;
			}
		}
		string ans = "OFF";
		if(power & (1 << n)) ans = "ON";

		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
