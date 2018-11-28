// in this program, I assume that character code is ascii (or compatible to ascii),
// and that the values of 'A' to 'Z' are continuous. 

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {
  if(argc < 3)
    return 0;

  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  int num_cases;
  ifs >> num_cases;
  for(int i=1;i<=num_cases;i++){
    ofs << "Case #" << i << ": ";

    int combine_list[26][26];
    memset(combine_list, 0, sizeof(int) * 26 * 26);
    int oppose_list[26][26];
    memset(oppose_list, 0, sizeof(int) * 26 * 26);

    int n;
    ifs >> n;
    for(int k=0;k<n;k++){
      char str[4];
      ifs >> str;
      combine_list[str[0] - 'A'][str[1] - 'A'] = str[2];
      combine_list[str[1] - 'A'][str[0] - 'A'] = str[2];
    }
    ifs >> n;
    for(int k=0;k<n;k++){
      char str[3];
      ifs >> str;
      oppose_list[str[0] - 'A'][str[1] - 'A'] = 1;
      oppose_list[str[1] - 'A'][str[0] - 'A'] = 1;
    }

    ifs >> n;
    char str[100];
    char output[100];
    int output_len = 0;
    ifs >> str;
    bool flag;
    for(int k=0;k<n;k++){
      if(output_len == 0){
	output[0] = str[k];
	output_len++;
	continue;
      }

      // combine?
      char c = combine_list[output[output_len - 1] - 'A'][str[k] - 'A'];
      if(c != 0)
	output[output_len - 1] = c;
      else {
	// opposed?
	flag = true;
	for(int c=0;c<output_len;c++) {
	  if(oppose_list[output[c] - 'A'][str[k] - 'A'] != 0) {
	    output_len = 0;
	    flag = false;
	    break;
	  }
	}
	if(flag)
	  output[output_len++] = str[k];
      }
    }

    ofs << "[";
    for(int c=0;c<output_len;c++){
      if(c != 0)
	ofs << ", ";
      ofs << output[c];
    }
    ofs << "]" << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}
