#include <string>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <hash_map>
#include <unordered_map>


using namespace std;

int recycled(int A, int B);
vector<int> get_digits(int n);
int get_number(vector<int>&);

int main(int argc, char** argv)
{
	
	FILE *fp1, *fp2;
	int cases, A, B;

	fp1 = fopen("C-large.in", "r");
	if(fp1 == NULL) return 1;
	fp2 = fopen("result_number.out", "w");
	if(fp2 == NULL) return 1;

	fscanf(fp1, "%d", &cases);
	for(int i = 0; i < cases; ++i) {
		fscanf(fp1, "%d%d ", &A, &B);
    int total = recycled(A, B);		
    fprintf(fp2, "Case #%d: %d\n", i+1, total);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}

int recycled(int A, int B)
{
  if(A < 10 && B < 10) return 0; 
  int r = 0;
  vector<int>::iterator it;
  unordered_map<int, int> values; 

  for(int i = A; i < B; ++i) {
    vector<int> v = get_digits(i);    
    values.clear();
     for(int j = 0; j < v.size(); ++j) {     
       rotate(v.begin(), v.begin()+1, v.end());        
       int t = get_number(v);
       if(t > i && t <= B && values.find(t) == values.end()) {
         r++;
         values[t] = t;
       }
     }
  }
  return r;
}

vector<int> get_digits(int n)
{
  vector<int> vec;
  if(n < 10) 
    vec.push_back(n);
  else {
    while(n > 0) {
      int r = n % 10;
      vec.push_back(r);  
      n /= 10;
    }  
    
    reverse(vec.begin(), vec.end());
  }  
  return vec;
}


int get_number(vector<int>& vec)
{
  int r = 0;
  for(int i = 0; i < vec.size(); ++i) {
    r *= 10;  
    r += vec[i];
  }
  return r;  
}
