#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

pair<pair<int,int>,string> proc(vector<pair<pair<string,int>,string> >::iterator start, vector<pair<pair<string,int>,string> >::iterator end, string::iterator str, int N, char test) {
	vector<pair<pair<string,int>,string> >::iterator i=start;
	int rslt=N;
	int number=100000;
	string mystr;
	//cout << "PROC " << N << "...";
	while (i<end) {
		int score=N;
		//cout << "Di:" << i-start << endl;
		vector<pair<pair<string,int>,string> >::iterator j=i+1;
		//if (j<end) cout << i->first.first << ":" << j->first.first << endl;
		while (j<end && i->first.first==j->first.first) {
			//cout << "Dj:" << j-start << endl;
			j++;
		}
		//cout << "abc"<<endl;
		if (test!='*' && i->first.first.find_first_of(test)==string::npos) score++;
		// process range of words [i,j)
		if (j==i+1) {
			//cout << score << " " << test << " " << i->second << endl;
			//if (mystr.empty()) mystr=i->second;
			if (rslt<score || mystr.empty() || (rslt==score && number>i->first.second)) {
				rslt=score;
				mystr=i->second;
				number=i->first.second;
			}
			i=j;
			continue;
		}
		//cout << "abcc"<<endl;
		string::iterator strit=str;
		//int bad=0;
		while (1) {
			bool found=false;
			//cout << "find " << *strit << endl;
			for (vector<pair<pair<string,int>,string> >::iterator it=i;it<j;it++) {
				int pos=0;
				
				pos=it->second.find_first_of(*strit,0);
				//cout << pos << endl;
				while (pos!=string::npos) {
					found=true;
					it->first.first[pos]=*strit; // fill in blank
					pos=it->second.find_first_of(*strit,pos+1); // find next character position
				}
			}
			//cout << found << endl;
			if (found) {
				sort(i,j);
				pair<pair<int,int>,string> ans=proc(i,j,strit+1,score,*strit);
				if (rslt<ans.first.first || mystr.empty() || (rslt==ans.first.first && number > ans.first.second)) {
					rslt=ans.first.first;
					number=ans.first.second;
					mystr=ans.second;
				}
				break;
			}
			else strit++;
			//cout << *strit
		}

		i=j;
	}
	return pair<pair<int,int>,string>(pair<int,int>(rslt,number),mystr);
}

int main() {
	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		int N,M;
		cin >> N >> M;
		vector<pair<pair<string,int>,string> > dict;
		for (int n=0;n<N;n++) {
			string word;
			cin >> word;
			string blk(word.length(),'_');
			dict.push_back(pair<pair<string,int>,string>(pair<string,int>(blk,n),word));
		}
		sort(dict.begin(),dict.end());
		//cin >> M;
		cout << "Case #" << t << ":";
		for (int m=0;m<M;m++) {
			vector<pair<pair<string,int>,string> > mydict=dict;
			string order;
			cin >> order;
			pair<pair<int,int>,string> ans=proc(mydict.begin(),mydict.end(),order.begin(),0,'*');
			cout << " ";
			cout << ans.second;
			
		}
		cout << endl;
	}

	return 0;
}