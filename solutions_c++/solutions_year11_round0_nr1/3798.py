#include <iostream>
#include <vector>


using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		
		int ocur = 1;
		int bcur = 1;
		vector < bool > m1; //orange = true, blue = false
		vector < int > m2;
		
		int n;
		cin >> n;
		m1.resize(n);
		m2.resize(n);
		for (int i = 0; i < n; i++) {
			char r;
			int p;
			cin >> r >> p;
			m1[i] = r == 'O';
			m2[i] = p;
		}
		
		int ans = 0;
		int omove = 0;
		int bmove = 0;
		
		//find first moves
		if (m1[0]) { // first bot is orange
			//find first blue move
			while (bmove < n && m1[bmove])
				bmove++;
		} else { // first bot is blue
			//find first orange move
			while (omove < n && !m1[omove])
				omove++;
		}
		
		while (omove < n || bmove < n) {
			
			if (omove < bmove) { // orange press next
				int otar = m2[omove];
				int oinc;
				if (ocur < otar)
					oinc = otar - ocur;
				else
					oinc = ocur - otar;
				ans += oinc + 1; //move orange and press button
				ocur = otar;
				//look for next orange move
				omove++;
				while (omove < n && !m1[omove])
					omove++;
				
				//move blue
				if (bmove < n) { //if there are any blue moves
					int btar = m2[bmove];
					int binc = bcur - btar;
					if (binc < 0) { //blue to left of target
						if (-binc > oinc + 1) { //blue wont get to target before next orange press
							bcur += oinc + 1;
						} else { //blue will get to target before next orange press
							bcur = btar;
						}
					} else { //blue to right of target
						if (binc > oinc + 1) { //blue wont get to target before next orange press
							bcur -= oinc + 1;
						} else { //blue will get to target before next orange press
							bcur = btar;
						}
					}
				}
// 				cout << ans << " O " << ocur << ' ' << bcur <<endl;
			} else { // blue press next
				int btar = m2[bmove];
				int binc;
				if (bcur < btar)
					binc = btar - bcur;
				else
					binc = bcur - btar;
				ans += binc + 1; //move blue and press button
				bcur = btar;
				//look for next blue move
				bmove++;
				while (bmove < n && m1[bmove])
					bmove++;
				
				//move orange
				if (omove < n) { //if there are any orange moves
					int otar = m2[omove];
					int oinc = ocur - otar;
					if (oinc < 0) { //orange to left of target
						if (-oinc > binc + 1) { //orange wont get to target before next blue press
							ocur += binc + 1;
						} else { //orange will get to target before next blue press
							ocur = otar;
						}
					} else { //orange to right of target
						if (oinc > binc + 1) { //orange wont get to target before next blue press
							ocur -= binc + 1;
						} else { //orange will get to target before next blue press
							ocur = otar;
						}
					}
				}
// 				cout << ans << " B " << ocur << ' ' << bcur <<endl;
			}
			
		}
		
		cout << ans << endl;
	}
}