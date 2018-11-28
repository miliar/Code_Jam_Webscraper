#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <map>
#include <iomanip>
#include <cmath>

#include "LiDIA/bigint.h"
#include "LiDIA/isstream.h"
#include "LiDIA/osstream.h"

using namespace LiDIA;


using namespace std;


int main()
{
	int C;
	cin >> C;
	for (int c=0;c<C;c++) {

		cout << "Case #" << c+1 << ": ";
		
		int H, W;
		cin >> H >> W;
		int R;
		cin >> R;
		
		set<pair<int,int> > forbid;
		
		for (int i=0;i<R;i++) {
			int x, y;
			cin >> x >> y;
			forbid.insert(make_pair(x-1,y-1));
		}
		
		if ((H+W)%3 != 2) {
			cout << "0" << endl;
			continue;
		}
		
		vector<bigint> prevDiag(H+W), diag(H+W);
		
		prevDiag[0]=1;
		
		for (int d=3;d<H+W-1;d+=3) {
			for (int i=min(d, H-1); i>=0; i--) {
				// for (int j=max(0, d-H); j<=min(d, W-1); j++) {
					
				//}
				
				int j = d-i;
				
				diag[i]=0;
				
				if (forbid.find(make_pair(i,j)) == forbid.end()) {
					if (i>0) diag[i]+=prevDiag[i-1];
					if (i>1) diag[i]+=prevDiag[i-2];
				}
			}
			
			diag.swap(prevDiag);
		}
		
		cout << prevDiag[H-1]%10007 << endl;
	}
}
