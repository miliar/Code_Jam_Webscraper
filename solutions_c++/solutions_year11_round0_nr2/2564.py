#include <stack>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream cin("B-large.in");
    ofstream cout("ret_large.txt");
    string str;
	int ncase;
	cin>>ncase;
	int i;
	for(int kcase=1;kcase<=ncase;kcase++){
		char hash_ret[101]={0};
		char opp[256][256]={0};
		char combin[256][256]={0};
		int c,d,n;
		char ch;
		cin>>c;
		for(i=0;i<c;i++){
			cin>>str;
			combin[str.at(0)][str.at(1)]=str.at(2);
			combin[str.at(1)][str.at(0)]=str.at(2);
		}
		cin>>d;
		for(i=0;i<d;i++){
			cin>>str;
			opp[str.at(0)][str.at(1)]=-1;
			opp[str.at(1)][str.at(0)]=-1;
		}
		cin>>n;
		cin>>str;
		if(n!=str.size()) cerr<<"error"<<endl;
		int total=0;
		for(i=0;i<n;i++){
			char ch=str.at(i);
			if(total==0){
				hash_ret[total]=ch;
				total+=1;
			}else{
				while(total>0){
                    char t=hash_ret[total-1];
                    if((combin[t][ch]>0)){
                        ch=combin[t][ch];
                        total-=1;
                    }else{break;}
				}
				bool isopp=false;
                if(total>0){
					int j=0;
                    for(j=total-1;j>=0;--j){
                        char t=hash_ret[j];
                        if(opp[t][ch]==-1){
                            total=0;
                            isopp=true;
                            break;

                        }
                    }
					//(j<0) break;
                }
                if(!isopp){
                    hash_ret[total]=ch;
					total+=1;
                }
			}
		}
		cout<<"Case #"<<kcase<<": [";
		if(total!=0){
			cout<<hash_ret[0];
			for(i=1;i<total;i++) cout<<", "<<hash_ret[i];
        }
        cout<<']';
        if(kcase!=ncase)cout<<endl;

	}
}
