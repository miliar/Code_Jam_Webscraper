/*
 * recycled.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: kazemjahanbakhsh
 */
#include <iostream>
#include <sstream>
#include <map>

using namespace std;

int main(){
	map< pair<long, long>, int> found_m;
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++){
		long A = 0, B = 0;
		cin >> A >> B;
		long n, m;
		long recycled_pairs = 0;
		for(n = A; n < B; n++){
			//first convert n to a string
			string ns;
			stringstream out;
			out << n;
			ns = out.str();
			//cout << s << endl;
			for(int start = ns.length() - 1; start > 0; start--){
				//find the recycle pair of n
				int count = 0;
				string ms = ns;
				while(count < ns.length()){
					//cout << ns[start] << " ";
					ms[count] = ns[start];
					start++;
					start %= ns.length();
					count++;
				}
				//cout << endl << "ms: " << ms << endl;
				//convert ms to an integer
				istringstream buffer(ms);
				buffer >> m;
				//check if this m is valid
				if(m > n && m <= B){
					if(found_m.find(pair<long, long>(n,m)) == found_m.end()){
						//cout << "n: " << n << ", m: " << m << endl;
						recycled_pairs++;
						found_m.insert(pair< pair<long, long>,int>(pair<long, long>(n,m), 1));
					}else{
						map< pair<long, long>, int>::iterator it = found_m.find(pair<long, long>(n,m));
						//cout << "n: " << n << ", m = " << m << " with n = " << (*it).first.first << "!!!!!!!!!!" << endl;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << recycled_pairs << endl;
		found_m.clear();
	}
	return 0;
}

