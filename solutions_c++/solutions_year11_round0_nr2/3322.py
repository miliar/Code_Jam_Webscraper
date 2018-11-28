#include <vector>
#include <iostream>

using namespace std;

int main(){
	int cases, comb, erase, length, inv;
	char temp;
	bool skip;
	cin>>cases;
	vector <int> erase1, erase2;
	vector <char> comb1, comb2, comb3, e1, e2, result;
	for (int z=1; z<=cases; z++){
		cin>>comb;
		for (int i=0; i<comb;i++){
			cin>>temp;
			comb1.push_back(temp);
			cin>>temp;
			comb2.push_back(temp);
			cin>>temp;
			comb3.push_back(temp);
		}
		cin>>erase;
		for (int i=0; i<erase;i++){
			cin>>temp;
			e1.push_back(temp);
			cin>>temp;
			e2.push_back(temp);
		}
		erase1.assign(erase, 0);
		erase2.assign(erase, 0);
		cin>>length;
		cin>>temp;
		inv=0;
		result.push_back(temp);
		for (int i=0; i<erase; i++){
			if (result[0]==e1[i])
				erase1[i]++;
			if (result[0]==e2[i])
				erase2[i]++;
		}
		
		//checker
	/*	if (erase>0)
			cout<<e1[0]<<" "<<e2[0]<<endl; */

		for (int i=1; i<length; i++){

			//checker
	/*		for (int x=0; x< erase; x++)
				cout<<erase1[x]<<" "<<erase2[x]<<endl;*/

			skip=false;
			cin>>temp;
			for (int j=0; j<comb; j++){
				if (temp==comb1[j]){
					if (result[inv]==comb2[j]){
						for (int k=0; k<erase; k++){
							if (result[result.size()-1]==e1[k])
								erase1[k]--;
							if (result[result.size()-1]==e2[k])
								erase2[k]--;
						}
						result[inv]=comb3[j];
						skip=true;
						break;
					}
				}
				if (temp==comb2[j]){
					if (result[inv]==comb1[j]){
						for (int k=0; k<erase; k++){
							if (result[inv]==e1[k])
								erase1[k]--;
							if (result[inv]==e2[k])
								erase2[k]--;
						}
						result[inv]=comb3[j];
						skip=true;
						break;
					}
				}
			}
			if (!skip){
				for (int j=0; j<erase; j++){
					if (temp==e1[j])
						erase1[j]++;
					if (temp==e2[j])
						erase2[j]++;
					if (erase1[j]&&erase2[j]){
						skip=true;
						result.clear();
						for (int k=0; k<erase; k++){
							erase1[k]=0;
							erase2[k]=0;
						}
						if (i<length-1){
							cin>>temp;
							i++;
							inv=0;
							result.push_back(temp);
							for (int k=0; k<erase; k++){
								if (result[0]==e1[k])
									erase1[k]++;
								if (result[0]==e2[k])
									erase2[k]++;
							}
						}
						break;
					}
				}
			}
			if (!skip){
				result.push_back(temp);
				inv++;
			}
		}
		cout<<"Case #"<<z<<": [";
		for (int a=0; a<result.size(); a++){
			cout<<result[a];
			if (a!=result.size()-1)
				cout<<", ";
		}
		cout<<"]"<<endl;
		comb1.clear();
		comb2.clear();
		comb3.clear();
		e1.clear();
		e2.clear();
		erase1.clear();
		erase2.clear();
		result.clear();
	}
	return 0;
}
