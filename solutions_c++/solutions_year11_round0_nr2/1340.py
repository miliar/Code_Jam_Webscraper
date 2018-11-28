#include <vector>
#include <iostream>
#include <string>
using namespace std;

struct Pair {
	char in1;
	char in2;
	char out;
};

struct Oppose {
	char in1;
	char in2;
};

int main() {
	int numTests;
	cin>>numTests;
	for(int test=0;test<numTests;test++){
		int numPair;
		cin>>numPair;
        Pair *pairArr = new Pair[numPair*2];
		for(int i=0;i<numPair;i++){
			string s;
			cin>>s;
			pairArr[i*2].in1=s[0];
			pairArr[i*2].in2=s[1];
			pairArr[i*2].out=s[2];
			pairArr[i*2+1].in1=s[1];
			pairArr[i*2+1].in2=s[0];
			pairArr[i*2+1].out=s[2];
		}
		int numOppose;
		cin>>numOppose;
		Oppose *opposeArr = new Oppose[numOppose*2];
		for(int i=0;i<numOppose;i++){
			string s;
			cin>>s;
			opposeArr[i*2].in1=s[0];
			opposeArr[i*2].in2=s[1];
			opposeArr[i*2+1].in1=s[1];
			opposeArr[i*2+1].in2=s[0];
		}
		int numInvoke;
		cin>>numInvoke;
		string invokeSeq;
		cin>>invokeSeq;
		vector<char> endSeq;
		for(int i=0;i<numInvoke;i++){
			bool b=false;
		    if(endSeq.empty()){
                 endSeq.push_back(invokeSeq[i]);
                 continue;                  
            }
            char in1=endSeq.back();
			endSeq.push_back(invokeSeq[i]);
			char in2=endSeq.back();
			for(int j=0;j<numPair*2;j++){
				if(in1==pairArr[j].in1 && in2==pairArr[j].in2){
                    endSeq.pop_back();
					endSeq.pop_back();
					endSeq.push_back(pairArr[j].out);
					b=true;
					break;
				}
			}
			if(b)
			     continue;
			for(int j=0;j<numOppose*2;j++){
				if(in2==opposeArr[j].in1){
					for(int k=0;k<endSeq.size()-1;k++){
						if(endSeq[k]==opposeArr[j].in2){
                            endSeq.clear();
                            break;
						}
					}
					if(endSeq.empty()){
                        break;                  
                     }
				}
			}
		}
		cout<<"Case #"<<(test+1)<<": [";
		for(int j=0;j<endSeq.size();j++)
		{
			cout<<endSeq[j];
			if(j!=(endSeq.size()-1))
			cout<<", ";
		}
		cout<<"]"<<endl;
	}
}
