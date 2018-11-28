#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int t, n, s, p, count=0;

  int n0[5] = {0,0,0};
  int n1[5] = {1,0,0};
  int n2[5] = {1,1,0};
  int s2[5] = {2,0,0};
  int n3[5] = {1,1,1};
  int s3[5] = {2,1,0};
  int n4[5] = {2,1,1};
  int s4[5] = {2,2,0};
  int n5[5] = {2,2,1};
  int s5[5] = {3,1,1};
  int n6[5] = {2,2,2};
  int s6[5] = {3,2,1};
  int n7[5] = {3,2,2};
  int s7[5] = {3,3,1};
  int n8[5] = {3,3,2};
  int s8[5] = {4,2,2};
  int n9[5] = {3,3,3};
  int s9[5] = {4,3,2};
  int n10[5] = {4,3,3};
  int s10[5] = {4,4,2};
  int n11[5] = {4,4,3};
  int s11[5] = {5,3,3};
  int n12[5] = {4,4,4};
  int s12[5] = {5,4,3};
  int n13[5] = {5,4,4};
  int s13[5] = {5,5,3};
  int n14[5] = {5,5,4};
  int s14[5] = {6,4,4};
  int n15[5] = {5,5,5};
  int s15[5] = {6,5,4};
  int n16[5] = {6,5,5};
  int s16[5] = {6,6,4};
  int n17[5] = {6,6,5};
  int s17[5] = {7,5,5};
  int n18[5] = {6,6,6};
  int s18[5] = {7,6,5};
  int n19[5] = {7,6,6};
  int s19[5] = {7,7,5};
  int n20[5] = {7,7,6};
  int s20[5] = {8,6,6};
  int n21[5] = {7,7,7};
  int s21[5] = {8,7,6};
  int n22[5] = {8,7,7};
  int s22[5] = {8,8,6};
  int n23[5] = {8,8,7};
  int s23[5] = {9,7,7};
  int n24[5] = {8,8,8};
  int s24[5] = {9,8,7};
  int n25[5] = {9,8,8};
  int s25[5] = {9,9,7};
  int n26[5] = {9,9,8};
  int s26[5] = {10,8,8};
  int n27[5] = {9,9,9};
  int s27[5] = {10,9,8};
  int n28[5] = {10,9,9};
  int s28[5] = {10,10,8};
  int n29[5] = {10,10,9};
  int n30[5] = {10,10,10};

  cin >> t;
  cin.ignore();
  for (int i=0; i<t; i++) {
    count = 0;
    cin >> n >> s >> p;
    cin.ignore();
    int g[n];
    for(int j=0; j<n; j++) {
      cin >> g[j];
      cin.ignore();
    }
 
    sort(g, g + n);

    for (int j=0; j<n; j++) {
      if (g[j] == 0) {
	if (n0[0] >= p || n0[1] >= p || n0[2] >= p) count++;
      }
      if (g[j] == 1) {
	if (n1[0] >= p || n1[1] >= p || n1[2] >= p) count++;
      }
      if (g[j] == 2) {
	if (s!=0) {
	  if (s2[0] >= p || s2[1] >= p || s2[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n2[0] >= p || n2[1] >= p || n2[2] >= p) count++;
	}
      }
if (g[j] == 3) {
	if (s!=0) {
	  if (s3[0] >= p || s3[1] >= p || s3[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n3[0] >= p || n3[1] >= p || n3[2] >= p) count++;
	}
      }
if (g[j] == 4) {
	if (s!=0) {
	  if (s4[0] >= p || s4[1] >= p || s4[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n4[0] >= p || n4[1] >= p || n4[2] >= p) count++;
	}
      }
if (g[j] == 5) {
	if (s!=0) {
	  if (s5[0] >= p || s5[1] >= p || s5[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n5[0] >= p || n5[1] >= p || n5[2] >= p) count++;
	}
      }
if (g[j] == 6) {
	if (s!=0) {
	  if (s6[0] >= p || s6[1] >= p || s6[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n6[0] >= p || n6[1] >= p || n6[2] >= p) count++;
	}
      }
if (g[j] == 7) {
	if (s!=0) {
	  if (s7[0] >= p || s7[1] >= p || s7[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n7[0] >= p || n7[1] >= p || n7[2] >= p) count++;
	}
      }
if (g[j] == 8) {
	if (s!=0) {
	  if (s8[0] >= p || s8[1] >= p || s8[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n8[0] >= p || n8[1] >= p || n8[2] >= p) count++;
	}
      }
if (g[j] == 9) {
	if (s!=0) {
	  if (s9[0] >= p || s9[1] >= p || s9[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n9[0] >= p || n9[1] >= p || n9[2] >= p) count++;
	}
      }
if (g[j] == 10) {
	if (s!=0) {
	  if (s10[0] >= p || s10[1] >= p || s10[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n10[0] >= p || n10[1] >= p || n10[2] >= p) count++;
	}
 }
if (g[j] == 11) {
	if (s!=0) {
	  if (s11[0] >= p || s11[1] >= p || s11[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n11[0] >= p || n11[1] >= p || n11[2] >= p) count++;
	}
 }
if (g[j] == 12) {
	if (s!=0) {
	  if (s12[0] >= p || s12[1] >= p || s12[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n12[0] >= p || n12[1] >= p || n12[2] >= p) count++;
	}
 }
if (g[j] == 13) {
	if (s!=0) {
	  if (s13[0] >= p || s13[1] >= p || s13[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n13[0] >= p || n13[1] >= p || n13[2] >= p) count++;
	}
 }
if (g[j] == 14) {
	if (s!=0) {
	  if (s14[0] >= p || s14[1] >= p || s14[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n14[0] >= p || n14[1] >= p || n14[2] >= p) count++;
	}
 }
if (g[j] == 15) {
	if (s!=0) {
	  if (s15[0] >= p || s15[1] >= p || s15[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n15[0] >= p || n15[1] >= p || n15[2] >= p) count++;
	}
 }
if (g[j] == 16) {
	if (s!=0) {
	  if (s16[0] >= p || s16[1] >= p || s16[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n16[0] >= p || n16[1] >= p || n16[2] >= p) count++;
	}
 }
if (g[j] == 17) {
	if (s!=0) {
	  if (s17[0] >= p || s17[1] >= p || s17[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n17[0] >= p || n17[1] >= p || n17[2] >= p) count++;
	}
 }
if (g[j] == 18) {
	if (s!=0) {
	  if (s18[0] >= p || s18[1] >= p || s18[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n18[0] >= p || n18[1] >= p || n18[2] >= p) count++;
	}
 }
if (g[j] == 19) {
	if (s!=0) {
	  if (s19[0] >= p || s19[1] >= p || s19[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n19[0] >= p || n19[1] >= p || n19[2] >= p) count++;
	}
 }
if (g[j] == 20) {
	if (s!=0) {
	  if (s20[0] >= p || s20[1] >= p || s20[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n20[0] >= p || n20[1] >= p || n20[2] >= p) count++;
	}
 }
if (g[j] == 21) {
	if (s!=0) {
	  if (s21[0] >= p || s21[1] >= p || s21[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n21[0] >= p || n21[1] >= p || n21[2] >= p) count++;
	}
 }
if (g[j] == 22) {
	if (s!=0) {
	  if (s22[0] >= p || s22[1] >= p || s22[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n22[0] >= p || n22[1] >= p || n22[2] >= p) count++;
	}
 }
if (g[j] == 23) {
	if (s!=0) {
	  if (s23[0] >= p || s23[1] >= p || s23[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n23[0] >= p || n23[1] >= p || n23[2] >= p) count++;
	}
 }
if (g[j] == 24) {
	if (s!=0) {
	  if (s24[0] >= p || s24[1] >= p || s24[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n24[0] >= p || n24[1] >= p || n24[2] >= p) count++;
	}
 }
if (g[j] == 25) {
	if (s!=0) {
	  if (s25[0] >= p || s25[1] >= p || s25[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n25[0] >= p || n25[1] >= p || n25[2] >= p) count++;
	}
 }
if (g[j] == 26) {
	if (s!=0) {
	  if (s26[0] >= p || s26[1] >= p || s26[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n26[0] >= p || n26[1] >= p || n26[2] >= p) count++;
	}
 }
if (g[j] == 27) {
	if (s!=0) {
	  if (s27[0] >= p || s27[1] >= p || s27[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n27[0] >= p || n27[1] >= p || n27[2] >= p) count++;
	}
 }
if (g[j] == 28) {
	if (s!=0) {
	  if (s28[0] >= p || s28[1] >= p || s28[2] >= p) {
	    count++;
	    s--;
	  }
	}
	else {
	  if (n28[0] >= p || n28[1] >= p || n28[2] >= p) count++;
	}
 }
if (g[j] == 29) {
	if (n29[0] >= p || n29[1] >= p || n29[2] >= p) count++;
      }
if (g[j] == 30) {
	if (n30[0] >= p || n30[1] >= p || n30[2] >= p) count++;
      }











    
    /*for (int j=0; j<n; j++) {
      cout << g[j] << endl;
      }*/


    } 
    cout << "Case #" << i+1 << ": " << count << endl; 
  }
  return 0;
}
