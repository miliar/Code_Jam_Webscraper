/*
 * C.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: ram
 */

#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;

#define f(i,a,b) for( i = ( a ); i < ( b ); ++ i )
#define fo(i,b) f( i, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define m memset

int main(){
	int T;
	cin >> T;
	int i;
	fo(i,T){
		cout << "Case #" << i+1 << ": ";
		int ans=0;
		int ia,ib;
		cin >> ia >> ib;
		//cout << "ia " << ia << " ib " << ib << endl;
		int i = 0;
		f(i,ia,ib+1){

			stringstream si;
			si << i;
			string s = si.str();
//			cout << "s = " << s << endl;
			vector<char> v;
			int z;
//			cout << "vector = ";
			fo(z,s.length()){
				v.pb(s[z]);
//				cout <<  v.at(z);
			}
//			cout << endl;
			int j;
			f(j,i+1,ib+1){

//				cout << "j = " << j<<  " length " << s.length() << endl;
				int z = 0;
				fo(z,s.length()){
					char a = v.front();
					v.erase(v.begin());
					v.pb(a);
					int tz;
					si.str("");
					fo(tz,v.size())
						si<<v.at(tz);
					string ts = si.str();
					int ti = atoi(ts.c_str());
					//cout << ti << " "<< j << endl;
					if (j==ti)
						{ans++; break;}
				}
			}

		}
		cout << ans << endl;
	}
}


