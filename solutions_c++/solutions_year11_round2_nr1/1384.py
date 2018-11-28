/*OMG i have a fever :(
 */
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int main() {
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        int N;
        cin >> N;
        vector<vector<char> > scores;
        scores.resize(N);
        for(int i=0; i<N; i++) {
	  scores[i].resize(N);
	  for(int j=0; j<N; j++)
	      cin >> scores[i][j];
        }
        vector<int> ilewin;
        vector<int> ileall;
        ilewin.resize(N,0);
        ileall.resize(N,0);
        for(int i=0; i<N; i++) {
	  for(int j=0; j<N; j++)
	      if(scores[i][j] != '.') {
		ileall[i]++;
		if(scores[i][j] == '1')
		    ilewin[i]++;
	      }
        }
        vector<double> owp;
        owp.resize(N,0.0);
        for(int i=0; i<N; i++) {
	  for(int j=0; j<N; j++) {
	      if(scores[i][j] == '1')
		owp[i] += double(ilewin[j]) / double(ileall[j]-1);
	      if(scores[i][j] == '0') 
		owp[i] += double(ilewin[j]-1) / double(ileall[j]-1);
	  }
        }
        
        cout << "Case #" << z << ":\n";
        for(int i=0; i<N; i++) {
	  double m_wp=0, m_owp=0, m_oowp=0;
	  m_wp = double(ilewin[i]) / double(ileall[i]);
	  m_owp = double(owp[i]) / double(ileall[i]);
	  
	  for(int j=0; j<N; j++) {
	      if(scores[i][j] != '.')
		m_oowp += owp[j] / double(ileall[j]);
	  }
	  m_oowp /= double(ileall[i]);
// 	  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
// 	  cerr << "player " << char('A'+i) << endl;
// 	  cerr << "wp: " << m_wp << endl;
// 	  cerr << "owp: " << m_owp << endl;
// 	  cerr << "oowp: " << m_oowp << endl;
	  printf("%.12lf\n", 0.25 * m_wp + 0.5 * m_owp + 0.25 * m_oowp);
        }
        
    }
    return 0;
}