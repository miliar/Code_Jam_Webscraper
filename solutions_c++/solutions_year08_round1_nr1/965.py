#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;
int product_vec(vector<int>&vec1,vector<int>&vec2){
	int sum = 0;
	for(int i = 0; i < vec1.size(); i++){
		sum += vec1[i] * vec2[i];
	}
	return sum;
}
int compute(vector<int>&vec1,vector<int>&vec2)
{
	int min = product_vec(vec1, vec2);
	if(vec1.size() <=1)
		return min;
	vector<int> vec_tmp1;
	for(int i = 1; i < vec1.size();i++){
		vec_tmp1.push_back(vec1[i]);
	}
	for(int i = 0; i < vec1.size();i++){
		vector<int> vec_tmp2;
		int val = vec1[0]*vec2[i];
		for(int j = 0; j < vec1.size(); j++){
			if(j != i)
			vec_tmp2.push_back(vec2[j]);
		}
		/*cout << vec1.size() << endl;
		cout << vec2.size() << endl;
		cout << vec_tmp1.size() << endl;
		cout << vec_tmp2.size() << endl;*/
		val += compute(vec_tmp1, vec_tmp2);
		if (min > val)
			min = val;
	}	
	return min;
}
int main(int argc, char **argv)
{
  string line;
  ifstream myfile(argv[1]);
  char outfile[255];

  sprintf(outfile, "%s.out", argv[1]);
  ofstream out(outfile);

  if (myfile.is_open()) {

    getline(myfile, line);
    int cases_count = atoi(line.c_str());

    for (int round_i = 0; round_i < cases_count; round_i++) {
	
      getline(myfile, line);
      int dim = atoi(line.c_str());
	vector<int> vec1;
	vector<int> vec2;
       for(int i = 0; i < dim; i++){
		int tmp;
      		myfile >> tmp ;
		vec1.push_back(tmp);
	}
      getline(myfile, line);
       for(int i = 0; i < dim; i++){
		int tmp;
      		myfile >> tmp ;
		vec2.push_back(tmp);
	}
      getline(myfile, line);
      
	cout << vec1.size() <<endl;
	cout << vec2.size() <<endl;

      //string result = "";

      // main algorithm
      int result = compute(vec1, vec2);

      // main algorithm end


      out << "Case #" << round_i + 1 << ": " << result << endl;
    }
    myfile.close();
    out.close();
  }

  else
    cout << "Unable to open file";

  return 0;
}
