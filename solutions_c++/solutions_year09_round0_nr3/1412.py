#include<iostream>
#include<string>
#include<vector>
using namespace std;


const char* input_str = "welcome to code jam";

vector< vector<int>* > counts;
int getCount(string& inp,
	     int inp_pos,
	     int start_pos) {
  if (start_pos == strlen(input_str)) {
    //    cout << "return 1" << endl;
    return 1;
  }
  if (inp_pos == inp.length()) {
    //    cout << "return 0" << inp <<  endl;
    return 0;
  }
  if ((*counts[start_pos])[inp_pos] != -1) {
    //    cout << "return dp" << endl;
    return (*counts[start_pos])[inp_pos];
  }
  int count = 0;
  if (inp[inp_pos] == input_str[start_pos]) {
    //    cout << "matching " << inp[inp_pos] << endl;
    count += getCount(inp, inp_pos+1, start_pos+1);
  }
  count += getCount(inp, inp_pos+1, start_pos);
  count %= 10000;
  (*counts[start_pos])[inp_pos] = count;
  //  cout << count << ":" << start_pos << ":" << inp_pos << endl;
  return count;
}

int main(int argc, char * argv[])
{
  int T;
  cin >> T;
  char tmp[2];
  cin.getline(tmp, 1);
  for (int t = 0; t < T; t++) {
    char temp_str[512];
    cin.getline(temp_str, 512);
    string temp(temp_str);
    //    cout << temp;
    counts.clear();
    for (int l = 0; l < strlen(input_str); l++) {
      vector<int>* inpv = new vector<int>(temp.length(), -1);
      counts.push_back(inpv);
    }
    int count = getCount(temp,0, 0);
    cout << "Case #" << t+1 << ": ";
    printf("%04d\n", count);
  }
}
