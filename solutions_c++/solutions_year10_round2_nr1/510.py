#include <iostream>
#include <string>
#include <map>
using namespace std;

int t,n,m;
map<string,int> mapa;


int main() {
    cin >> t;
    for (int l=1;l<=t;l++) {
    int num = 0;
        cin >> n >> m;
        for (int j=0;j<n;j++) {
            string s;
            cin >> s;
            while ( true ) {
                  mapa[s] = 0;
                  int pos1 = s.find_last_of("/");
                  int pos2 = s.find_first_of("/");
                  if (pos1 == pos2)
                     break;
                  s.erase(pos1,(int)s.size() - pos1);
            }
        }
        for (int j=0;j<m;j++) {
            string s;
            cin >> s;
            while ( true ) {
                  if (mapa.find(s) == mapa.end())
                      mapa[s] = 1;
                  num++;
                  int pos1 = s.find_last_of("/");
                  int pos2 = s.find_first_of("/");
                  if (pos1 == pos2)
                     break;
                  s.erase(pos1,(int)s.size()-pos1);
            }
        }
     
        int resp = 0;
        for (map<string,int>::iterator it = mapa.begin(); it != mapa.end(); it++) {
            //cout << it->first << " " << it->second << endl;
            resp += (*it).second;
        }
        cout << "Case #" << l << ": " << resp << " " << num << endl;
        mapa.clear();
    }
    return 0;
}
