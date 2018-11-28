#include<iostream>
#include<ext/hash_set>
#include<ext/hash_map>
#include<string>
#include<vector>

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
//         template<> struct hash< int >
//         {
//                 size_t operator()( const int& x ) const
//                 {
//                         return hash< const int >()( x.c_str() );
//                 }
//         };
}

using __gnu_cxx::hash_set;
using __gnu_cxx::hash_map;
using namespace std;


void insert_map(int val, string str, hash_map<int, string>& newmap) {
  if (str[0] < '0') {
    cout << "ERR" << str << "<" << val << endl;
    exit(0);
  }
  hash_map<int, string>::iterator it = newmap.find(val);
  if (it == newmap.end()) {
    newmap[val] = str;
    return;
  }
  if ((it->second).length() < str.length()) {
    return;
  }
  if ((it->second).length() > str.length()) {
    newmap[val] = str;
    return;
  }
  // Equal
  string oldstr = it->second;
  if(oldstr.compare(str) > 0) {
    newmap[val] = str;
    return;
  }
  return;
}

int main(int argc, char * argv[])
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    char w_mat[20][20];
    hash_map<int, string> str_mat[20][20];
    hash_map<int, string> global_map;
    int W, Q;
    cin >> W >> Q;
    for (int w = 0; w < W; w++) {
      for (int w2 = 0; w2 < W; w2++) {
	cin >> w_mat[w][w2];
	int val = w_mat[w][w2] - '0';
	//	if (val >=0) {
	  string valstr("");
	  valstr.push_back(w_mat[w][w2]);
	  if (val >=0 ) {
	    global_map[val] = valstr;
	    str_mat[w][w2][val] =  valstr;
	  } else {
	    //	    str_mat[w][w2][val] =  valstr;
	  }
	  //	}
      }
    }
    cout << "Case #" << t+1 << ":" << endl;
    for (int q = 0; q < Q; q++) {
      int req;
      cin >> req;
      bool sign=false;
      string answer("");
      while(answer.compare("") == 0) {
	if(global_map.find(req) != global_map.end()) {
	  answer = global_map.find(req)->second;
	  break;
	}
	for (int w = 0; w < W; w++) {
	  for (int w2 = 0; w2 < W; w2++) {
	    if (sign) {
	      //	      cout <<"SIGN " << endl;
	      if (w_mat[w][w2] < '0') {
		hash_map<int, string>& mapval = str_mat[w][w2];
		hash_map<int, string>::iterator it;
		for (it = mapval.begin();
		     it != mapval.end();
		     it++) {
		  if (w > 0) {
		    hash_map<int, string>& newmapval = str_mat[w-1][w2];
		    int new_char = w_mat[w-1][w2];
		    string temp = it->second;
		    temp.push_back(new_char);
		    int val = it->first;
		    if (w_mat[w][w2] == '+') {
		      val += new_char - '0';
		    } else {
		      if (w_mat[w][w2] == '-') {
			val -= new_char - '0';
		      } else {
			cout << "ERR";
			exit(0);
		      }
		    }
		    insert_map(val, temp, newmapval);
		    insert_map(val, temp, global_map);
		  }

		  if (w2 > 0) {
		    hash_map<int, string>& newmapval = str_mat[w][w2-1];
		    int new_char = w_mat[w][w2-1];
		    string temp = it->second;
		    temp.push_back(new_char);
		    int val = it->first;
		    if (w_mat[w][w2] == '+') {
		      val += new_char - '0';
		    } else {
		      if (w_mat[w][w2] == '-') {
			val -= new_char - '0';
		      } else {
			cout << "ERR";
			exit(0);
		      }
		    }
		    insert_map(val, temp, newmapval);
		    insert_map(val, temp, global_map);
		  }

		  if (w < W-1) {
		    hash_map<int, string>& newmapval = str_mat[w+1][w2];
		    int new_char = w_mat[w+1][w2];
		    string temp = it->second;
		    temp.push_back(new_char);
		    int val = it->first;
		    if (w_mat[w][w2] == '+') {
		      val += new_char - '0';
		    } else {
		      if (w_mat[w][w2] == '-') {
			val -= new_char - '0';
		      } else {
			cout << "ERR";
			exit(0);
		      }

		    }
		    insert_map(val, temp, newmapval);
		    insert_map(val, temp, global_map);
		  }

		  if (w2 < W-1) {
		    hash_map<int, string>& newmapval = str_mat[w][w2+1];
		    int new_char = w_mat[w][w2+1];
		    string temp = it->second;
		    temp.push_back(new_char);
		    int val = it->first;
		    if (w_mat[w][w2] == '+') {
		      val += new_char - '0';
		    } else {
		      if (w_mat[w][w2] == '-') {
			val -= new_char - '0';
		      } else {
			cout << "ERR";
			exit(0);
		      }
		    }
		    insert_map(val, temp, newmapval);
		    insert_map(val, temp, global_map);
		  }
		}		
	      }
	    } else {
	      //	      cout <<"SIGN NOT" << endl;
	      if (w_mat[w][w2] >= '0') {
		hash_map<int, string>& mapval = str_mat[w][w2];
		hash_map<int, string>::iterator it;
		for (it = mapval.begin();
		     it != mapval.end();
		     it++) {
		  if (w > 0) {
		    hash_map<int, string>& newmapval = str_mat[w-1][w2];
		    string temp = it->second;
		    temp.push_back(w_mat[w-1][w2]);
		    insert_map(it->first, temp, newmapval);
		  }
		  if (w2 > 0) {
		    hash_map<int, string>& newmapval = str_mat[w][w2-1];
		    string temp = it->second;
		    temp.push_back(w_mat[w][w2-1]);
		    insert_map(it->first, temp, newmapval);
		  }

		  if (w < W-1) {
		    hash_map<int, string>& newmapval = str_mat[w+1][w2];
		    string temp = it->second;
		    temp.push_back(w_mat[w+1][w2]);
		    insert_map(it->first, temp, newmapval);
		  }

		  if (w2 < W-1) {
		    hash_map<int, string>& newmapval = str_mat[w][w2+1];
		    string temp = it->second;
		    temp.push_back(w_mat[w][w2+1]);
		    insert_map(it->first, temp, newmapval);
		  }
		}
	      }
	    }
	  }
	}
	sign = !sign;
      }
    cout << answer << endl;

    }
    
  }
  return 0;
}
