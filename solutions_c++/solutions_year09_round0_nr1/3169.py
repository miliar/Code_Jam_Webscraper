#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<map>
#include<cstdlib>
#include <queue>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifile("data.txt");

	int word_len;
	int n;
	int a;

	ifile >> word_len;
	ifile >> a;//vocabulary
	ifile >> n;//no. of test cases

	vector <string> vec;
	string s="";
	for(int i=0;i<a;i++){
		ifile>>s;
		vec.push_back(s);
		s="";
	}

    
	int flag=0;
	string temp="";
	vector<string> vv;
	vector <bool> test;
    ofstream ofile("out.txt");
    int count=0;

	for( int j=0;j<n;j++){
		ifile >> s;
		for(int i=0;i<s.size();i++){
			if(s[i]=='('){
				flag=1;
			}else if(flag==1){
				if(s[i]==')'){
					vv.push_back(temp);
					temp="";
					test.push_back(false);
					flag=0;
					continue;
				}
				temp.push_back(s[i]);
			}else if(flag==0){
				temp.push_back(s[i]);
				vv.push_back(temp);
				test.push_back(true);
				temp="";
			}
		}
		if(temp.size()!=0){
			vv.push_back(temp);
			test.push_back(true);
			temp="";
		}

		bool chk=false;
		flag=0;

        string d="";
        
    	for(int i=0;i<vec.size();i++){
			for(int k=0;k<vec[i].size();k++){
				if(test[k]){
                    d.push_back(vec[i][k]);
					if(vv[k]==d){
						chk=true;
					}else{
						chk=false;
						break;
					}
                    d="";
				}else if(!test[k]){
					for(int z=0;z<vv[k].size();z++){
						if(vv[k][z]==vec[i][k]){
							flag=1;
							chk=true;
							break;
						}
					}
					if(flag==0){
						chk=false;
                        break;
					}
				}
                flag=0;

			}
            if(chk)count++;
            chk=false;
            d="";
            flag=0;
		}
        ofile << "Case #" << j+1 <<": " << count << endl;

        count=0;
        vv.clear();
        test.clear();
        flag=0;
	}



  //system("pause");
  return 0;
}
