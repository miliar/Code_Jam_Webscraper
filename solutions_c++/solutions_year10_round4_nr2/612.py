#include <cstdio>
#include <iostream>

using namespace std;

const int MAX_TEAMS = 10000;
const int MAX_MATCHES = MAX_TEAMS;

int p;
int minCount[MAX_TEAMS];
int price[MAX_MATCHES];
bool buyTicket[MAX_MATCHES];

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d", &p);
    int nTeams = 1 << p;
    int nMatches = nTeams - 1;

    for (int i = 0; i < nTeams; i++) {
      scanf("%d", &minCount[i]);
    }
    for (int i = 0; i < nMatches; i++) {
      scanf("%d", &price[i]);
    }

    fill(buyTicket, buyTicket + nMatches, false);
    int totalPrice = 0;

    for (int i = 0; i < nTeams; i++) {
      for (int j = 0; j < p - minCount[i]; j++) {
        int iMatch = nTeams - (1 << (j + 1)) + (i >> (p - j));
        //cout << "team=" << i << " j=" << j << " iMatch=" << iMatch << endl;
        if (!buyTicket[iMatch]) {
          buyTicket[iMatch] = true;
          totalPrice++;
        }
      }
    }
    
    cout << "Case #" << iCase << ": " << totalPrice << endl;
  }
  return 0;
}
