#include <vector>
#include <string>
#include <algorithm>

using namespace std;


bool term_comp_fst(const string& t1, const string& t2){
	return t1.at(0) < t2.at(0);
}

class alang{
public:
	int L;
	int D;
	int N;
	vector<string> dic;

	alang():L(0),D(0),N(0){
		dic.clear();
	}

	void add_dic(string str){
		dic.push_back(str);
	}

	void sort_dic(){
		sort(dic.begin(),dic.end());
	}

	int analysis(string str){
		vector<vector<char>> vterm;
		bool bbrk = false;
		int icnt = 0;

		for(int i=0;i<str.length();i++){
			if(str[i] == '('){
				bbrk = true;
				vterm.push_back(vector<char>());
				continue;
			}
			if(str[i] == ')'){
				bbrk = false;
				continue;
			}
			if(!bbrk)
				vterm.push_back(vector<char>());
			vterm.at(vterm.size()-1).push_back(str[i]);
		}

		if(vterm.size() != L || !vterm.at(0).size())
			return -1; //wrong

		for(int fst=0;fst<vterm.at(0).size();fst++){
			string sfst = "";
			sfst += vterm[0].at(fst);

			vector<string>::iterator lb = lower_bound(dic.begin(),dic.end(),sfst,term_comp_fst);
			if(lb == dic.end())
				continue;
			vector<string>::iterator ub = upper_bound(dic.begin(),dic.end(),sfst,term_comp_fst);

			for(vector<string>::iterator itr = lb;itr!=ub;itr++){
				bool bdif = false;
				for(int i=1;i<vterm.size();i++){
					if(!vterm.at(i).size())
						return -1; //wrong
					if(find(vterm.at(i).begin(),vterm.at(i).end(),(*itr).at(i)) == vterm.at(i).end()){
						bdif = true;
						break;
					}
				}
				if(!bdif)
					icnt++;
			}
		}

		return icnt;
	}

};
