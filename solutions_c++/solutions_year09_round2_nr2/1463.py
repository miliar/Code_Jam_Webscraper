#include <iostream>
#include <string>
#include <algorithm>
using namespace std; 
int compare (string a, string b) {
  while (a[0] == '0') a.erase(a.begin()+0);
  while (b[0] == '0') b.erase(b.begin()+0);
  if (a.size() > b.size()) return 1;
  if (b.size() > a.size()) return 0;
  if (a > b) return 1;
  return 0;
}
string solve(string curnum) {
  string aux,aux2, mine = "9999999999";
  int i,j,k;
  curnum = '0' + curnum;
  for (i = curnum.size()-1; i >= 0 ; i--) {
    for (j = i-1 ; j >= 0 ; j--) {
      if (curnum[i] != curnum[j]) {
	aux = curnum;
	aux.erase(aux.begin()+i);
	aux.insert(aux.begin()+j,curnum[i]);
	stable_sort(aux.begin()+j+1,aux.end());
	//	cout << aux << "\n";
	if (!compare(aux,mine) && compare(aux,curnum)) {
	  mine = aux;
	}
	else {
	  for (k = 1 ; k < aux.size() ; k++) {
	    aux2 = aux;
	    aux2.insert(aux2.begin()+k,'0');
	    stable_sort(aux2.begin()+k+1,aux2.end());
	    //  cout << aux2 << "\n";
	    if (!compare(aux2,mine) && compare(aux2,curnum)) {
	      mine = aux2;
	    }
	  }
	}
      }
    }
  }
  for (i = 0 ; i < curnum.size() ; i++) {
    for (j = i+1 ; j < curnum.size() ; j++) {
      if (curnum[i] != curnum[j]) {
	aux = curnum;
	aux.erase(aux.begin()+i);
	aux.insert(aux.begin()+j,curnum[i]);
	stable_sort(aux.begin()+j+1,aux.end());
	//	cout << aux << "\n";
	if (!compare(aux,mine) && compare(aux,curnum)) {
	  mine = aux;
	}
	else {
	  for (k = 1 ; k < aux.size() ; k++) {
	    aux2 = aux;
	    aux2.insert(aux2.begin()+k,'0');
	stable_sort(aux2.begin()+k+1,aux2.end());
	    //	    cout << aux2 << "\n";
	    if (!compare(aux2,mine) && compare(aux2,curnum)) {
	      mine = aux2;
	    }
	  }
	}
      }
    }
  }
  while (mine[0] == '0') 
    mine.erase(mine.begin()+0);
  return mine;
	
}
int main() {
  int N,i;
  string num;
  scanf("%d",&N);
  for (i = 1 ; i <= N ; i++) {
    cin >> num;
    cout << "Case #" << i << ": " << solve(num) << "\n";
  }
  return 0;
}
