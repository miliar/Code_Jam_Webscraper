#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;


int main(){
	//freopen("sample.in","r",stdin);
	//freopen("sample.out","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);
	//freopen("B-small-attempt1.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int C,D;
		cin>>C;
		vector<string> Formto;
		for (int CLoop = 0; CLoop<C; CLoop++) {
			string sFormto;
			cin>>sFormto;
			Formto.push_back(sFormto);
		}
		vector<string> Oppose;
		cin>>D;
		for (int DLoop = 0; DLoop<D; DLoop++) {
			string sOppose;
			cin>>sOppose;
			Oppose.push_back(sOppose);
		}
		int invokelength; cin>>invokelength;
		string InvokeOrder; cin>>InvokeOrder;
		string Rslt;
		for (int strLoop=0;strLoop<InvokeOrder.length(); strLoop++){
			if (Rslt.length()>0){
				//transform
				bool matched = false;
				for (unsigned int FormLoop=0; FormLoop<Formto.size(); FormLoop++){
					string sFormPair=Formto[FormLoop];
					if ( (Rslt[Rslt.length()-1] == sFormPair[0] && InvokeOrder[strLoop] == sFormPair[1])
						|| (Rslt[Rslt.length()-1] == sFormPair[1] && InvokeOrder[strLoop] == sFormPair[0]) ) {
						Rslt[Rslt.length()-1] = sFormPair[2];
						matched = true;
						break;
					}
				}
				if (!matched){
					//conflict check
					bool bOpposed = false;
					for (unsigned int OpposeLoop=0; OpposeLoop<Oppose.size();OpposeLoop++){
						for (unsigned int RLoop=0;RLoop<Rslt.length();RLoop++){
						    if ( (Rslt[RLoop] == Oppose[OpposeLoop][0] && InvokeOrder[strLoop] == Oppose[OpposeLoop][1]) 
								||(Rslt[RLoop] == Oppose[OpposeLoop][1] && InvokeOrder[strLoop] == Oppose[OpposeLoop][0]) ) {
							    bOpposed = true;
								break;
							}
						}
						if (bOpposed){
							break;
						}
					}
					if (bOpposed){
						Rslt.clear();
					} else {
						Rslt+=InvokeOrder[strLoop];
					}
				} else {
					continue;
				}
			} else {
				Rslt+=InvokeOrder[strLoop];
			}
		}
		cout<<"Case #"<<i+1<<": [";
		for (int RsltLoop=0;RsltLoop<Rslt.length();RsltLoop++) {
			cout<<Rslt[RsltLoop];
			if (RsltLoop < Rslt.length()-1) {
			    cout<<", ";
			}
		}
		cout<<"]"<<endl;
	}
	
	
}