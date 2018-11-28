// repeatNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
#ifdef GENERATE_DATA
	int A = 1000000, B = 2000000;
	fstream dout("F7", ios::out);
	for(long long j = A; j <= B; ++j) {
		stringstream iss;
		iss << j;
		string s = iss.str();
		set<long long> st;
		for(int k = 1; k < s.size(); ++k) { // for all shifts of this num
			string newS;
			for(int l = 0; l < s.size(); ++l) {
				int x = (l + k)%s.size();
				newS += s[x];
			}
			stringstream oss(newS);
			long long repeatNumber;
			oss >> repeatNumber;
			if(st.find(repeatNumber) == st.end()) {
				st.insert(repeatNumber);
			}
		}
		if(!st.empty()) {
			dout << j << " " << st.size() << " "; 
			for(set<long long>::const_iterator ci = st.begin(); ci != st.end(); ++ci) 
				dout << *ci << " "; 
			dout << endl;
		}
	}
	dout.close();
#endif

	vector< vector<int> > V2;
	vector< vector<int> > V3;
	vector< vector<int> > V4;
	vector< vector<int> > V5;
	vector< vector<int> > V6;
	vector< vector<int> > V7;
	fstream fd2("F2", ios::in);
	fstream fd3("F3", ios::in);
	fstream fd4("F4", ios::in);
	fstream fd5("F5", ios::in);
	fstream fd6("F6", ios::in);
	fstream fd7("F7", ios::in);


	for(int j = 0; j < 99-10+1; ++j) {
		int n, m;
		fd2 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd2 >> y;
			rotV.push_back(y);
		}
		V2.push_back(rotV);
	}
	cout << "Reading file F3... " << endl;
	for(int j = 0; j < 999-100+1; ++j) {
		int n, m;
		fd3 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd3 >> y;
			rotV.push_back(y);
		}
		V3.push_back(rotV);
	}
	cout << "Reading file F4... " << endl;
	for(int j = 0; j < 9999-1000+1; ++j) {
		int n, m;
		fd4 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd4 >> y;
			rotV.push_back(y);
		}
		V4.push_back(rotV);
	}
	
	cout << "Reading file F5... " << endl;;
	for(int j = 0; j < 99999-10000+1; ++j) {
		int n, m;
		fd5 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd5 >> y;
			rotV.push_back(y);
		}
		V5.push_back(rotV);
	}
	cout << "Reading file F6... " << endl;
	for(int j = 0; j < 999999-100000+1; ++j) {
		int n, m;
		fd6 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd6 >> y;
			rotV.push_back(y);
		}
		V6.push_back(rotV);
	}
	cout << "Reading file F7... " << endl;
	for(int j = 0; j < 9999999-1000000+1; ++j) {
		int n, m;
		fd7 >> n >> m;
		vector<int> rotV;
		for(int z = 0; z < m; ++z) {
			int y;
			fd7 >> y;
			rotV.push_back(y);
		}
		V7.push_back(rotV);
	}
	
	cout << "Done!" << endl;
	getchar();
	getchar();
	getchar();
	cout << "Processing in.txt now ... " << endl;
	fstream f("in.txt", ios::in);
	fstream fout("out.txt", ios::out);

	int T;
	f >> T;
	for(int i = 1; i <= T; ++i) {
		long long total = 0;
		long long A, B;
		f >> A >> B;
		if(A < 10) {
			total = 0;
		} else if (A < 100) {
			for(int k = A; k <= B; ++k) {
				int index = (k%100)-10;
				vector<int> v = V2[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		} else if (A < 1000) {
			for(int k = A; k <= B; ++k) {
				int index = (k%1000)-100;
				vector<int> v = V3[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		} else if (A < 10000) {
			for(int k = A; k <= B; ++k) {
				int index = (k%10000)-1000;
				vector<int> v = V4[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		} else if (A < 100000) {
			for(int k = A; k <= B; ++k) {
				int index = (k%100000)-10000;
				vector<int> v = V5[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		} else if (A < 1000000) {
			for(int k = A; k <= B; ++k) {
				int index = (k%1000000)-100000;
				vector<int> v = V6[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		} else if (A < 10000000) {
			for(int k = A; k <= B; ++k) {
				int index = (k%10000000)-1000000;
				vector<int> v = V7[index];
				for(int l = 0; l < v.size(); ++l) {
					if(k == v[l])
						continue;
					if(A <= v[l] && v[l] <= B) {
						++total;
					}
				}
			}
		}
		cout << "Case #" << i << ": " << total/2 << endl;		
		fout << "Case #" << i << ": " << total/2 << endl;
	}

#ifdef SMALL_INPUT_SOURCE
		long long repeatCount = 0;
		set<pair<long long, long long> > st;
		for(long long j = A; j <= B; ++j) {
			stringstream iss;
			iss << j;
			string s = iss.str();
			for(int k = 1; k < s.size(); ++k) { // for all shifts of this num
				string newS;
				for(int l = 0; l < s.size(); ++l) {
					int x = (l + k)%s.size();
					newS += s[x];
				}
				stringstream oss(newS);
				long long repeatNumber;
				oss >> repeatNumber;
				// cout << "Repeat number for " << j << " is " << repeatNumber ;
				// fout << "Repeat number for " << j << " is " << repeatNumber ;	
				if(repeatNumber != j && repeatNumber >= A && repeatNumber <= B) {
					// pair<long long, long long> p(j, repeatNumber);
					// if(st.find(p) == st.end()) {
						// st.insert(p);
						++repeatCount;
						// cout << " Yes!.";
						fout << repeatNumber << endl;
					// }
				}
				// cout << endl;
				// fout << endl;
			}
		}
		cout << "Case #" << i << ": " << repeatCount/2 << endl;
		fout << "Case #" << i << ": " << repeatCount/2 << endl;
	}
	f.close();
	fout.close();
#endif


	return 0;
}

