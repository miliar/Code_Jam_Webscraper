#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>

using namespace std;

void retira(){

}

int main(){
	int n, atual, aux, flag,caso=1,zero;
	string str;
	vector <char> number;
	char temp;
	stringstream ss;
	cin>>n; cin.ignore();
	for(int i=0; i<n; i++){
		getline(cin,str);
		number.clear();
		ss.clear();
		ss.str(str);
		while((ss>>temp)>0){
			number.push_back(temp);
		}
		for(atual=number.size()-1; atual>=0; atual--){
			//atual=number.size()-k;
			flag=0;
			for(int j=number.size()-1; j>atual; j--){
				//cout<<number[atual]<<"\t"<<str[j]<<endl;
				if(number[atual]<number[j]){
					//cout<<"Trocou: "<<atual<<" | "<<j<<endl;
					number.insert(number.begin()+atual,number[j]);
					number.erase(number.begin()+j+1);
					sort(number.begin()+atual+1,number.end());
					flag=1;
					break;	
				}
			}
			if(flag==1) break;
		}
		if(flag==0){
			sort(number.begin(),number.end());
			zero=0;
			while(number[zero]==48){
				zero++;
			}
			//cout<<"zero: "<<zero<<endl;
			number.insert(number.begin(),number[zero]);
			number.erase(number.begin()+zero+1);	
		       	number.insert(number.begin()+1,48);
		}
		cout<<"Case #"<<caso<<": ";
			caso++;
		for(int j=0; j<number.size(); j++) cout<<number[j];
		cout<<endl;
	}
}
