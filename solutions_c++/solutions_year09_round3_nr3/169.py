#include <iostream>
#include <string>

#define MAX_Q 101

using namespace std;

int n, q;
int v[MAX_Q];

int m[MAX_Q][MAX_Q];

int main() {
  int t;
  cin >> t;
  for (int k=1;k<=t;k++) {
    cin >> n >> q;
    for (int i=0;i<q;i++)
      cin >> v[i];

    if (q==1)
      cout << "Case #" << k << ": " << n-1 << endl;
    else {
      memset(m, 0x7F, sizeof(m));
      
      m[0][0]=v[1]-2;
      for (int i=1;i<q-1;i++) 
	m[i][i]=v[i+1]-v[i-1]-2;
      m[q-1][q-1]=n-v[q-2]-1;
    

      for (int i=1;i<q-1;i++) {

	//first
	int next= (i+1 != q)?v[i+1]:n;
	m[0][i]=min(m[0][i], next-2 + m[1][i]);
	for (int p=1;p<i;p++)
	  m[0][i]=min(m[0][i], next-2 + m[0][p-1] + m[p+1][i]);
	m[0][i]=min(m[0][i], next-2 + m[0][i-1]);

	//between j and j+i
	for (int j=1;j+i<q-1;j++) {
	  m[j][j+i]=min(m[j][j+i], v[j+i+1]-v[j-1]-2 + m[j+1][j+i]);

	  for (int p=j+1;p<j+i;p++)
	    m[j][j+i]=min(m[j][j+i], v[j+i+1]-v[j-1]-2 + m[j][p-1] + m[p+1][j+i]);

	  m[j][j+i]=min(m[j][j+i], v[j+i+1]-v[j-1]-2 + m[j][j+i-1]);
	}

	//last
	int previous=(q-i-2>=0)?v[q-i-2]:0;
	m[q-i-1][q-1]=min(m[q-i-1][q-1], n-previous-1 + m[q-i][q-1]);
	for (int p=q-i;p<q-1;p++)
	  m[q-i-1][q-1]=min(m[q-i-1][q-1], n-previous-1 + m[q-i-1][p-1] + m[p+1][q-1]);
	m[q-i-1][q-1]=min(m[q-i-1][q-1], n-previous-1 + m[q-i-1][q-2]);

      } 
      m[0][q-1]=min(m[0][q-1], n-1 + m[1][q-1]);
      for (int p=1;p<q-1;p++)
	m[0][q-1]=min(m[0][q-1], n-1 + m[0][p-1] + m[p+1][q-1]);
      m[0][q-1]=min(m[0][q-1], n-1 + m[0][q-2]);

      /*
      for (int i=0;i<q;i++) {
	for (int j=0;j<q;j++)
	  cout << (i>j?0:m[i][j]) << " ";
	cout << endl;
      }
      */

      cout << "Case #" << k << ": " << m[0][q-1] << endl;
    }
  }
  return 0;
}
