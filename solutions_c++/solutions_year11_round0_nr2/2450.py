#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <ctime>
//#include <fstream>
using namespace std;

#define INF 1000000000
#define PI acos(-1.0)

string a[100],b[100],c[100];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for (int t=1; t<=tt; t++){
		int c;
		cin>>c;
		for (int i=0; i<c; i++){
			cin>>a[i];
		}
		int d;
		cin>>d;
		for (int i=0; i<d; i++){
			cin>>b[i];
		}

		int n;
		cin>>n;
		string s;
		cin>>s;

		string res="";

		for (int i=0; i<s.length(); i++){
			if (res.length()>0){
				char c1=res[res.length()-1],c2=s[i];

				bool ok=0;

				for (int i=0; i<c; i++){
					if ((a[i][0]==c1 && a[i][1]==c2) || (a[i][0]==c2 && a[i][1]==c1)){
						res.pop_back();
						res+=a[i][2];
						ok=1;
						break;
					}
				}

				if (ok) continue;
			}

			if (res.length()>0){

				bool okk=0;


				for (int j=0; j<res.size(); j++){

					char c1=res[j],c2=s[i];

					bool ok=0;
				
					for (int i=0; i<d; i++){
						if ((b[i][0]==c1 && b[i][1]==c2) || (b[i][1]==c1 && b[i][0]==c2)){
							res.clear();
							ok=1;
							break;
						}
					}

					if (ok) {
						okk=1;
						break;
					}

				}

				if (okk) continue;
			}

			res+=s[i];
		}

		cout<<"Case #"<<t<<": [";
		if (res.size()) cout<<res[0];
		for (int i=1; i<res.size(); i++){
			cout<<", "<<res[i];
		}
		cout<<"]"<<endl;
	}

}