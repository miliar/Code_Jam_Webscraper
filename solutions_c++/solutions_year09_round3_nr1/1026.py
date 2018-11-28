#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>

using namespace std;

void displayvec(vector<int> vec)
{	for(int i=0;i<vec.size();i++){
		cout << vec[i] << " ";
	}
	cout << endl;

	return ;
}

unsigned long long fun(int base, vector<int> vec)
{
	unsigned long long sum=0;
	for(int i=vec.size()-1;i>=0;i--){
		sum+=vec[i]*(pow((double)base,(double)((vec.size()-1)-i)));
	}
	return sum;
}


int main()
{
	ifstream ifile("data.txt");
	ofstream ofile("data1.txt");

	int n;
	ifile >> n;

	
	map<char,long> mp;

	string s;
	for(int i=0;i<n;i++){
		mp.clear();
        vector <bool> vec(256,false);
		int count=0;
		ifile >> s;
		//cout << s;
		mp[s[0]]=1;
		vec[(int)s[0]]=true;
		int flag=0;
		for(int j=1;j<s.size();j++){
			if(!vec[(int)s[j]]){
				if(flag==1)flag++;
				mp[s[j]]=flag;
				flag++;
				count++;
				vec[(int)s[j]]=true;
			}
		}
		vector<int> vect;
		vect.push_back(1);
		for(int j=1;j<s.size();j++){
			vect.push_back(mp[s[j]]);
		}

		unsigned long long num;
		//displayvec(vect);
		if(count==0){
			num=fun(count+2,vect);
		}else{
			num=fun(count+1,vect);
		}
			ofile <<"Case #" << i+1 << ": " << num << endl;
	}


	//system("pause");
	return 0;
}

