#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream>

using namespace std;
int readInt(ifstream& fin){
	stringstream ss;
	string temp;
	int n=-1;
	getline(fin, temp); 
	ss << temp;
	ss >> n;
	return n;
}

int main() {

	int n, s, q;
	int ans, count; //count stores count of remaining options
	string name;

	map<string, bool> status;

	n=s=q=count=ans=0;

	ifstream fin("7.in");
	ofstream fout("7.out");

	n = readInt(fin);

	for(int i=0; i<n; i++){
		
		//clear state before each test case
		status.clear();
		ans=0;
		count=0;
		
		s = readInt(fin);

		for (int j=0; j<s; j++) {
			getline(fin, name);
			status[name]=true; 
			count++;
		}

		q = readInt(fin);

		if(q!=0){	
			for (int k=0; k<q; k++) {
		
				getline(fin, name);

				if(status[name]) count--; // if we're toggling to false keep count
				
				//if count has reached minimum retoggle all others to true and increase our
				//ans by one.
				if(count==0) {
					for(map<string,bool>::iterator a=status.begin(); a!=status.end(); a++)
						a->second = true;
						ans++;
						count=s-1;
				}
				status[name]=false; 
			}
		}
	fout << "Case #" << i + 1 << ": " << ans <<endl;
	cout << "Case #" << i + 1 << ": " << ans <<endl;
	}

	return 0;
}
