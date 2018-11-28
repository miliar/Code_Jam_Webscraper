#define MAX 1001 // 2000001
#include <list>
#include <cmath>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int foo(int AA, int BB){
  //cout << endl << endl << AA << '\t' << BB << endl;
  set<pair<int,int>> pairs;
  int recycled;
  for(size_t t(12>AA?12:AA); t < BB; ++t){
    string a((int)ceil(log((double)t)/log(10.)),0);
    sprintf(&(a[0]), "%d\0", t);
    string b = a;
    for(size_t i(0); i < a.size() - 1; ++i){
      b.push_back(b[0]);
      b.erase(b.begin());
      if(b[0] != '0'){
        recycled = atoi(&(b[0]));
        if(AA <= recycled && recycled <= BB && recycled != t){
          if(t<recycled) pairs.insert(make_pair(t,recycled));
          else pairs.insert(make_pair(recycled,t));
        }
      }
    }
  }
  /*for(set<pair<int,int>>::iterator it = pairs.begin(); it != pairs.end(); it++){
    cout << (*it).first << '\t' << (*it).second << endl;
  }*/
  return pairs.size();
}


int main(){
  ifstream fin("a.in");
  ofstream fout("a.out");
  int c;
  fin >> c;
  int a, b;
  for(size_t i(0); i < c; ++i){
    fout << "Case #" << i+1 << ": ";
    fin >> a >> b;
    fout << foo(a, b) << endl;
  }
  system("pause");
}


//bool isRecycled(int a, int b){
//  char A[8], B[8];
//  sprintf_s(A, "%d", a);
//  sprintf_s(B, "%d", b);
//  string strA = string(A);
//  string strB = string(B);
//  for(size_t i(0); i < strA.size(); ++i){
//    string strC;
//    for(size_t j(0); j < strA.size(); ++j){
//      strC.push_back(strA[(i+j)%strA.size()]);
//    }
//    if(strB == strC){
//      return true;
//    }
//  }
//  return false;
//}
//
//int main(){
//  cout << "(23,32): " << isRecycled(23,32) << endl;
//
//  vector<vector<bool> > recycled(MAX, vector<bool>(MAX, false));
//  bool val;
//  for(size_t i(0); i < MAX-1; ++i){
//    for(size_t j(i+1); j < MAX; ++j){
//      val = isRecycled(i,j);
//      recycled[i][j] = val;
//      if(i == 23 && j == 32) 
//        cout << "";
//    }
//  }
//  cout << '\t';
//  for(size_t j(0); j < MAX; ++j){
//    cout << (j-(j%10))/10 << ' ';
//  }
//  cout << endl;
//  cout << '\t';
//  for(size_t j(0); j < MAX; ++j){
//    cout << j% 10 << ' ';
//  }
//  cout << endl << endl;
//  for(size_t i(0); i < MAX-1; ++i){
//    cout << i << '\t';
//    for(size_t j(0); j < MAX; ++j){
//      if(recycled[i][j]) cout << 1 << ' ';
//      else cout << "  ";
//    }
//    cout << endl;
//  }
//
//
//  system("pause");
//}
//
//
//
////int main(){
////  vector<vector<bool> > recycled(MAX, vector<bool>(MAX,false));
////  
////  cout << "recycled\n";
////  for(size_t A = 0; A < MAX - 1; ++A){
////    for(size_t B = A + 1; B < MAX; ++B){
////      recycled[A][B] = isRecycled(A,B);
////      cout << recycled[A][B] << ' ';
////    }
////    cout << endl;
////  }
////  
////  vector<vector<int> > matrix(MAX, vector<int>(MAX,0));  
////  for(size_t A = 0; A < MAX; ++A){
////    for(size_t B = A + 1; B < MAX; ++B){
////      if(A - 1 == B) if(recycled[A][B]) matrix[A][B] = 1;
////      else
////        if(recycled[A][B]) matrix[A][B] = 1 + matrix[A][B-1];
////        else matrix[A][B] = matrix[A][B];
////    }
////  }
////
////  cout << "Filename\n";
////  string in;
////  cin >> in;
////  ifstream fin(&(in[0]));
////  int cases;
////  fin >> cases;
////  ofstream fout("out.txt");
////  int a, b;
////  for(size_t i(0); i < cases; ++i){
////    fout << "Case #" << 1+i << ": ";
////    fin >> a >> b;
////    fout << matrix[a][b] << endl;
////  }
////  system("pause");
////}