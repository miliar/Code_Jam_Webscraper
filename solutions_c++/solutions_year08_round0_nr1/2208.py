#include "iostream"
#include "string"
#include "list"
#include "algorithm"

using namespace std;

int main(){
	int N, S, Q;
	int i, j;
	cin >> N;
	cin.ignore();
	for(i = 0; i < N; i++){
		list<string> engines;
		char data[101];
		cin >> S;
		cin.ignore();
		for(j = 0; j < S; j++){
			string temp;
			cin.getline( data , 101);
			temp = data;
			engines.push_front( temp );
		}
		cin >> Q;
		cin.ignore();
		
		
		list<string> found;
		int count = 0;
		for(j = 0; j < Q; j++){
			string temp;
			cin.getline( data , 101);
			temp = data;
	
//			cout << temp << endl;
			
//			cout << found.size() << ":" << (S-1) << endl;
			
			if((found.size() < (S-1)) && find(found.begin(), found.end(), temp) == found.end()){
//				cout << "Adding: " << temp << endl;
				
				found.push_front(temp);
			}
			else if(found.size() == (S-1)  && find(found.begin(), found.end(), temp) == found.end()){
//				cout << "Count!!" << endl;
				found.clear();
				found.push_front(temp);
				count++;
			}

		}
		cout << "Case #" << (i+1) << ": " << count << endl;
	}
	
}
