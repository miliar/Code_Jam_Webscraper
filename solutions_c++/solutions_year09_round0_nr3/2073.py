#include<vector>
#include<iostream>
#include<fstream>
using namespace std;

void dfs(vector<int> &idxlist, vector<vector<int> > &freqlist, int idx, int &count) {
  if(freqlist.size() == idx) {
    count = (count+1)%10000;
    return;
  }
  for(int i = 0; i < freqlist[idx].size(); i++) {
    idxlist[idx] = freqlist[idx][i];
    if(idx > 0) {
      if(idxlist[idx-1] > idxlist[idx]) continue;
    }
    dfs(idxlist, freqlist, idx+1, count);
  }
}

vector<vector<int> > IndexAccumulator(char *str, const string & comparestr) {
  vector<vector<int> > vvi;
  if(str == NULL) return vvi;
  int lenstr = strlen(str);
  if(lenstr == 0) return vvi;
  
  for(int i = 0; i < comparestr.size(); i++) {
    int idx = 0;
    vector<int> vi;
    while(idx < lenstr) {
      if(str[idx] == comparestr[i]) vi.push_back(idx);
      idx++;
    }
    vvi.push_back(vi);
  }
  return vvi;
}

bool IndexSorter(vector<vector<int> > &vvi) {
  sort(vvi[0].begin(), vvi[0].end());
  for(int i = 1; i < vvi.size(); i++) {
    sort(vvi[i].begin(), vvi[i].end());
    if(vvi[i-1][0] > vvi[i][vvi[i].size()-1 ]) return false;
    int j = 0;
    while(j < vvi[i].size()) {
      if(vvi[i][j] < vvi[i-1][0]) break; 
      j++;
    }
    if(j > 0) vvi[i].erase(vvi[i].begin(), vvi[i].begin()+j-1);
  }
  return true;
}

int main(int argc, char*argv[]) {
  if(argc < 2) return -1;
  ifstream infile(argv[1]);
  int numtests = 0;
  infile >> numtests;
  string comparestr = "welcome to code jam";
  char inputstring[501];
  infile.getline(inputstring, 501);// Get the new line character.
  vector<int> idxlist(comparestr.size(), 0);
  for(int i = 0; i < numtests; i++) {
    memset(inputstring, 0, 501);
    infile.getline(inputstring, 501);
    vector<vector<int> > vvi = IndexAccumulator(inputstring, comparestr);
    int lidx = 0;
    int count = 0;
    for(lidx = 0; lidx < vvi.size(); lidx++) if(vvi[lidx].size() == 0) break;
    if(lidx == vvi.size()) {
      dfs(idxlist, vvi, 0, count);
      /*
      bool retval = IndexSorter(vvi);
      if(retval) {
	count = 1;
	for(int idx = 0; idx < vvi.size(); idx++) {
	  count *= vvi[idx].size();
	}
      }
      */
    }

    cout << "Case #" << (i+1) << ": ";
    count = count % 10000;
    unsigned int show = (count-count%1000);
    cout << show/1000;
    
    count = count - show;
    show = (count-count%100);
    cout << show/100;
    
    count = count - show;
    show = (count-count%10);
    cout << show/10;

    count = count - show;
    show = count;
    cout << show/1;

    cout << endl;
  }
  return 0;
}
