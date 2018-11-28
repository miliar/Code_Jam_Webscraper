//============================================================================
//
//	@kirbdee
//	googlecodejam2011
//	round q
//
//============================================================================

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	//freopen("B-test.in","r",stdin);
	//freopen("B-test.out","w",stdout);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);

	//number of cases;
	int N;
	cin >> N;
	string line;

	for(int i=0; i<N;i++){
		vector<string> base;
		vector<string> oppose;
		string invoke;
		string output;
		cin >> line;
		for(int a=0; a<atoi(line.c_str());a++){
			cin>>line;
			base.push_back(line);
		}
		cin >> line;
		for(int b=0; b<atoi(line.c_str());b++){
			cin>>line;
			oppose.push_back(line);
		}
			cin>>line;
			cin>>invoke;

		// checked elements
			/*
		cout << i+1 << ":";
		for(int k=0; k<(int)base.size();k++) cout << base[k];
		cout << ":";
		for(int k=0; k<(int)oppose.size();k++) cout << oppose[k];
		cout << ":";
		for(int k=0; k<(int)invoke.size();k++) cout << invoke[k];
		cout << endl;
		*/

		//readinvoke
		for(int d=0; d<(int)invoke.size();d++){
			output+=invoke[d];
			if(output.size()>1){
				//checkcombo
				for(int e=0;e<(int)base.size();e++){
					//replace
					size_t pos= base[e].find(output[output.size()-1]);
					if(pos!=string::npos)
						if(base[e][(pos-1)%2] == output[output.size()-2]){
							output.resize(output.size()-1);
							output[output.size()-1]=base[e][2];
							break;
						}
				}
				//checkclear
				for(int f=0;f<(int)oppose.size();f++){
					//clear current
					size_t pos= oppose[f].find(output[output.size()-1]);
					if(pos!=string::npos){
						size_t cPos = output.find(oppose[f].substr((pos-1)%2,1));
						if(cPos !=string::npos){
							output.clear();
							break;
						}
					}

				}

			}
		}

		cout << "Case #" << i+1 << ": [";

		for(int o=0;o<output.size();o++){
			cout << output[o];
			if(o < output.size()-1) cout << ", ";
		}
		cout <<"]" << endl;
			//print all output elements

	}

	return 0;
}
