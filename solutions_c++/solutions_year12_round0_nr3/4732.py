#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <list>
#include <map>

using namespace std;

list <int> 
digitalize(int num) 
{
  list <int> digits;
  int i = 1;
  int divider = 10;
  int n = num;

  while (n >= divider) {
     int remainder = n % divider;
     digits.push_back(remainder);
	n /= divider;
  }
  digits.push_back(n);
  reverse(digits.begin(), digits.end());
  return digits;
}

int 
numerize(list <int> M) 
{
	int num = 0;
	list <int> :: iterator it = M.begin();
	for (; it != M.end(); it++) {
	     num = num * 10 + *it;
	}
	return num;
}

void
flip_check (list <int> D, int A, int B, int *count) 
{
   int N = D.size();
   list <int> M (N);
   if (N <= 1) {
	  return;
   }
   int orig = numerize(D);
   map <int, int> pairs;
   map <int, int> ::iterator pairs_it;

   int i = 1;
   while (i<=N) {
	   list <int> :: iterator index = D.begin();
	   advance(index, i);
	   if (*index == 0) {
		  i++;
		  continue;
	   }

	   int j = 0;
        copy(D.begin(), D.end(), M.begin());
        while (j < i) {
		   int ele = M.front();
		   M.pop_front();
		   M.push_back(ele);
		   j++;
	   }
	   int new_num = numerize(M);

	   pairs_it = pairs.find(orig);
	   if (pairs_it == pairs.end()) {
	      if (new_num <= B && new_num > orig) {
		     *count = *count + 1;
		     //cout << orig << " " << new_num << endl;
	      } else if (new_num < orig && new_num < A) {
	      }
		 pairs.insert(pair <int,int>(orig, new_num));
	   } else if (pairs_it->second != new_num) {
	      if (new_num <= B && new_num > orig) {
		     *count = *count + 1;
		     //cout << orig << " " << new_num << endl;
	      } else if (new_num < orig && new_num < A) {
	      }
		 pairs.insert(pair <int,int>(orig, new_num));
	   }
	   i++;
   }
}

int main(int argc, char **argv) {
	int case_num = 1;
	char buffer[100];
	string str;
	bool first = 0;
	int total_cases;
	int TC_num = 0;
	int A, B;
	
	ifstream read_file (argv[1]);

	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
			 } else {
				 stringstream ss(str);
				 ss >> A >> B;
				 int count = 0;
				 for (int i = A; i <= B; i++ ) {
				      list <int> D = digitalize(i);
					 flip_check(D, A, B, &count);
				 }
				 cout << "Case #" << ++TC_num <<": "<< count << endl;
			 }
	    }
	    read_file.close();
	}
}
